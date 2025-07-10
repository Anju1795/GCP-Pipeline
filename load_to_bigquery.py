from google.cloud import bigquery
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\anjuk\Downloads\turing-nimbus-465512-j6-36008886afa5.json"

def load_csv_to_bq(dataset_id, table_id, file_path):
    client = bigquery.Client()
    table_ref = client.dataset(dataset_id).table(table_id)

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
    )

    with open(file_path, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_ref, job_config=job_config)

    job.result()  # Wait for job to complete
    print("Loaded {} rows into {}:{}".format(job.output_rows, dataset_id, table_id))

# Example
load_csv_to_bq("bike_analysis", "bike_cleaned", r"C:\Users\anjuk\Desktop\Bigquery\bike_data_cleaned.csv")
