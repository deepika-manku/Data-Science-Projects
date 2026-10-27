import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load dataset
df = pd.read_csv("marketing_campaign.csv", sep="\t")

# Select features
features = ["Income", "MntWines", "MntFruits",
"MntMeatProducts", "MntFishProducts",
"MntSweetProducts", "MntGoldProds"]

# Preprocessing
data = df[features].copy()
data = data.fillna(data.median())
data = data.clip(data.quantile(0.01),
                 data.quantile(0.99), axis=1)

# Standardization
scaler = StandardScaler()
X = scaler.fit_transform(data)

# Find suitable clusters
inertias, scores = [], []

for k in range(2, 8):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = model.fit_predict(X)
    inertias.append(model.inertia_)
    scores.append(silhouette_score(X, labels))

plt.plot(range(2, 8), inertias, marker="o")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()

print("Silhouette Scores:", dict(zip(range(2, 8), scores)))

# Final clustering
best_k = range(2, 8)[scores.index(max(scores))]
kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10)
df["Customer_Segment"] = kmeans.fit_predict(X)

# Segment summary
summary = df.groupby("Customer_Segment")[features].mean().round(2)
print(summary)

# Visualization
sns.scatterplot(data=df, x="Income", y="MntWines",
                hue="Customer_Segment", palette="Set2")
plt.title("Customer Segmentation")
plt.show()

# Save results
df.to_csv("customer_segments.csv", index=False)
summary.to_csv("segment_summary.csv")