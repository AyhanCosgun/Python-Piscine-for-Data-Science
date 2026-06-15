from load_csv import load
import matplotlib.pyplot as plt


def main():
	"""Displays a graph of the life expectancy projections for Turkey."""
	df = load("life_expectancy_years.csv")
	if df is None:
		return
	row = df[df["country"] == "Turkey"]
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
