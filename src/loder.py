import os
import pandas as pd

DATA_FOLDER = "data"


def read_csv(file_name):
    """
    Generator to yield input examples from a CSV file
    """
    csv_path = os.path.join(DATA_FOLDER, file_name)
    return pd.read_csv(csv_path, engine="python")
