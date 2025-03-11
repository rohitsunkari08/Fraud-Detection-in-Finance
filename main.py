from src.utils import load_data, preprocess_data
from src.anomaly_detection import detect_anomalies
from src.clustering import perform_clustering
from src.classification import classify_transactions

def main():
    # Load and preprocess data
    filepath = 'data/transactions.csv'
    data = load_data(filepath)
    data = preprocess_data(data)
    
    # Step 1: Anomaly Detection
    print("Running anomaly detection...")
    data = detect_anomalies(data)
    
    # Step 2: Clustering
    print("Running clustering...")
    data = perform_clustering(data)
    
    # Step 3: Classification
    print("Running classification...")
    data = classify_transactions(data)

    print("\nFinal Processed Data:")
    print(data)

if __name__ == "__main__":
    main()
