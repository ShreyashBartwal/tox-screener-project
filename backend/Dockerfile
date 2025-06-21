# Start from an official, lightweight Python image.
# This is our base operating system.
FROM python:3.11-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy just the requirements file first. This is a Docker best practice
# that allows for faster rebuilds by caching the installed packages.
COPY ./requirements.txt /app/requirements.txt

# Install the Python dependencies from the requirements file.
RUN pip install --no-cache-dir -r /app/requirements.txt

# Now, copy the rest of your backend application code into the container.
COPY . /app

# Tell Docker what command to run when the container starts.
# It will run uvicorn on port 8000, listening on all available network interfaces.
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
