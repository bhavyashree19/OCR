import subprocess
import streamlit as st

def check_tesseract():
    try:
        # Run the Tesseract command
        result = subprocess.run(['tesseract', '--version'], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

st.title("Tesseract Check")
st.write("Checking if Tesseract is installed...")

tesseract_output = check_tesseract()
st.write("Tesseract Output:")
st.code(tesseract_output)
