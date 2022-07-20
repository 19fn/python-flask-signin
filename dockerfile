FROM python:3.10.5-slim-bullseye

# Create working directory
WORKDIR /app

# Copy all files
COPY . /app/

# Update system
RUN apt-get update -y
# Upgrade pip
RUN python3 -m pip install --upgrade pip
# Install virtual environment
RUN python3 -m venv /app/venv

# Enable virtual environment
ENV PATH="/app/venv/bin:$PATH"

# Open port 80 (http)
EXPOSE 80

# Install python dependencies
RUN python3 -m pip install -r requirements.txt

# Set flask environment variable
ENV FLASK_APP="app"
ENV FLASK_ENV="production"

# Run flask --host=0.0.0.0 (This tells operating system to listen on all public IPs.)
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=8080"]

