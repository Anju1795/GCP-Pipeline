from google.cloud import storage
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\anjuk\Downloads\turing-nimbus-465512-j6-36008886afa5.json"

def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

# Sample call
if __name__ == "__main__":
    upload_to_gcs(
        bucket_name="bike_data_bucket",
        source_file_name=r"C:\Users\anjuk\Desktop\Bigquery\bike_data.csv",
        destination_blob_name="raw/bike_data.csv"
    )