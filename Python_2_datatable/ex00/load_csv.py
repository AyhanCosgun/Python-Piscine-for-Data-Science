import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """Loads a dataset from the given path
    and returns it as a pandas DataFrame.
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except (FileNotFoundError, pd.errors.EmptyDataError,
            pd.errors.ParserError, UnicodeDecodeError, OSError) as exc:
        print(f"Error loading dataset: {exc}")
        return None
    except Exception as exc:
        print(f"Unexpected error loading dataset: {exc}")
        return None
