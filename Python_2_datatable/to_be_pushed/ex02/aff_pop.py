from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from pathlib import Path


def format_pop(x: float, pos: int) -> str:
    """Formats given population number to a version with appropriate suffix."""
    if x >= 1e12:
        return f"{x/1e12:.0f}T"
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
    try:
        return float(entry)
    except (ValueError, TypeError):
        pass
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
        "k": 1e3,
        "K": 1e3,
        "m": 1e6,
        "M": 1e6,
        "b": 1e9,
        "B": 1e9,
        "t": 1e12,
        "T": 1e12,
    }

    return number * multipliers[suffix]


def main():
    """Displays a graph of the population projections for Turkey vs France
    between 1800 and 2050."""
    data_path = Path(__file__).resolve().parent / "population_total.csv"
    df = load(str(data_path))
    if df is None:
        return
    if "country" not in df.columns:
        print("Error: 'country' column not found in dataset.")
        return
    row_turkey = df[df["country"] == "Turkey"]
    row_france = df[df["country"] == "France"]
    if row_turkey.empty or row_france.empty:
        print("Error: No data found for Turkey or France.")
        return
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
