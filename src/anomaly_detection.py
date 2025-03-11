from sklearn.ensemble import IsolationForest

def detect_anomalies(data):
    """Detect anomalies using Isolation Forest."""
    iso_forest = IsolationForest(contamination=0.1, random_state=42)
    data['anomaly_score'] = iso_forest.fit_predict(data[['transaction_amount']])
    return data
