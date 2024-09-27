import streamlit as st
import easyocr
from PIL import Image, ImageFilter, ImageEnhance
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def assess_image_quality(img):
    """Check image quality (size, mode) before processing."""
    if img is None or img.size[0] < 100 or img.size[1] < 100:
        logging.error("Image quality is poor. Please provide a larger image.")
        return False
    if img.mode not in ["RGB", "L"]:
        logging.error("Unsupported image mode. Please use RGB or Grayscale images.")
        return False
    return True

def preprocess_image(img):
    """Preprocess the image for better OCR results."""
    img = img.convert('L')  # Convert to grayscale
    img = img.filter(ImageFilter.SHARPEN)  # Apply sharpening filter
    
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.5)  # Increase contrast by 50%
    
    return img

def perform_ocr(img):
    """Perform OCR on the image and return the extracted text."""
    reader = easyocr.Reader(['en', 'hi'])  # Specify the languages you need
    result = reader.readtext(img, detail=0)  # detail=0 returns only text
    return " ".join(result)

def highlight_keywords(text, keywords):
    """Highlight the keywords in the extracted text."""
    for keyword in keywords:
        text = text.replace(keyword, f"<mark>{keyword}</mark>")
    return text

def main():
    """Main function to orchestrate the OCR process."""
    st.title("OCR Text Extractor from Image Upload")
    
    # File upload for the image
    uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        
        if not assess_image_quality(img):
            st.error("Image quality is poor. Please provide a larger image.")
            return
        
        img = preprocess_image(img)

        # Perform OCR for both Hindi and English
        extracted_text = perform_ocr(img)

        # Prepare the final output
        final_text = extracted_text.strip() if extracted_text else ""
        
        # Log the extracted text
        logging.info("Extracted Text:")
        logging.info(final_text)

        # Display the extracted text in the app
        st.subheader("Extracted Text:")
        st.text(final_text)

        # Keyword input for searching
        keywords = st.text_input("Enter keywords to search within the extracted text (comma-separated):")
        
        if keywords:
            keyword_list = [k.strip() for k in keywords.split(",")]
            highlighted_text = highlight_keywords(final_text, keyword_list)
            st.markdown("### Search Results:")
            st.markdown(highlighted_text, unsafe_allow_html=True)

        # Save the result as a plain text file
        output_filename = 'extracted_text.txt'
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(final_text)

        st.success(f"Text saved to '{output_filename}'")

if __name__ == "__main__":
    main()
