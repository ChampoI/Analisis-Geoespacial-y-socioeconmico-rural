import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv("datos_limpio.csv")
X = df[['HaNatura', 'HaAgro', 'HanoAgro', 'HaOtro']]
kmeans = KMeans(n_clusters=3, random_state=42).fit(X)
df['cluster'] = kmeans.labels_
df.to_csv("resultados_modelo.csv", index=False)

print("📊 Agrupamiento completo. Etiquetas de cluster añadidas.")