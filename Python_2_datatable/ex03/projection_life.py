from load_csv import load
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.ticker import FuncFormatter


def format_income(value: float, position: int) -> str:
    """Format income values using the k suffix."""
    if value >= 1000:
        return f"{value / 1000:g}k"
    return f"{value:g}"


def main():
    """Displays the projection of life expectancy in relation to the gross
    national product of the year 1900 for each country in the dataset."""

    income_file = \
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    life_file = "life_expectancy_years.csv"
    income_path = Path(__file__).resolve().parent / income_file
    income = load(str(income_path))
    life_path = Path(__file__).resolve().parent / life_file
    life = load(str(life_path))

    if income is None or life is None:
        return
    try:
        income_1900 = income[["country", "1900"]]
        life_1900 = life[["country", "1900"]]
    except KeyError as exc:
        print(f"Error: missing required column: {exc}")
        return

    data = income_1900.merge(
        life_1900,
        on="country",
        suffixes=("_income", "_life"),
    )
    data = data.dropna()

    plt.title("1900", fontsize=18)
    plt.xlabel("Gross domestic product", fontsize=14)
    plt.ylabel("Life expectancy", fontsize=14)
    plt.tick_params(axis='both', labelsize=14)
    plt.xscale("log")
    plt.xlim(300, 10000)
    plt.xticks([300, 1000, 10000])
    plt.gca().xaxis.set_major_formatter(FuncFormatter(format_income))
    plt.scatter(
        data["1900_income"],
        data["1900_life"],
        label="Countries",
        s=80
    )
    plt.legend(loc="upper left", fontsize=12)
    plt.show()


if __name__ == "__main__":
    main()
