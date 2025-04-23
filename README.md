# FastAPI Hotdog App

This project is a FastAPI-based application that leverages a pre-trained AI model to classify images, specifically determining whether an uploaded image is a hotdog or not. The application utilizes a Keras deep learning model for image recognition and provides a web interface for seamless user interaction. By integrating FastAPI with AI-driven image classification, this project showcases the power of machine learning in real-time applications.

## File Structure
```
is-it-hotdog/
|
├── static/
|  └──index.html
|
├── Dockerfile
├── keras_model.h5
├── labels.txt
├── main.py
├── README.md
└── requirements.txt
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fastapi-hotdog-app.git
   cd fastapi-hotdog-app
   ```

2. Create a virtual environment:
   ```
   virtualenv -p python3.10 env
   source env/bin/activate  # On Windows use `. env/bin/activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the FastAPI server:
   ```
   uvicorn main:app --reload
   ```

2. Open your browser and go to `http://127.0.0.1:8000`.

3. Use the provided form to upload an image and check if it is a hotdog.

## Docker Instructions

To build and run the application using Docker, follow these steps:

1. Build the Docker image:
   ```
   docker build -t fastapi-hotdog-app .
   ```

2. Run the Docker container:
   ```
   docker run -p 8000:8000 fastapi-hotdog-app
   ```

3. Open your browser and go to `http://127.0.0.1:8000`.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
