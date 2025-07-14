import pandas as pd

df = pd.read_csv("Censo_Nacional_Agropecuario_-_Uso_de_la_tierra.csv", low_memory=False)
df = df.dropna(axis=1, thresh=len(df) * 0.6)
df = df.dropna()
df.to_csv("datos_limpio.csv", index=False)
print("✅ Archivo limpio guardado: datos_limpio.csv")
print("Filas finales:", df.shape[0])
print("Columnas disponibles:", df.columns.tolist())