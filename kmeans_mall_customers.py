# --------------------------------------------
# Mall Customer Segmentation using K-Means
# --------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# -----------------------------
# 1. Load Dataset
# -----------------------------
data = pd.read_csv("Mall_Customers.csv")

print("Dataset Preview:")
print(data.head())

# -----------------------------
# 2. Select Features
# -----------------------------
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# -----------------------------
# 3. Feature Scaling
# -----------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -----------------------------
# 4. Elbow Method
# -----------------------------
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss)
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.savefig("elbow_method.png")
plt.show()

# -----------------------------
# 5. Apply K-Means (k = 5)
# -----------------------------
kmeans = KMeans(n_clusters=5, random_state=42)
data['Cluster'] = kmeans.fit_predict(X_scaled)

# -----------------------------
# 6. Add Cluster Names
# -----------------------------
cluster_labels = {
    0: "VIP Customers",
    1: "Low Priority Customers",
    2: "Regular Customers",
    3: "Impulse Buyers",
    4: "Careful Premium Customers"
}

data['Cluster_Type'] = data['Cluster'].map(cluster_labels)

# -----------------------------
# 7. Visualize Clusters
# -----------------------------
plt.figure(figsize=(8, 6))
plt.scatter(
    X.iloc[:, 0],
    X.iloc[:, 1],
    c=data['Cluster'],
    cmap='viridis'
)

plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    s=200
)

plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("Customer Segmentation using K-Means")
plt.savefig("customer_clusters.png")
plt.show()

# -----------------------------
# 8. Cluster Summary
# -----------------------------
print("\nCluster-wise Summary:")
print(
    data.groupby('Cluster_Type')[
        ['Annual Income (k$)', 'Spending Score (1-100)']
    ].mean()
)

# -----------------------------
# 9. Save Clustered Dataset
# -----------------------------
data.to_csv("Clustered_Mall_Customers.csv", index=False)
print("\nClustered dataset saved as Clustered_Mall_Customers.csv")
