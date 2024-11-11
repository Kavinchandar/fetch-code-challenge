# Use the official Python image as a base
FROM python:3.9-slim

# Set a working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . /app

# Expose the port that the Flask app will run on
EXPOSE 8080

# Command to run the application
CMD ["python", "controller.py"]
