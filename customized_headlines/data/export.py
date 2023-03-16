import pandas as pd
import pathlib
from typing import Union


"""
Function to save dataframe
as csv file
"""
def df_csv(df: pd.DataFrame, path: Union[pathlib.PosixPath, str]):
    return df.to_csv(path, index=False)