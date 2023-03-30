# Customized Headlines
A proof-of-concept to create customized headlines from news content based on demographic data.

### Data

News content data from a Mexican newsroom outlet from 10-01-22 to 03-01-23 and was collected with [MediaCloud](https://search.mediacloud.org/).


### Pre-processing

Data was cleanned with...

### Embeddings

Created by: Fer Aguirre

---
## Directory Structure
```
├── .gitignore
├── .gitsecret
│   ├── keys
│   │   ├── mapping.cfg
│   │   ├── pubring.kbx
│   │   ├── pubring.kbx~
│   │   └── trustdb.gpg
│   └── paths
│       └── mapping.cfg
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── assets
├── config.ini.secret
├── customized_headlines
│   ├── __init__.py
│   ├── data
│   │   ├── __init__.py
│   │   ├── analyze.py
│   │   ├── export.py
│   │   ├── load.py
│   │   └── process.py
│   └── utils
│       ├── __init__.py
│       └── paths.py
├── data
│   ├── processed
│   │   ├── embeddings-t5.csv
│   │   └── news.csv
│   └── raw
│       └── milenio.csv
├── docs
│   ├── data-dictionary.md
│   └── references
├── notebooks
│   ├── 0.0-process-data.ipynb
│   ├── 0.1-webscraping.ipynb
│   ├── 0.2-clean-text.ipynb
│   ├── 1.0-embeddings.ipynb
│   ├── 1.1-embeddings.ipynb
│   └── 1.1-semantic-search.ipynb
├── outputs
│   ├── figures
│   └── tables
├── scripts
│   ├── api.py
│   └── app.py
└── setup.py
```
---

## License

This project is released under [MIT License](/LICENSE).

---

This repository was generated with [cookiecutter](https://github.com/cookiecutter/cookiecutter).