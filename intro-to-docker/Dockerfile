# Start with a base Python image:
FROM python:3.11-slim

# Set up the working directory:
WORKDIR /app

# Install dependencies (this order is important for caching):
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code:
COPY . .

# Expose the port and set the startup command:
EXPOSE 8000
CMD ["python", "app.py"]
