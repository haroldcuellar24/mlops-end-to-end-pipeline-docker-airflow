def main():
    """
    Main function to run the model training process.
    """
    import os
    import joblib
    import pandas as pd
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

    # Load the model 
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # project root folder
    model_path = os.path.join(BASE_DIR, 'models', 'modelo_random_forest.pkl')
    modelo = joblib.load(model_path)

    data_path = os.path.join(BASE_DIR, 'data', 'preprocessed_data.parquet')
    df_test = pd.read_parquet(data_path)

    n_lags = 3  # Number of lags created
    # Split variables
    X_test = df_test[[f'lag_{i}' for i in range(1, n_lags + 1)]]
    y_test = df_test['price']

    # Make predictions
    y_pred = modelo.predict(X_test)

    # Calculate evaluation metrics
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Evaluation Success !!")

