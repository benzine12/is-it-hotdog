# Description: Dockerfile for the FastAPI application
FROM python:3.10.16

# Set the working directory
WORKDIR /usr/src/app

# Copy the entire application code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 80

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "443", "--ssl-keyfile", "/etc/letsencrypt/live/is-it-hotdog.duckdns.org/privkey.pem", "--ssl-certfile", "/etc/letsencrypt/live/is-it-hotdog.duckdns.org/fullchain.pem"]