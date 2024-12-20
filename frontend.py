import streamlit as st
import requests
from PIL import Image
import io

# FastAPI backend endpoint URL
FASTAPI_URL = "http://localhost:8000/segment/"

# Set up Streamlit page configuration
st.set_page_config(page_title="Moon Image Segmentation", page_icon="🌕", layout="wide")

# Background CSS for adding a background image
background_image_url = "https://cdn.mos.cms.futurecdn.net/E79btr66HQWP22EybDE7LZ.jpg"  # Replace with your image URL or local path

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<h1 style="color: lightgray; text-align: center;">🌙 Lunar Terrain Segmentation App</h1>', unsafe_allow_html=True)

# Initialize session state for storing images
if 'segmented_image' not in st.session_state:
    st.session_state['segmented_image'] = None
if 'uploaded_file' not in st.session_state:
    st.session_state['uploaded_file'] = None

# Display the "Upload an Image" button and image uploader when clicked
uploaded_file = st.file_uploader("Upload an image of the moon's surface", type=["jpg", "jpeg", "png", "bmp"])

if uploaded_file is not None:
    # Save the uploaded image in session state
    st.session_state['uploaded_file'] = uploaded_file

    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    # Display the "Segment Image" button after the image is uploaded
    segment_button = st.button("Segment Image")

    # When the segment button is clicked, call the FastAPI backend for segmentation
    if segment_button:
        # Send the uploaded image to the FastAPI backend for segmentation
        try:
            # Convert the uploaded image to bytes
            files = {'file': uploaded_file.getvalue()}
            st.write("Segmenting....")
            response = requests.post(FASTAPI_URL, files=files)

            st.write("Tried my best :')")

            # Check if the request was successful
            if response.status_code == 200:
                # Convert the segmented image from the response
                segmented_image = Image.open(io.BytesIO(response.content))
                st.session_state['segmented_image'] = segmented_image  # Store the segmented image in session state
            else:
                st.error("Error in segmentation: " + response.json().get("detail", "Unknown error"))
        except requests.exceptions.RequestException as e:
            st.error(f"Error during request: {e}")

# Display the segmented image if available
if st.session_state['segmented_image'] is not None:
    st.image(st.session_state['segmented_image'], caption="Segmented Image", use_container_width=True)

# Add a footer to the page
footer = """
<div style='position: fixed; left: 0; bottom: 0; width: 100%; background-color: white; text-align: center; padding: 10px;'>
    <p style='color: black; margin: 0;'>This project is developed by <b>Pavankumar Megeri</b> as part of the <b>Machine Learning for Astronomy</b> Training Program by Spartifical</p>
</div>
"""

# Inject the footer using markdown
st.markdown(footer, unsafe_allow_html=True)
