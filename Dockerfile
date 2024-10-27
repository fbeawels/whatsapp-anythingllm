# Use an official Python runtime as a parent image
FROM python:3.12.4-slim

# Install waitress WSGI server
RUN pip install pip waitress --upgrade

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Add the current directory contents into the container at /app
COPY ./app /apps/app
COPY serve.py /apps

# Set the working directory in the container to /app
WORKDIR /apps

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/apps/app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Create a new user 'myuser' with UID 1000
RUN useradd -m awels && chown -R awels /apps

# Set the user for the subsequent instructions and run the container as this user
USER awels

# Run app.py when the container launches
CMD ["python", "serve.py"]
