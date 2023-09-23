# Use an official Python runtime as a parent image
FROM python:3.10.4

# Set the working directory to /app
WORKDIR /app

# Use the Debian base image
FROM debian:bullseye

# Update the package list and install necessary packages
RUN apt-get update && apt-get install -y python3 python3-pip

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create a virtual environment and activate it
RUN python3 -m venv /opt/venv && . /opt/venv/bin/activate

# Install the project dependencies
RUN pip install -r requirements.txt

# Expose port 80 for the application to use
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]