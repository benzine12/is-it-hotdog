# Description: Dockerfile for the FastAPI application
FROM python:3.10.16

# Set the working directory
WORKDIR /usr/src/app

# Copy the entire application code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]