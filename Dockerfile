# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy source code
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run server
CMD ["python", "server.py"]
