import pandas as pd


df = pd.read_csv("data_table.csv")
# print(f"Shape: {df.shape}")
# print(f"df.columns[1:]: \n {df.columns[1:].astype(int)} \n")

# print(f"df['country']: \n {df['country'].to_string(index=False)} \n")

# print(f"df['country'].iloc[0]: \n {df['country'].iloc[0]} \n")

# print(f"df.iloc[1]: \n {df.iloc[1]} \n")
# print(f"Dtypes:\n{df.dtypes}")
# print(f"First few rows:\n{df.head()}")

row = df[df["country"] == "Albania"]

# print(f"Rows for Albania:\n{row} \n")
print(f"row.columns[1:]: {type(row.columns[1:])} \n {row.columns[1:].astype(int)} \n")


print(f"row.iloc[0]: {type(row.iloc[0])} \n {row.iloc[0]} \n")

print(f"row.iloc[0, 1:]: {type(row.iloc[0, 1:])} \n {row.iloc[0, 1:]} \n")

print(f"row.iloc[0, 1:].values: {type(row.iloc[0, 1:].values)} \n {row.iloc[0, 1:].values} \n")


life_expectancy = row.iloc[0, 1:].values.astype(float)

print(f"row.iloc[0, 1:].values.astype(float): {type(life_expectancy)} \n {life_expectancy} \n")

#print(f"row.index: \n {row.index} \n")

# print(f"row.columns: \n {row.columns} \n")

# print(f"başlıksız: \n {df[df['country'] == 'Albania'].to_string(header=False)} \n")

# print(f"indexsiz: \n {df[df['country'] == 'Albania'].to_string(index=False)} \n")

# print(f"başlıksız ve indexsiz: \n {df[df['country'] == 'Albania'].to_string(index=False, header=False)} \n")


# print(f"Index’i sıfırlayıp daha temiz tablo: \n {df[df['country'] == 'Albania'].reset_index(drop=True)} \n")

# print(f"df[1800] :\n  {df['1800']}") 

# print(f"boolean series: \n {df[[True, False, True, False, True, False, False, False]]}")

# column = df["1805"]
# print(f"Values for 1805:\n{column}")
# cols = [col for col in df.columns if col.startswith("18")]
# print(f"Columns starting with '18': {cols}")
