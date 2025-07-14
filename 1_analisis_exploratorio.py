import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv("Censo_Nacional_Agropecuario_-_Uso_de_la_tierra.csv")

# Filtrar sólo columnas numéricas
df_numeric = df.select_dtypes(include=['number'])

# Calcular correlación sólo entre columnas numéricas
correlation = df_numeric.corr()

# Graficar heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Mapa de calor de correlaciones numéricas")
plt.show()
