import pandas as pd
import numpy as np
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from typing import List


"""
Function to get a list
of column values
"""
def get_col_val(df: pd.DataFrame, column_name: str) -> List:
    return df[column_name].tolist()


"""
Function to make a http request 
and parse html content
"""
def make_request(url: str) -> BeautifulSoup:
    # Make a http request to the specified url
    response = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    # Read content from request
    html = urlopen(response).read()
    # Return content of the response
    return BeautifulSoup(html, "html.parser")


"""
Function to parse text 
from BeautifulSoup object
"""
def extract_text(soup: BeautifulSoup) -> str:
    try:
        for data in soup(["style", "script"]):
            # Remove tags
            data.decompose()
        text = " ".join(soup.stripped_strings)
    except Exception:
        text = np.nan
    # Return data by retrieving the tag content
    return text
