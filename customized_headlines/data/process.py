from typing import List, Generator
import pandas as pd


"""
Function to read a list of path 
files as a dataframe and add a new 
column with the file name
"""
dfs = []


def files_to_df(files: Generator) -> List:
    for f in files:
        data = pd.read_csv(f)
        # .stem is method for pathlib objects to get the filename w/o the extension
        data["category"] = f.stem
        dfs.append(data)
    return dfs


"""
Function to concatenate
a list of dataframes
"""


def concat_dfs(dfs: List) -> pd.DataFrame:
    return pd.concat(dfs, ignore_index=True)