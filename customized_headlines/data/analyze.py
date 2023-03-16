import pandas as pd
from typing import List


"""
Function to get a list
of column values
"""
def get_col_val(df: pd.DataFrame, column_name: str) -> List:
    return df[column_name].tolist()
