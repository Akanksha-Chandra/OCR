
# OCR and Document Search Application

This is a simple web-based application that performs Optical Character Recognition (OCR) on uploaded images containing text in English and Hindi. It extracts text from the image and allows users to search for keywords within the extracted text. The application is built using **Streamlit**, **OpenCV**, **Pytesseract**, and **Pillow**.

## Features
- Upload images in **JPEG**, **PNG**, or **JPG** format.
- Preprocess images using OpenCV for better OCR performance.
- Extract text from images in both **English** and **Hindi** using **Tesseract-OCR**.
- Search functionality to find keywords in the extracted text.

## Requirements
To run the application, you need the following:

### 1. Python Libraries:
- **Streamlit**: For building the web app.
- **Pillow**: For image handling.
- **Pytesseract**: For OCR functionality.
- **OpenCV**: For image preprocessing.
- **NumPy**: For numerical operations on image arrays.

You can install these libraries via pip:

```bash
pip install streamlit pillow pytesseract opencv-python-headless numpy
```

### 2. Tesseract-OCR:
- You must have **Tesseract-OCR** installed on your system.
- Download it from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract).
- After installing, update the path in the script to the location where Tesseract is installed:
  ```python
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  ```

## How to Run the Application
1. **Clone or download the repository**.
2. Make sure you have all the required dependencies installed.
3. Open a terminal or command prompt, navigate to the folder containing the application script, and run:
   ```bash
   streamlit run app.py
   ```
4. A browser window will open with the application interface.

## Usage
1. **Upload an Image**: Click on the "Upload an Image" button and choose an image file (JPEG, PNG, JPG) to upload.
2. **View Extracted Text**: Once the image is uploaded, the app will preprocess the image and use Tesseract to extract the text, which will be displayed on the screen.
3. **Search for Keywords**: Enter a keyword in the search bar to find occurrences in the extracted text.

## Example Workflow
1. Upload an image with both English and Hindi text.
2. The app will display the image and the extracted text.
3. You can enter keywords (either in English or Hindi) to search within the extracted text.


## Notes
- The path to Tesseract must be correctly set in the Python script for the OCR to work.
- For better accuracy, ensure that the uploaded images are clear and high-quality.
- Tesseract’s performance on Hindi text may require fine-tuning based on the font, quality, and complexity of the images.

## Contributing
Feel free to open an issue or submit a pull request if you find bugs or want to add new features to the app.
