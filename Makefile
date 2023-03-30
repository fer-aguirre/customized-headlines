scrape-data:
	minet fetch url -i ./data/processed/milenio_urls.csv > ./data/processed/report.csv
	minet extract -i ./data/processed/report.csv -I downloaded > ./data/processed/extracted.csv 
