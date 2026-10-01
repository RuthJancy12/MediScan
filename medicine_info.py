import pandas as pd

DATA_PATH = "data/medicines.csv"

# Load dataset
df = pd.read_csv(DATA_PATH, sep="\t")


def search_medicine(medicine_name):
    result = df[
        df["product_name"].str.lower() == medicine_name.lower()
    ]

    if result.empty:
        return None

    return result.iloc[0]