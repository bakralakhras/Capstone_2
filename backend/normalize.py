import pandas as pd

def normalize_for_looker(df: pd.DataFrame, filename: str) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.lower()

    # ✅ Create customer_id if not present
    if "customer_id" not in df.columns:
        df["customer_id"] = df.index + 1

    # ✅ Add engineered fields without dropping anything

    # Total spending
    df["total_spent"] = df[[
        "mntwines", "mntfruits", "mntmeatproducts",
        "mntfishproducts", "mntsweetproducts", "mntgoldprods"
    ]].sum(axis=1)

    # Total accepted campaigns
    df["num_promos_accepted"] = df[[
        "acceptedcmp1", "acceptedcmp2", "acceptedcmp3",
        "acceptedcmp4", "acceptedcmp5"
    ]].sum(axis=1)

    # Children + parenthood
    if "children" not in df.columns:
        df["children"] = df["kidhome"] + df["teenhome"]

    df["is_parent"] = (df["children"] > 0).astype(int)

    # Living with
    df["living_with"] = df["marital_status"].replace({
        "married": "Partner", "together": "Partner",
        "single": "Alone", "divorced": "Alone",
        "widow": "Alone", "absurd": "Alone", "yolo": "Alone"
    }).fillna("Alone")

    # Family size
    df["family_size"] = df.apply(
        lambda row: (2 if row["living_with"] == "Partner" else 1) + row.get("children", 0),
        axis=1
    )

    # Age
    if "year_birth" in df.columns:
        df["age"] = pd.Timestamp.now().year - df["year_birth"]

    # Education level
    df["education_level"] = df["education"].replace({
        "basic": "Undergraduate", "2n cycle": "Undergraduate",
        "graduation": "Graduate", "master": "Postgraduate", "phd": "Postgraduate"
    })

    # ✅ UNPIVOT campaign columns
    campaign_cols = ["acceptedcmp1", "acceptedcmp2", "acceptedcmp3", "acceptedcmp4", "acceptedcmp5", "response"]

    campaign_long = df[["customer_id"] + campaign_cols].melt(
        id_vars=["customer_id"],
        value_vars=campaign_cols,
        var_name="campaign_name",
        value_name="accepted"
    )

    # ✅ Keep full original dataset
    other_cols = df.copy()

    # ✅ Merge unpivoted campaigns back
    final_df = campaign_long.merge(other_cols, on="customer_id")

    # ✅ Add filename
    final_df["source_file"] = filename

    return final_df
