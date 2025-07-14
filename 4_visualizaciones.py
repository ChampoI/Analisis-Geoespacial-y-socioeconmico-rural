import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("resultados_modelo.csv")

plt.figure(figsize=(10,6))
sns.boxplot(x='cluster', y='HaAgro', data=df)
plt.title("Distribución de hectáreas agropecuarias por cluster")
plt.show()