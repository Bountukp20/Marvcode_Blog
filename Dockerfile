# Use an official Python runtime as a parent image
# FROM python:3.10.4

# Set the working directory to /app
# WORKDIR /app

# Use the Debian base image
# FROM debian:bullseye

# Install necessary packages for creating the virtual environment
# RUN apt-get update && apt-get install -y python3-venv python3-pip

# Create a virtual environment and activate it
# RUN python3 -m venv /opt/venv
# ENV PATH="/opt/venv/bin:$PATH"

# Copy the current directory contents into the container at /app
# COPY . /app

# Install the project dependencies
# RUN pip install -r requirements.txt -v

# Set the working directory to /app
# WORKDIR /app

# Expose port 80 for the application to use
# EXPOSE 80

# Install necessary tools
# RUN apt-get update && apt-get install -y python3-venv python3-pip

# Copy the requirements file into the container
# COPY requirements.txt .

# Install Python packages
# RUN python3 -m venv /opt/venv && \
#     . /opt/venv/bin/activate && \
#     pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
# COPY . .

# Set the entry point for the application
# ENTRYPOINT ["python", "app.py"]

# Define environment variable
# ENV NAME World


# Use the Python 3.8 image as the base image
FROM python:3.10.4

# Set the working directory in the container
# WORKDIR marvcode_blog/

# Install necessary tools and libraries for MySQL
RUN apt-get update && apt-get install -y python3-dev default-libmysqlclient-dev build-essential

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python packages
RUN python3 -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY blog /app

# Set the entry point for the application
ENTRYPOINT ["python", "/blog/app.py"]