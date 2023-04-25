scrape-data:
	minet fetch url -i ./data/processed/milenio_urls.csv > ./data/processed/report_milenio.csv
	minet extract -i ./data/processed/report_milenio.csv -I downloaded > ./data/processed/extracted_milenio.csv 
	minet fetch url ./data/processed/unam_urls.csv > ./data/processed/report_unam.csv 
	minet extract ./data/processed/report_unam.csv > ./data/processed/extracted_unam.csv