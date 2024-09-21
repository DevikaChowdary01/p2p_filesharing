import streamlit as st
import os

# Directory to save uploaded files
UPLOAD_FOLDER = 'uploaded_files'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Global variable to hold the set password
password = None

# Function to upload files
def upload_file(uploaded_file):
    # Create a secure filename
    filename = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    # Write the uploaded file to the upload folder
    with open(filename, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return filename

# Function to list files in upload folder
def list_files():
    return os.listdir(UPLOAD_FOLDER)

# Streamlit app
st.title("P2P File Sharing App")

# Set password for downloads
if 'password' not in st.session_state:
    st.session_state['password'] = ''

# Input for setting the password
set_password = st.text_input("Set Password for Downloads", type="password", key="set_password")
if st.button("Set Password"):
    st.session_state['password'] = set_password
    st.success("Password set successfully!")

# Upload file section
uploaded_file = st.file_uploader("Upload Files", type=['pdf', 'docx', 'jpg', 'jpeg', 'png'])
if uploaded_file is not None:
    upload_file(uploaded_file)
    st.success(f"{uploaded_file.name} uploaded successfully!")

# Input for downloading files
st.subheader("Download Files")
input_password = st.text_input("Enter Password to Download", type="password")
if st.button("Show Download Links"):
    if input_password == st.session_state['password']:
        st.success("Correct Password! Here are your files:")
        for file in list_files():
            download_link = f'<a href="{UPLOAD_FOLDER}/{file}" download>{file}</a>'
            st.markdown(download_link, unsafe_allow_html=True)
    else:
        st.error("Incorrect Password.")
