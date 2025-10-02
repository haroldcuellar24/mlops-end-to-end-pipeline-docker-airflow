def main():
    """
    Main function to run the model training process
    """
    import os 
    import pandas as pd
    from sklearn.ensemble import RandomForestRegressor
    import joblib

    # Load the raw data from the Parquet file
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # project root folder
    data_path = os.path.join(BASE_DIR, 'data', 'preprocessed_data.parquet')
    df_processed = pd.read_parquet(data_path)
    
    n_lags = 3 # Number of lags created

    # Split variables
    X = df_processed[[f'lag_{i}' for i in range(1, n_lags + 1)]]
    y = df_processed['price']

    # Train model
    modelo = RandomForestRegressor(n_estimators=100, random_state=42)
    modelo.fit(X, y)

    # Save the trained model
    model_path = os.path.join(BASE_DIR, 'models', 'modelo_random_forest.pkl')
    joblib.dump(modelo, model_path)
    print("Model trained and saved successfully !!")


