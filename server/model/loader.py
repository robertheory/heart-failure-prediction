import pandas as pd


class Loader:
    def __init__(self):
        """
        Initialize the Loader class.
        This class is responsible for loading datasets from a specified url.
        """
        pass

    def load(self, url: str, attributes: list) -> pd.DataFrame:
        """Load the dataset from the specified url."""
        try:
            df = pd.read_csv(url, usecols=attributes)
            return df
        except FileNotFoundError:
            raise FileNotFoundError(
                f"File not found at {url}. Please check the url.")
        except pd.errors.EmptyDataError:
            raise ValueError("No data found in the file.")
        except Exception as e:
            raise RuntimeError(
                f"An error occurred while loading the data: {e}")
