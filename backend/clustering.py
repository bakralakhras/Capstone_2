import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def cluster_data(df: pd.DataFrame, n_clusters: int = None) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.lower()

    feature_cols = [
        "age", "income", "children", "recency",
        "mntwines", "mntfruits", "mntmeatproducts", "mntfishproducts",
        "mntsweetproducts", "mntgoldprods",
        "numdealspurchases", "numwebpurchases", "numcatalogpurchases",
        "numstorepurchases", "numwebvisitsmonth"
    ]
    X = df[feature_cols].copy()

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    if n_clusters is None:
        best_k, best_score = 2, -1
        for k in range(2, 9):
            model = KMeans(n_clusters=k, random_state=42, n_init=10)
            labels = model.fit_predict(X_scaled)
            score = silhouette_score(X_scaled, labels)
            if score > best_score:
                best_k, best_score = k, score
        n_clusters = best_k

    model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df["cluster_label"] = model.fit_predict(X_scaled)
    df["auto_k_used"] = n_clusters

    return df
