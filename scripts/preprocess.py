def main():
    """
    Main function to run the preprocessing process.
    """
    import pandas as pd
    import os
    import numpy as np

    # Load the raw data from the Parquet file
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # project root folder
    data_path = os.path.join(BASE_DIR, 'data', 'raw_data.parquet')
    df_parquet = pd.read_parquet(data_path)

    # Perform preprocessing steps
    df_data = df_parquet.copy()

    # Create lagged variables (lags) 
    n_lags = 3  # Number of lags to create
    for i in range(1, n_lags + 1):
        df_data[f'lag_{i}'] = df_data['price'].shift(i)

    df_data.dropna(inplace=True)  # Drop rows with NaN
    
    preprocessed_path = os.path.join(BASE_DIR, 'data', 'preprocessed_data.parquet')
    df_data.to_parquet(preprocessed_path, index=False)

    print("Preprocess Success !!")


