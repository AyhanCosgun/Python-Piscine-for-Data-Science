from load_csv import load
import matplotlib.pyplot as plt
from pathlib import Path


def main():
    """Displays a graph of the life expectancy projections for Turkey."""
    data_path = Path(__file__).resolve().parent / "life_expectancy_years.csv"
    df = load(str(data_path))
    if df is None:
        return
    if "country" not in df.columns:
        print("Error: 'country' column not found in dataset.")
        return
    row = df[df["country"] == "Turkey"]
    if row.empty:
        print("Error: No data found for Turkey.")
        return
    years = row.columns[1:].astype(int)
    life_expectancy = row.iloc[0, 1:].values.astype(float)

    plt.title("Turkey Life expectancy Projections", fontsize=20)
    plt.xlabel("Year", fontsize=15)
    plt.ylabel("Life expectancy", fontsize=15)
    plt.tick_params(axis='both', labelsize=15)
    plt.plot(years, life_expectancy, lw=3)
    plt.show()


if __name__ == "__main__":
    main()
