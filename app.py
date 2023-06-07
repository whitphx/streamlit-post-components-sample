import streamlit as st


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write(uploaded_file.name)
    bytes_data = uploaded_file.getvalue()
    st.write(len(bytes_data))


picture = st.camera_input("Take a picture")
if picture:
    st.image(picture)
