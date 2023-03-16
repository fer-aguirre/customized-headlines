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
        data['category'] = f.stem
        dfs.append(data)
    return dfs


"""
Function to concatenate
a list of dataframes
"""
def concat_dfs(dfs: List) -> pd.DataFrame:
    return pd.concat(dfs, ignore_index=True)


"""
Function to get a sample
from a dataframe
"""
def get_sample(df: pd.DataFrame, n: int) -> pd.DataFrame:
    return df.sample(n=n, replace=True)


"""
Function to get unique values from 
a column, get a sample of 20 from each 
one and return a list of dataframes
"""
dfs_sam = []
def get_col_sample(df: pd.DataFrame) -> List:
    categories = df['category'].unique().tolist()
    for i in range(len(categories)):
        df_cat = df[df['category'] == categories[i]]
        sample = get_sample(df_cat, 20)
        dfs_sam.append(sample)
    return dfs_sam

