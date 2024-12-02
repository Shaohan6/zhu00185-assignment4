# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all Python files to the container
COPY . /app

# Install any dependencies (if required)
# RUN pip install --no-cache-dir -r requirements.txt  # Uncomment if you have a requirements.txt

# Command to run the app
CMD ["python", "quiz_app.py"]
