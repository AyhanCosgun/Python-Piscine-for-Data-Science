from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def format_pop(x: float, pos: int) -> str:
    if x >= 1e9:
        return f"{x/1e9:.0f}B"
    if x >= 1e6:
        return f"{x/1e6:.0f}M"
    if x >= 1e3:
        return f"{x/1e3:.0f}K"
    return str(int(x))


def convert_to_float(entry: str) -> float:
    """Converts a string representing a number
    with an optional suffix to a float.
    """
    if not entry or not entry.strip():
        return float('nan')

    s = entry.strip()
    if s[-1] in "kKmMbBtT":
        try:
            number = float(s[:-1])
        except ValueError:
            return float('nan')
        suffix = s[-1]
    else:
        try:
            number = float(s)
        except ValueError:
            return float('nan')
        suffix = ""

    multipliers = {
        "": 1,
        "k": 1000,
        "K": 1000,
        "m": 1000000,
        "M": 1000000,
        "b": 1000000000,
        "B": 1000000000,
        "t": 1000000000000,
        "T": 1000000000000,
    }

    return number * multipliers[suffix]


def main():
    """Displays a graph of the population projections for Turkey vs France
    between 1800 and 2050."""
    df = load("population_total.csv")
    if df is None:
        return
    row_turkey = df[df["country"] == "Turkey"]
    row_france = df[df["country"] == "France"]
    years = row_turkey.columns[1:].astype(int)
    mask = (years >= 1800) & (years <= 2050)
    years = years[mask]
    
    population_turkey = row_turkey.iloc[0, 1:][mask].map(convert_to_float) \
        .values.astype(float)
    population_france = row_france.iloc[0, 1:][mask].map(convert_to_float) \
        .values.astype(float)

    plt.title("Population Projections", fontsize=20)
    plt.xlabel("Year", fontsize=15)
    plt.ylabel("Population", fontsize=15)
    plt.tick_params(axis='both', labelsize=15)
    plt.plot(years, population_turkey, lw=3, label="Turkey")
    plt.plot(years, population_france, lw=3, label="France")
    plt.legend(fontsize=15)
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_pop))
    plt.show()


if __name__ == "__main__":
    main()
