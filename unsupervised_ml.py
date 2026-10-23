import matplotlib.pyplot as plt
from collections import Counter
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
customer_data = [[1000, 2],[1500, 3],[2000, 2],[5000, 6],[6000, 7],[5500, 5],[12000, 12],[15000, 14],[13000,11],[3000, 4]]
scaler = StandardScaler()
scaled_data = scaler.fit_transform(customer_data)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(scaled_data)
labels = kmeans.labels_
print("--- Customer Cluster Assignments ---")
for i, label in enumerate(labels):
    print(f"Customer {i+1} belongs to Cluster {label}")
print("\n--- Cluster Summary Counts ---")
counts = Counter(labels)
for cluster, count in sorted(counts.items()):
    print(f"Cluster {cluster}: {count} customers")
    spending = [row[0] for row in customer_data]
visits = [row[1] for row in customer_data]

plt.figure(figsize=(8, 6))
scatter = plt.scatter(spending, visits, c=labels, cmap='viridis', s=100, edgecolors='black')
plt.title('Supermarket Customer Segmentation (K-Means)', fontsize=14, pad=15)
plt.xlabel('Monthly Spending (KES)', fontsize=12)
plt.ylabel('Monthly Visits', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
legend = plt.legend(*scatter.legend_elements(), title="Clusters", loc="upper left")
plt.gca().add_artist(legend)
plt.show()