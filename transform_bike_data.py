import pandas as pd

def transform_data():
    # Read local or downloaded CSV
    df = pd.read_csv(r"C:\Users\anjuk\Desktop\Bigquery\bike_data.csv")
    
    print('Before transformation')
    print(df)
    # Basic transformation
    df['duration_min'] = df['duration'] / 60
    df['start_time'] = pd.to_datetime(df['start_date'])
    df['end_time'] = pd.to_datetime(df['end_date'])
    df['day_of_week'] = df['start_time'].dt.day_name()
    df.dropna()
    # filter out long trips
    df = df[df['duration_min'] < 120]
    
    print('After transformation')
    print(df)
    # Save cleaned file
    df.to_csv(r"C:\Users\anjuk\Desktop\Bigquery\bike_data_cleaned.csv", index=False)
