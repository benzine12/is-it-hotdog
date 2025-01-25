# FastAPI Hotdog App

This project is a simple FastAPI application that allows users to upload an image and determines whether the image is a hotdog or not.

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
   source env/bin/activate  # On Windows use `env\Scripts\activate`
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