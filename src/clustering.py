from sklearn.cluster import KMeans

def perform_clustering(data):
    """Cluster transactions using KMeans."""
    kmeans = KMeans(n_clusters=2, random_state=42)
    data['cluster'] = kmeans.fit_predict(data[['transaction_amount']])
    return data
