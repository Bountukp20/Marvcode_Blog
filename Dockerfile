# Use an official Python runtime as a parent image
FROM python:3.10.4

# Set the working directory to /app
WORKDIR /app

# Use the Debian base image
FROM debian:bullseye

# Install necessary packages for creating the virtual environment
RUN apt-get update && apt-get install -y python3-venv python3-pip

# Create a virtual environment and activate it
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy the current directory contents into the container at /app
COPY . /app

# Install the project dependencies
RUN pip install -r requirements.txt

# Set the working directory to /app
WORKDIR /app

# Expose port 80 for the application to use
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]