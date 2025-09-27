import pandas as pd
from pathlib import Path

def load_csv(path, **kwargs):
    """Load a CSV into a DataFrame with sensible defaults.

Parameters
----------
path : str or Path
    Path to CSV file.
**kwargs : dict
    Passed to pandas.read_csv.

Returns
-------
pandas.DataFrame
"""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"CSV not found: {path}")
    return pd.read_csv(path, low_memory=False, **kwargs)
