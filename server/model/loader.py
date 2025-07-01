import pandas as pd


class Loader:
    def __init__(self):
        """
        Initialize the Loader class.
        This class is responsible for loading datasets from a specified url.
        """
        pass

    def load(self, path, attributes):
        """Load the dataset from the specified url."""
        return pd.read_csv(path, usecols=attributes, header=0)
