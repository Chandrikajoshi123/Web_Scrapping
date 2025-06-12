import streamlit as st
import requests
import os
from PIL import Image

st.set_page_config(page_title="Pinterest-Inspired Image Board", layout="wide")

# Header
st.markdown(
    """
    <h1 style='text-align: center; color: #BD081C;'>📌 Pinterest Style Image Board</h1>
    <p style='text-align: center;'>Welcome to <strong>Image Scrappy</strong> – My love for Pinterest turned into code ❤️</p>
    """,
    unsafe_allow_html=True
)
# --- Search Box

# # Dummy image source (Unsplash random images for demo)
# def get_images():
#     urls = [
#         "-8.jpg",
#         "https://source.unsplash.com/600x800/?art",
#         "https://source.unsplash.com/600x800/?interior",
#         "https://source.unsplash.com/600x800/?travel",
#         "https://source.unsplash.com/600x800/?nature",
#         "https://source.unsplash.com/600x800/?makeup",
#         "https://source.unsplash.com/600x800/?design",
#         "https://source.unsplash.com/600x800/?food",
#     ]
#     return urls * 3  # repeat to fill grid

# # --- Path to images
# image_folder = "Images"
# image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

# # --- Sort for consistent display
# image_files.sort()

# # --- Show in grid
# cols = st.columns(4)

# for i, img_file in enumerate(image_files):
#     img_path = os.path.join(image_folder, img_file)
#     with cols[i % 4]:
#         try:
#             image = Image.open(img_path)
#             st.image(image, caption=img_file, use_container_width=True)
#         except Exception as e:
#             st.error(f"❌ Error loading {img_file}: {e}")
# # Grid Layout
# cols = st.columns(4)
# images = Image.open(img_path)
# for i, img in enumerate(images):
#     with cols[i % 4]:
#         st.image(img, use_column_width=True)
# Define local folder
image_folder = "Images"  # Make sure this folder exists and has .jpg/.png images

# Read and sort local image files
image_files = sorted([
    f for f in os.listdir(image_folder)
    if f.lower().endswith(('.jpg', '.jpeg', '.png'))
])

# Search box
search = st.text_input("🔍 ")

# Filter images if keyword is entered
if search:
    image_files = [f for f in image_files if search.lower() in f.lower()]

# Display images in 4-column grid
cols = st.columns(4)
for i, img_file in enumerate(image_files):
    img_path = os.path.join(image_folder, img_file)
    try:
        image = Image.open(img_path)
        with cols[i % 4]:
            st.image(image, caption=img_file, use_container_width=True)
    except Exception as e:
        st.error(f"Error showing {img_file}: {e}")