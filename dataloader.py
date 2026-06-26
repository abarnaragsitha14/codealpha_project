import pandas as pd

def load_data():
    df = pd.read_csv("sales_data.csv")
    return df

def dataset_info(df):
    print("First 5 Rows:")
    print(df.head())

    print("\nDataset Information:")
    print(df.info())

    print("\nStatistical Summary:")
    print(df.describe())

    print("\nMissing Values:")
    print(df.isnull().sum())