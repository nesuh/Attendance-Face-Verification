# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port (same as uvicorn default)
EXPOSE 8000

# Command to run the FastAPI app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


# Explanation:
# python:3.11-slim: lightweight Python image.

# We copy and install dependencies first to use Docker layer caching.

# Copy the whole app afterward.

# Expose port 8000 for FastAPI.

# Run uvicorn pointing to your FastAPI app in app/main.py (app.main:app).

# --reload enables auto-reload (good for development, remove it in production).