from pathlib import Path, PosixPath
from typing import Union
import pandas as pd
import customized_headlines.utils.paths as paths

# Inputs
data_raw = paths.data_raw_dir()
data_processed = paths.data_processed_dir()


# Outputs
news = paths.data_processed_dir("news.csv")
embeddings_t5 = paths.data_processed_dir("embeddings-t5.csv")
embeddings_ada = paths.data_processed_dir("embeddings-ada.csv")

