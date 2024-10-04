import streamlit as st
from PIL import Image
import pytesseract
import cv2
import numpy as np

# Specify the correct path to Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update the path as needed

# Title for the web app
st.title("OCR and Document Search Application")

# File uploader to allow users to upload an image
uploaded_image = st.file_uploader("Upload an Image (JPEG, PNG)", type=["png", "jpg", "jpeg"])

# Function to preprocess the image for OCR
def preprocess_image(image):
    # Convert the image to an array using OpenCV
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply adaptive thresholding to get a binary image
    processed_image = cv2.adaptiveThreshold(
        gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )
    
    return processed_image

# If an image is uploaded
if uploaded_image is not None:
    # Open the image
    img = Image.open(uploaded_image)
    
    # Display the uploaded image on the web page
    st.image(img, caption='Uploaded Image', use_column_width=True)
    
    # Preprocess the image
    processed_image = preprocess_image(img)
    
    # Perform OCR using pytesseract
    extracted_text = pytesseract.image_to_string(processed_image, lang="eng+hin")
    
    # Show extracted text
    st.subheader("Extracted Text")
    st.write(extracted_text)
    
    # Search functionality
    st.subheader("Search in Extracted Text")
    search_query = st.text_input("Enter a keyword to search")
    
    # If user enters a search query
    if search_query:
        if search_query.lower() in extracted_text.lower():
            st.write(f"Keyword '{search_query}' found in the text.")
        else:
            st.write(f"Keyword '{search_query}' not found.")
