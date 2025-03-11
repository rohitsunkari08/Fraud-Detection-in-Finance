# Fraud Detection in Finance

This project implements a fraud detection system in finance using machine learning techniques such as anomaly detection, clustering, and classification algorithms. The goal is to sift through massive transaction datasets to spot unusual patterns indicative of fraud or market manipulation.

## Project Overview
Fraud detection is critical in the finance industry to ensure the safety of transactions and prevent financial losses. This project focuses on:
- **Anomaly Detection**: Identifying outliers in transaction data using Isolation Forest.
- **Clustering**: Grouping transactions based on similarity using KMeans clustering.
- **Classification**: Predicting fraudulent transactions using Decision Tree Classifier.

## Features
1. Detect anomalies in transaction datasets.
2. Cluster transactions to identify patterns and trends.
3. Classify transactions as fraudulent or non-fraudulent.

## Technologies Used
- **Python**: Programming language for implementation.
- **Libraries**:
  - `pandas` for data manipulation.
  - `scikit-learn` for machine learning algorithms.
  - `matplotlib` and `seaborn` for data visualization (EDA).
- **Dataset**: A sample dataset representing financial transactions with features like transaction amount, type, customer ID, timestamp, and fraud labels.

## Project Structure
fraud-detection-system/
│
├── data/
│ ├── transactions.csv # Dataset for transactions
│
├── src/
│ ├── anomaly_detection.py # Isolation Forest implementation
│ ├── clustering.py # KMeans clustering implementation
│ ├── classification.py # Decision Tree classification implementation
│ ├── utils.py # Utility functions (e.g., data loading, preprocessing)
│
├── notebooks/
│ ├── exploratory_analysis.ipynb # Jupyter notebook for EDA
│
├── README.md # Project documentation
├── requirements.txt # Python dependencies
└── main.py # Main script to run the system

## How to Run the Project
1. Clone the repository:

git clone https://github.com/rohitsunkari08/Fraud-Detection-in-Finance
cd fraud-detection-system/

2. Install dependencies:

pip install -r requirements.txt

3. Run the main script:

python main.py

4. (Optional) Open the Jupyter notebook for exploratory analysis:

jupyter notebook notebooks/exploratory_analysis.ipynb

## Algorithms Used
1. **Isolation Forest**: Detects anomalies by isolating outlier points in the dataset.
2. **KMeans Clustering**: Groups similar transactions into clusters to identify patterns.
3. **Decision Tree Classifier**: Classifies transactions as fraudulent or non-fraudulent based on labeled data.

## Results and Insights
The system processes transaction datasets and outputs predictions for fraud detection:
- Anomalies are flagged using Isolation Forest.
- Transactions are grouped into clusters using KMeans clustering.
- Fraudulent transactions are identified using Decision Tree classification.

## Future Enhancements
1. Integration with an online database for real-time fraud detection.
2. Use advanced algorithms like Gradient Boosting Machines or Autoencoders.
3. Implement real-time monitoring with stream processing frameworks like Apache Kafka.

---
