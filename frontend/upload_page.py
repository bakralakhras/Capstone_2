import streamlit as st
import pandas as pd

def upload_page():
    st.title("1. Upload CSV Files")
    st.markdown("Upload one or more customer-related CSV files to begin.")

    uploaded_files = st.file_uploader(
        label="Upload CSV files",
        type=["csv"],
        accept_multiple_files=True
    )

    if uploaded_files:
        uploaded_data = {}
        for file in uploaded_files:
            try:
                df = pd.read_csv(file)
                uploaded_data[file.name] = df
                st.success(f"✅ {file.name} loaded successfully.")
                st.dataframe(df.head())
            except Exception as e:
                st.error(f"❌ Failed to read {file.name}: {e}")

        st.session_state["uploaded_data"] = uploaded_data

    if st.button("Continue"):
        if "uploaded_data" in st.session_state:
            st.session_state["form_submitted"] = True
            st.session_state["selected_demo"] = "2. Clean"
            st.success("✅ Files ready. Move to Step 2.")
        else:
            st.error("Please upload at least one CSV file first.")
