# OCR
# Image Text Extraction using OCR and Tesseract
 This is a Streamlit-based web application that performs Optical Character Recognition(OCR) for extracting text from images containing text in both english and Hindi. It does preprocessing on images, scans the image quality, and also underlines keyword words in the extracted text.
 
## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Running the Application Locally](#running-the-application-locally)
- [Deployment on Streamlit Sharing](#deployment-on-streamlit-sharing)
 
## Features
- Upload pictures in JPG, JPEG, or PNG formats
- Extract text from images in English and Hindi
- Search and get the keywords highlighted
- The extracted text is saved as a plain text  file

## Requirements
- Python 3.7 or above
- Streamlit
- Pytesseract
- Pillow
- Tesseract-OCR installed in machine
- Github
- Streamlit Sharing

## Setup Instructions
1. **Clone the repository:**
  ```bash
git clone https://github.com/bhavyashree19/OCR.git   cd OCR

2. **Create a virtual environment**
   python -m venv venv
   source venv/bin/activate
3. **Install the required packages**
    pip install -r requirements.txt
4. **Install Tesseract-OCR**
    Download and install Tesseract from GitHub

## Running the Application Locally
1. Set the Tesseract path:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

2. Start the Streamlit application
    streamlit run ocr_app.py
3. Open the browser and navigate to:
    http://localhost:8501
    
## Deployment on Streamlit Sharing
- Go to Streamlit Sharing website
- Click on "Sign in with Github"
- Click on "New app"
- Click "Deploy


