import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Cargar los datos
df = pd.read_csv("resultados_modelo.csv")

# Convertir columnas relevantes a numérico
columnas_numericas = [
    "HaNatura", "HaAgro", "HanoAgro", "HaOtro", "PrPropia", "PrArrien",
    "UPA", "UPNA", "cluster"
]
for col in columnas_numericas:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Inicializar app
app = dash.Dash(__name__)
app.title = "Dashboard Agropecuario de Colombia"

# Layout
app.layout = html.Div([
    html.H1("🌾 Dashboard Agropecuario de Colombia", style={'textAlign': 'center'}),

    html.Div([
        html.Label("📍 Filtrar por departamento (DPTO):", style={'fontSize': 16}),
        dcc.Dropdown(
            id='departamento-dropdown',
            options=[{'label': d, 'value': d} for d in sorted(df['DPTO'].dropna().unique())],
            placeholder="Selecciona un departamento (opcional)",
            style={'width': '60%', 'margin': 'auto'}
        ),
    ], style={'marginBottom': '30px'}),

    html.Div([
        html.Label("📊 Selecciona una variable para analizar:", style={'fontSize': 18}),
        dcc.Dropdown(
            id='variable-dropdown',
            options=[
                {'label': '🌳 Hectáreas de bosque natural', 'value': 'HaNatura'},
                {'label': '🚜 Hectáreas de uso agropecuario', 'value': 'HaAgro'},
                {'label': '🏭 Hectáreas no agropecuarias', 'value': 'HanoAgro'},
                {'label': '🗺️ Otras hectáreas', 'value': 'HaOtro'},
                {'label': '🏡 Propiedad propia', 'value': 'PrPropia'},
                {'label': '🏠 Tierra en arriendo', 'value': 'PrArrien'},
                {'label': '👨‍🌾 UPA - Producción agropecuaria', 'value': 'UPA'},
                {'label': '🏢 UPNA - No agropecuaria', 'value': 'UPNA'},
                {'label': '📌 Segmento / Cluster', 'value': 'cluster'}
            ],
            value='HaAgro',
            style={'width': '80%', 'margin': 'auto'}
        )
    ], style={'marginBottom': '40px', 'textAlign': 'center'}),

    dcc.Graph(id='histograma'),
    dcc.Graph(id='barplot'),
    html.Hr(),
    html.Div([
        html.H4("📦 Comparación por Clúster (sin valores extremos)", style={'textAlign': 'center'}),
        dcc.Graph(id='por-cluster')
    ])
])

@app.callback(
    Output('histograma', 'figure'),
    Output('barplot', 'figure'),
    Output('por-cluster', 'figure'),
    Input('variable-dropdown', 'value'),
    Input('departamento-dropdown', 'value')
)
def actualizar_graficos(variable, dpto):
    data = df.copy()
    if dpto:
        data = data[data['DPTO'] == dpto]

    if variable not in data.columns:
        fig_empty = px.scatter(title=f"⚠️ La columna '{variable}' no se encuentra.")
        return fig_empty, fig_empty, fig_empty

    df_filtrado = data[[variable]].dropna()
    if df_filtrado.empty:
        fig_empty = px.scatter(title=f"⚠️ No hay datos válidos para '{variable}'.")
        return fig_empty, fig_empty, fig_empty

    # Histograma
    hist = px.histogram(df_filtrado, x=variable, nbins=40,
                        color_discrete_sequence=['#00cc96'],
                        title=f'Distribución de {variable}')
    hist.update_layout(xaxis_title=variable, yaxis_title="Frecuencia")

    # Barras por municipio (top 30)
    data_bar = data[['MPIO', variable]].dropna().groupby('MPIO')[variable].sum().nlargest(30).reset_index()
    bar = px.bar(data_bar, x='MPIO', y=variable,
                 title=f"Top 30 municipios por {variable}",
                 labels={'MPIO': 'Municipio', variable: variable},
                 color_discrete_sequence=["#636efa"])
    bar.update_layout(xaxis_tickangle=-45)

    # Violin por cluster
    if 'cluster' in data.columns:
        df_cluster = data[['cluster', variable]].dropna()
        lim_sup = df_cluster[variable].quantile(0.95)
        df_cluster = df_cluster[df_cluster[variable] <= lim_sup]

        cluster_violin = px.violin(df_cluster, x="cluster", y=variable, box=True, points="all",
                                   color="cluster",
                                   color_discrete_sequence=px.colors.qualitative.Pastel,
                                   title=f"Distribución de {variable} por Clúster (sin extremos)")
        cluster_violin.update_layout(
            xaxis_title="Cluster",
            yaxis_title=f"{variable} (escala adaptada)",
            yaxis_type="log" if df_cluster[variable].max() > 10000 else "linear"
        )
    else:
        cluster_violin = px.scatter(title="⚠️ Columna 'cluster' no disponible")

    return hist, bar, cluster_violin

if __name__ == '__main__':
    app.run(debug=True)
