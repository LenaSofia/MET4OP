import pandas as pd, matplotlib.pyplot as plt, geopandas as gpd, contextily as ctx, numpy as np

#%%

# Importo .csv:

promedio_edad_circuito = pd.read_csv("media_circuito_16_70.csv")

elecciones = pd.read_csv("../resultados.csv")

#%%

# Construyo DF con promedio_edad_circuito y la columna de votos al FIT de elecciones

corr_edad_pres_fit_circuito = pd.merge(promedio_edad_circuito, elecciones[["CODIGO_CIRCUITO", "VOTOS_FIT_PRES",
                                                                           "PORCENTAJE_FIT_PRES"]], on="CODIGO_CIRCUITO")

corr_circuitos = corr_edad_pres_fit_circuito.drop(columns=["NOMBRE_REGION", "CODIGO_CIRCUITO"], axis=1)

#%%

matriz_corr_circ = corr_circuitos.corr()