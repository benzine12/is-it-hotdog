from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import shutil
import os
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load model and labels at startup for better performance
model = load_model("keras_Model.h5", compile=False)
with open("labels.txt", "r") as f:
    class_names = f.readlines()

def classify_image(image_path):
    """
    Classify an image using the loaded Keras model.
    
    Args:
        image_path (str): Path to the image file to classify
        
    Returns:
        tuple: (class_name, confidence_score)
    """
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)
    
    # Create input array
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    
    # Open and preprocess image
    try:
        image = Image.open(image_path).convert("RGB")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
        
        # Convert to array and normalize
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
        data[0] = normalized_image_array
        
        # Make prediction
        prediction = model.predict(data)
        index = np.argmax(prediction)
        confidence_score = float(prediction[0][index])
        class_name = class_names[index][2:].strip()
        
        return class_name, confidence_score
        
    except Exception as e:
        return f"Error processing image: {str(e)}", 0.0

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    if file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        # Save uploaded file temporarily
        temp_path = f"temp_{file.filename}"
        try:
            with open(temp_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            
            # Classify the image
            class_name, confidence = classify_image(temp_path)
            
            return {
                "class": class_name,
                "confidence": confidence,
                "success": True
            }
            
        except Exception as e:
            return {"error": str(e), "success": False}
            
        finally:
            # Clean up temporary file
            if os.path.exists(temp_path):
                os.remove(temp_path)
    
    return {"error": "Invalid file type. Please upload an image.", "success": False}