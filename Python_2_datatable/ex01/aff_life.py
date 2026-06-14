from load_csv import load
import matplotlib.pyplot as plt


def main():
	df = load("life_expectancy.csv")
	if df is None:
		return
	row = df[df["country"] == "Turkey"]
	plt.title("Turkey Life expectancy Projections")
	plt.xlabel("Year")
	plt.ylabel("Life expectancy")
	plt.plot(row.columns[1:])
	plt.show()


if __name__ == "__main__":
	main()
