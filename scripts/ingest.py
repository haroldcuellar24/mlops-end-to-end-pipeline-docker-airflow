def main():
    """
    Main function to run the ingestion process.
    """
    import requests
    import json
    import pandas as pd
    from datetime import date
    import pyarrow
    import os

    # Define the API parameters
    api_url = os.getenv('API_URL')
    api_key = os.getenv('API_KEY')
    api_interval = "1day"
    api_start_date = "2021-01-01"
    api_end_date = date.today().isoformat()
    api_symbol = "XAU/USD"
    api_format = "json"

    # Construct the API URL with parameters
    api_url_parameter = f"{api_url}apikey={api_key}&interval={api_interval}&start_date={api_start_date}&end_date={api_end_date}&symbol={api_symbol}&format={api_format}"

    # Make the API request
    response = requests.get(api_url_parameter)

    dara_source = json.loads(response.text)
    data_raw = dara_source['values']

    df_normalize = pd.json_normalize(data_raw)

    selected_columns = ['datetime','close']
    df_price= df_normalize[selected_columns].copy()

    df_price["datetime"] = pd.to_datetime(df_price["datetime"])
    df_price["close"]  = df_price["close"].astype(float)
    df_price["close"] = df_price["close"].round(2)
    df_price = df_price.rename(columns={"datetime": "date", "close": "price"})
    df_price = df_price.set_index("date")
    df_price = df_price.sort_index(ascending=True)
    df_price = df_price.reset_index()
    
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # project root folder
    data_path = os.path.join(BASE_DIR, 'data', 'raw_data.parquet')
    
    # Save the DataFrame to a Parquet file
    df_price.to_parquet(data_path, index=False)
    print("Ingest Success !!")
