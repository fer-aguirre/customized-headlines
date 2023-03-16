from pathlib import Path, PosixPath
from typing import Union
import pandas as pd
import customized_headlines.utils.paths as paths

# Inputs
data_raw = paths.data_raw_dir()
data_processed = paths.data_processed_dir()


# Outputs
news_sample = paths.data_processed_dir('news_sample.csv')


"""
Function to get csv files
from the path provided
"""
def get_csv_dir(dir: Union[PosixPath, str]):
    # Get the csv files from the path provided
    return Path(dir).glob('*.csv')


"""
Function to read csv 
file a dataframe
"""
def read_csv(file_name: Union[PosixPath, str]):
    return pd.read_csv(file_name)