import streamlit as st
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"  # For Streamlit Cloud

st.title("📷 Math Problem OCR")

# File uploader
uploaded_image = st.file_uploader("Upload an image of a math problem", type=["jpg", "jpeg", "png"])

# Camera input
camera_image = st.camera_input("Or take a picture")

# Use whichever image is provided
image = uploaded_image or camera_image

if image:
    img = Image.open(image)
    st.image(img, caption="🖼 Input Image", use_column_width=True)

    with st.spinner("🔍 Extracting text..."):
        text = pytesseract.image_to_string(img, config='--psm 6')
        st.subheader("📝 Extracted Math Problem")
        st.code(text)