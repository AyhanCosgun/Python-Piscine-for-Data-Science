import pandas as pd


df = pd.read_csv("data_table.csv")
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Dtypes:\n{df.dtypes}")
print(f"First few rows:\n{df.head()}")
row = df[df["country"] == "Albania"]
print(f"Rows for Albania:\n{row}")
column = df["1805"]
print(f"Values for 1805:\n{column}")
cols = [col for col in df.columns if col.startswith("18")]
print(f"Columns starting with '18': {cols}")
