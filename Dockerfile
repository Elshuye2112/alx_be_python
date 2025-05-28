# Use official Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy all files from your repo into /app inside the container
COPY . /app

# Default command: just print Python version (override when running)
CMD ["python", "--version"]