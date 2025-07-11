# London Bike Trips - ETL with Google Cloud

## Project Overview
This project demonstrates a complete ETL pipeline using:
- Cloud Storage for staging raw data
- Python for transformation
- BigQuery for querying & analysis

## Tools
- Google Cloud Storage
- Google BigQuery
- Python (pandas, google-cloud libraries)

## Steps
1. Export bike trip data to Cloud Storage
2. Transform data using pandas
3. Load clean data into BigQuery
4. Run analysis queries

## Sample Analysis
- Busiest pickup station: Waterloo Station
- Most trips happen on Fridays
...

## Run Locally
```bash
pip install -r requirements.txt
python upload_to_cloud.py
python transform_bike_data.py
python load_to_bigquery.py
