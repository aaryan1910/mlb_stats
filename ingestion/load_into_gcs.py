import os
from google.cloud import storage
from datetime import datetime
from fetch_batting import fetch_batting_stats
from fetch_batting_statcast import fetch_batting_statcast
from fetch_pitching import fetch_pitching_stats

BUCKET_NAME = "mlb-stats-raw"

def upload_to_gcs(df, filename):
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    
    csv_data = df.to_csv(index=False)
    
    blob = bucket.blob(f"raw/{filename}")
    blob.upload_from_string(csv_data, content_type="text/csv")
    
    print(f"Uploaded {filename} to gs://{BUCKET_NAME}/raw/{filename}")

def main():
    print("Starting GCS load...")
    
    batting = fetch_batting_stats()
    upload_to_gcs(batting, f"batting_{datetime.utcnow().strftime('%Y%m%d')}.csv")
    
    statcast = fetch_batting_statcast()
    upload_to_gcs(statcast, f"batting_statcast_{datetime.utcnow().strftime('%Y%m%d')}.csv")
    
    pitching = fetch_pitching_stats()
    upload_to_gcs(pitching, f"pitching_{datetime.utcnow().strftime('%Y%m%d')}.csv")
    
    print("All files uploaded to GCS!")

if __name__ == "__main__":
    main()