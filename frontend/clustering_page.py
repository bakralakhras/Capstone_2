import streamlit as st
from backend.clustering import cluster_data
from backend.sql_upload import upload_to_azure_sql
from backend.normalize import normalize_for_looker

def clustering_page():
    st.title("3. Run Clustering")

    if "cleaned_data" not in st.session_state:
        st.error("🚨 Run cleaning step first.")
        return

    cleaned_dict = st.session_state["cleaned_data"]


    if st.button("Cluster All Files"):
        clustered_dict = {}
        for name, df in cleaned_dict.items():
            try:
                clustered = cluster_data(df, n_clusters=2)
                clustered_dict[name] = clustered
                st.success(f"✅ Clustered: {name} → {clustered['cluster_label'].nunique()} clusters")
            except Exception as e:
                st.error(f"❌ Clustering failed for {name}: {e}")
        st.session_state["clustered_data"] = clustered_dict

    if "clustered_data" in st.session_state:
        for name, df in st.session_state["clustered_data"].items():
            st.markdown(f"**Clustered Preview – {name}**")
            st.dataframe(df.head())

    if st.button("Upload to Azure SQL + Auto Open Dashboard"):
        if "clustered_data" in st.session_state:
            for name, df in st.session_state["clustered_data"].items():
                try:
                    normalized_df = normalize_for_looker(df, filename=name)
                    upload_to_azure_sql(normalized_df, table_name="clustered_insights")
                    st.success(f"{name} uploaded to Azure SQL ✅")

                    # ✅ Immediately open Looker dashboard in new tab
                    dashboard_url = "https://healthmobilesoftware.cloud.looker.com/dashboards/27"
                    js = f"window.open('{dashboard_url}')"
                    html = f"<script>{js}</script>"
                    st.components.v1.html(html)

                except Exception as e:
                    st.error(f"❌ Upload failed for {name}: {e}")
