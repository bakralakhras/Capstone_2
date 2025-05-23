import streamlit as st
from backend.preprocessing import auto_clean

def cleaning_page():
    st.title("2. Clean Uploaded Data")

    if "uploaded_data" not in st.session_state:
        st.error("🚨 Please upload files first.")
        return

    uploaded_dict = st.session_state["uploaded_data"]

    if st.button("Run Cleaning on All Files"):
        cleaned_dict = {}
        for name, df in uploaded_dict.items():
            try:
                cleaned_df = auto_clean(df)
                cleaned_dict[name] = cleaned_df
                st.success(f"✅ {name}: Cleaned → {cleaned_df.shape[1]} columns")
            except Exception as e:
                st.error(f"❌ {name} failed: {e}")
        st.session_state["cleaned_data"] = cleaned_dict

    if "cleaned_data" in st.session_state:
        for name, df in st.session_state["cleaned_data"].items():
            st.markdown(f"**Cleaned Preview – {name}**")
            st.dataframe(df.head())
