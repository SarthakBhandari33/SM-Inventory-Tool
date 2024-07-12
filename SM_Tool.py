import streamlit as st
from streamlit_image_select import image_select

# Define the CSS for the background colors and borders of each layer
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f0f0f0;
}
.layer-red {
    background-color: #ffcccc;
    padding: 20px;
    margin-bottom: 30px;
    border-radius: 10px;
}
.layer-yellow {
    background-color: #ffffcc;
    padding: 20px;
    margin-bottom: 30px;
    border-radius: 10px;
}
.layer-green {
    background-color: #ccffcc;
    padding: 20px;
    margin-bottom: 30px;
    border-radius: 10px;
}
.image-container {
    display: flex;
    flex-wrap: wrap;
    gap: 40px;  /* Increased gap between images */
    justify-content: space-around;
}
img.layer-yellow-selected {
    border: 50px solid yellow;
}
img.layer-green-selected {
    border: 50px solid green;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Function to create image selection and buttons with border colors
def create_image_selection(images, captions, layer_name, border_class):
    selected_img = image_select(
        label=f"Select an image from {layer_name} layer",
        images=images,
        captions=captions,
        use_container_width=False
    )
    if selected_img:
        st.image(selected_img, width=300, caption=border_class, use_column_width=False)
        col1, col2 = st.columns(2)
        with col1:
            st.button(f"Forward to seller", key=f"{layer_name}_forward")
        with col2:
            st.button(f"Remove", key=f"{layer_name}_remove")

# Sample image URLs and captions
images = [
    'https://bijnis.s3.amazonaws.com/PRODUCTION/uploads/uploadfile_1-93eb6705-f4b2-49a0-b611-d6eea317b0b9.PNG',
    'https://bijnis.s3.amazonaws.com/PRODUCTION/uploads/uploadfile_1-ed183c0b-b00b-4bed-aa4d-5e80652083f7.jpeg',
    'https://bijnis.s3.amazonaws.com/PRODUCTION/uploads/uploadfile_1-cdd80568-6d42-499a-b4ba-085867bd393d.jpeg',
]
captions = ["Image1", "Image2", "Image3"]

st.title("The Tool")

# Red Layer
# st.markdown('<div class="layer-red">', unsafe_allow_html=True)
st.header("Out of Stock")
create_image_selection(images, captions, 'red', '')
st.markdown('</div>', unsafe_allow_html=True)

# Yellow Layer
# st.markdown('<div class="layer-yellow">', unsafe_allow_html=True)
st.header("Low Stock")
create_image_selection(images, captions, 'yellow', 'layer-yellow-selected')
st.markdown('</div>', unsafe_allow_html=True)

# Green Layer
# st.markdown('<div class="layer-green">', unsafe_allow_html=True)
st.header("In Stock")
create_image_selection(images, captions, 'green', 'layer-green-selected')
st.markdown('</div>', unsafe_allow_html=True)
