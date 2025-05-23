# main.py

import streamlit as st
from frontend.upload_page import upload_page
from frontend.cleaning_page import cleaning_page
from frontend.clustering_page import clustering_page

PAGES = {
    "1. Upload": upload_page,
    "2. Clean":  cleaning_page,
    "3. Cluster": clustering_page,
}

st.sidebar.title("Navigation")
choice = st.sidebar.radio("Go to", list(PAGES.keys()))
PAGES[choice]()
