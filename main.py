import logging
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
   CORSMiddleware,
   allow_origins=["*", "https://tubular-cascaron-a48605.netlify.app"],
   allow_credentials=False,
   allow_methods=["*"],
   allow_headers=["*"],
)

logger.info("Loading model and labels...")
model_path = os.path.join(os.path.dirname(__file__), "keras_model.h5")
labels_path = os.path.join(os.path.dirname(__file__), "labels.txt")
model = load_model(model_path, compile=False)
with open(labels_path, "r") as f:
   class_names = f.readlines()
logger.info("Model loaded successfully")

def classify_image(image_path):
   logger.info(f"Processing image: {image_path}")
   np.set_printoptions(suppress=True)
   data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
   try:
       image = Image.open(image_path).convert("RGB")
       size = (224, 224)
       image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
       image_array = np.asarray(image)
       normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
       data[0] = normalized_image_array
       
       logger.info("Starting prediction")
       prediction = model.predict(data)
       logger.info("Prediction completed")
       
       index = np.argmax(prediction)
       confidence_score = float(prediction[0][index])
       class_name = class_names[index][2:].strip()
       return class_name, confidence_score
   except Exception as e:
       logger.error(f"Error in classification: {str(e)}")
       return f"Error processing image: {str(e)}", 0.0

@app.post("/api/classify/")
async def classify_upload(file: UploadFile = File(...)):
   logger.info(f"Received file: {file.filename}")
   if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
       return {"error": "Invalid file type. Please upload an image.", "success": False}
   
   temp_path = f"temp_{file.filename}"
   try:
       with open(temp_path, "wb") as buffer:
           shutil.copyfileobj(file.file, buffer)
       logger.info("File saved temporarily")
       
       class_name, confidence = classify_image(temp_path)
       return {
           "class": class_name,
           "confidence": confidence,
           "success": True
       }
   except Exception as e:
       logger.error(f"Upload error: {str(e)}")
       return {"error": str(e), "success": False}
   finally:
       if os.path.exists(temp_path):
           os.remove(temp_path)
           logger.info("Temporary file removed")

@app.get("/test")
async def root():
   return {"message": "Hello World"}

if __name__ == "__main__":
   import uvicorn
   port = int(os.environ.get("PORT", 10000))
   uvicorn.run("main:app", host="0.0.0.0", port=port)