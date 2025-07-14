# Análisis del Uso y Tenencia de la Tierra

Este proyecto analiza cómo se distribuye la tierra y los regímenes de tenencia en zonas rurales dispersas.

## 📄 Descripción del dataset

El conjunto de datos contiene información sobre:
- https://www.datos.gov.co/dataset/Censo-Nacional-Agropecuario-Uso-de-la-tierra/f9jj-yx8h/about_data

- **Distribución de coberturas y usos del suelo:**
  - `HaNatura`: Hectáreas con cobertura natural.
  - `HaAgro`: Hectáreas con uso agropecuario.
  - `HanoAgro`: Hectáreas con uso no agropecuario.
  - `HaOtro`: Hectáreas con otros usos.

- **Régimen de tenencia de la tierra:**
  - `PrPropia`: Tierra en propiedad propia.
  - `PrArrien`: Tierra en arriendo.
  - `PrAparce`: Tierra en aparcería.
  - `PrUsufru`: Tierra en usufructo.
  - `PrComoda`: Tierra en comodato.
  - `PrOcupac`: Tierra ocupada de hecho.
  - `PrColect`: Propiedad colectiva.
  - `PrAdjudi`: Adjudicatario comunero.
  - `PrOtros`: Otras formas de tenencia.
  - `PrMixta`: Tenencia mixta.

- **Unidades de producción:**
  - `UPA`: Número de Unidades de Producción Agropecuaria.
  - `UPNA`: Número de Unidades de Producción No Agropecuaria.

- **Variables geográficas:**
  - `DPTO`, `MPIO`: Departamento y municipio.
  - `LATITUDE`, `LONGITUDE`, `ELEVATION`: Datos geográficos.

## Instrucciones

1. Instala dependencias:
```
pip install pandas matplotlib seaborn scikit-learn
```

2. Corre los scripts en orden:
```
python 1_analisis_exploratorio.py
python 2_limpieza_datos.py
python 3_modelo_clustering.py
python 4_visualizaciones.py
```

## Resultado

- Estadísticas y gráficas descriptivas.
- Clustering de municipios por uso del suelo.
- Archivo exportado con resultados: `resultados_modelo.csv`

## Interpretacion inicial 
- Cluster 2 tiene municipios con muchas más hectáreas agropecuarias. La mediana está por encima de 1 millón y hay municipios con más de 2.4 millones de hectáreas.
- Clusters 0 y 1 agrupan municipios con menores superficies agropecuarias. Aunque hay algunos outliers que tienen más, la mayoría tienen menos de 100.000 hectáreas.
- Cluster 1 parece ser el más homogéneo y con menos superficie agropecuaria en promedio.

## Este tipo de análisis ayuda a:
- Identificar regiones con mayor desarrollo agropecuario.
- Agrupar municipios para aplicar políticas diferenciadas.
- Detectar concentraciones de tierra en ciertos territorios (como podría ser el caso del cluster 2).
