import pandas as pd

def auto_clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.lower()

    df.drop_duplicates(inplace=True)

    if "income" in df.columns:
        df = df[df["income"] < df["income"].quantile(0.99)]
        df["income"].fillna(df["income"].median(), inplace=True)

    if "year_birth" in df.columns:
        df["age"] = pd.Timestamp.now().year - df["year_birth"]
        df.drop(columns=["year_birth"], inplace=True)

    if "kidhome" in df.columns and "teenhome" in df.columns:
        df["children"] = df["kidhome"] + df["teenhome"]
        df.drop(columns=["kidhome", "teenhome"], inplace=True)

    return df
