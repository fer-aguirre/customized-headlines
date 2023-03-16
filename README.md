# Customized Headlines
Proof-of-concept to create customized headlines from news content based on demographic data.

Created by: Fer Aguirre

---
## Directory Structure
```
├── .gitignore
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── assets
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
│   │   ├── news_content.csv
│   │   └── news_sample.csv
│   └── raw
│       ├── arte.csv
│       ├── ciencia.csv
│       ├── cultura.csv
│       ├── deportes.csv
│       ├── entretenimeinto.csv
│       ├── medio_ambiente.csv
│       ├── negocios.csv
│       ├── politica.csv
│       ├── salud.csv
│       └── tecnologia.csv
├── docs
│   ├── data-dictionary.md
│   └── references
├── notebooks
│   ├── 0.0-process.ipynb
│   └── 1.0-webscraping.ipynb
├── outputs
│   ├── figures
│   └── tables
├── scripts
└── setup.py
```
---

## License

This project is released under [MIT License](/LICENSE).

---

This repository was generated with [cookiecutter](https://github.com/cookiecutter/cookiecutter).