import pandas as pd

def load_data(filepath):
    """Load dataset from a CSV file."""
    return pd.read_csv(filepath)

def preprocess_data(data):
    """Preprocess data (e.g., encode categorical variables)."""
    data['transaction_type'] = data['transaction_type'].astype('category').cat.codes
    return data
