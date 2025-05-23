# Customer Segmentation Pipeline with Streamlit + Azure SQL

This project is a modular data pipeline built with **Python**, **Streamlit**, and **Azure SQL** to enable customer data preprocessing, clustering, normalization, and visualization in **Looker Studio**.

## 🚀 Features

- 📁 **Upload CSVs** for customer analysis
- 🧹 **Clean data** automatically (deduplication, imputation, age/children derivation)
- 🔍 **Cluster customers** using KMeans with silhouette score optimization
- 🧮 **Normalize & enrich data** for Looker-friendly dashboards
- ☁️ **Upload results to Azure SQL** and open a linked Looker dashboard

## 🧱 Modules Overview

| File                  | Description |
|-----------------------|-------------|
| `upload_page.py`      | Streamlit interface to upload CSVs |
| `cleaning_page.py`    | Cleans and standardizes uploaded data |
| `clustering_page.py`  | Clusters cleaned data and uploads to Azure SQL |
| `clustering.py`       | KMeans clustering logic with silhouette score selection |
| `normalize.py`        | Normalizes and enriches clustered data for BI usage |
| `preprocessing.py`    | Auto-cleans data (outlier trimming, null handling, age derivation) |
| `sql_upload.py`       | Securely uploads data to Azure SQL using SQLAlchemy |

## 📊 Data Flow

1. **Upload** → multiple `.csv` customer datasets
2. **Clean** → removes duplicates, fills nulls, derives fields
3. **Cluster** → groups customers with KMeans
4. **Normalize** → reshapes data for BI dashboards
5. **Upload** → Azure SQL for dashboard access

## 📈 Looker Studio Integration

After clustering, the app **automatically uploads to Azure SQL** and opens a **Looker dashboard**:

[Looker Dashboard](https://healthmobilesoftware.cloud.looker.com/dashboards/27)

## 🔧 Environment Variables

Set your Azure SQL credentials via a `.env` file:

```env
AZURE_SQL_SERVER=your_server.database.windows.net
AZURE_SQL_DATABASE=your_database
AZURE_SQL_USERNAME=your_user
AZURE_SQL_PASSWORD=your_password
```
## 🖥️ How to Run

1. **Clone the repo**

```bash
git clone https://github.com/bakralakhras/Capstone_2.git
cd Capstone_2
```
2. **Install dependencies**
```bash
pip install -r requirements.txt
```
3. **Run the app**
```bash
streamlit run upload_page.py
```

