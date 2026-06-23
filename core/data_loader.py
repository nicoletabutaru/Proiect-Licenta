import pandas as pd
from core.config_loader import CONFIG


def load_data():


    csv_path = CONFIG["dataset"]["path"]
    df = pd.read_csv(csv_path)


    if "No-show" in df.columns and "Attended" not in df.columns:
        df["Attended"] = df["No-show"].apply(lambda x: 0 if x == "Yes" else 1)
       
    if "Age" in df.columns and "AgeGroup" not in df.columns:
        df["AgeGroup"] = pd.cut(
            df["Age"],
            bins=[0, 18, 35, 60, 120],
            labels=["Child", "Young Adult", "Adult", "Senior"]
        )


    return df
