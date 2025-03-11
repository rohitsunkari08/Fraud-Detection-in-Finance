from sklearn.tree import DecisionTreeClassifier

def classify_transactions(data):
    """Classify transactions using Decision Tree."""
    classifier = DecisionTreeClassifier(random_state=42)
    classifier.fit(data[['transaction_amount', 'transaction_type']], data['fraud_label'])
    data['predicted_label'] = classifier.predict(data[['transaction_amount', 'transaction_type']])
    return data
