def main():
    """
    Main function to run the model training process.
    """
    import os
    import joblib
    import pandas as pd
    import matplotlib.pyplot as plot

    # Load the model 
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # project root folder
    model_path = os.path.join(BASE_DIR, 'models', 'modelo_random_forest.pkl')
    modelo = joblib.load(model_path)

    data_path = os.path.join(BASE_DIR, 'data', 'preprocessed_data.parquet')
    df_data = pd.read_parquet(data_path)

    n_lags = 3  # Number of lags created
    # Split variables
    X_data = df_data[[f'lag_{i}' for i in range(1, n_lags + 1)]]
    y_data = df_data['price']

    # Make historical predictions
    y_pred = modelo.predict(X_data)

    # Historical plot
    plot.figure(figsize=(10, 5))
    plot.plot(y_data.values, label='Real values', marker='o')
    plot.plot(y_pred, label='Model Predictions', marker='x')
    plot.title('Actual vs predicted values - Full History')
    plot.xlabel('Index')
    plot.ylabel('Price')
    plot.legend()
    plot.grid(True)
    plot.tight_layout()

    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # project root folder
    img_path = os.path.join(BASE_DIR, 'img', 'history.jpg')
    plot.savefig(img_path,dpi=300, bbox_inches='tight') 

    # Recent plot
    plot.figure(figsize=(10, 5))
    plot.plot(y_data.tail(30).values, label='Real values', marker='o')
    plot.plot(modelo.predict(X_data.tail(30)), label='Model Predictions', marker='x')
    plot.title('Actual vs predicted values - Last 30 days')
    plot.xlabel('Index')
    plot.ylabel('Price')
    plot.legend()
    plot.grid(True)
    plot.tight_layout()
    img_path = os.path.join(BASE_DIR, 'img', 'recient.jpg')
    plot.savefig(img_path,dpi=300, bbox_inches='tight') 

    print("Graph Success !!")
