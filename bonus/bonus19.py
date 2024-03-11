import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    #Start the camera
    camera_image = st.camera_input("Camera")
    uploaded_image = st.file_uploader("Upload Image")

if camera_image:
    # Create a óççpw o,age omstamce
    img = Image.open(camera_image)

    # Convert the pillow image to a grayscale
    gray_img = img.convert("L")

    # Render the grayscale image on the webpage
    st.image(gray_img)
