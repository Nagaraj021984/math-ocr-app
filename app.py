import streamlit as st
from PIL import Image
import pytesseract

# Link to Tesseract
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

# Title of the app
st.title("📷 Math Problem OCR")

# File uploader for image input
uploaded_image = st.file_uploader("Upload an image of a math problem", type=["jpg", "jpeg", "png"])

# If an image is uploaded
if uploaded_image:
    img = Image.open(uploaded_image)
    st.image(img, caption="🖼 Uploaded Image", use_column_width=True)

    with st.spinner("🔍 Extracting text..."):
        text = pytesseract.image_to_string(img, config='--psm 6')
        st.subheader("📝 Extracted Math Problem")
        st.code(text)

