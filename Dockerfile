FROM python:3.12-slim

# Install Tesseract
RUN apt-get update && apt-get install -y tesseract-ocr && apt-get clean

# Set working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Command to run the app
CMD ["streamlit", "run", "ocr_app.py"]
