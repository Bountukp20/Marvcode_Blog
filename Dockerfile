# Use an official Python runtime as a parent image
FROM python:3.x

# Set the working directory to /app
WORKDIR /app

# Install MySQL development dependencies
RUN apt-get update && apt-get install -y libmysqlclient-dev

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN python -m venv /opt/venv && . /opt/venv/bin/activate && pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]