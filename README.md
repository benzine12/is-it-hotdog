# FastAPI Hotdog App

This project is a simple FastAPI application that allows users to upload an image and determines whether the image is a hotdog or not.

## Project Structure

```
fastapi-hotdog-app
├── src
│   ├── app.py               # Main application file
│   ├── templates
│   │   └── index.html       # HTML template for image upload
│   └── static
│       └── styles.css       # CSS styles for the HTML page
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fastapi-hotdog-app.git
   cd fastapi-hotdog-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the FastAPI server:
   ```
   uvicorn src.app:app --reload
   ```

2. Open your browser and go to `http://127.0.0.1:8000`.

3. Use the provided form to upload an image and check if it is a hotdog.

## Dependencies

- FastAPI
- Uvicorn
- Any additional libraries required for image processing (e.g., Pillow, TensorFlow, etc.)

## License

This project is licensed under the MIT License. See the LICENSE file for more details.