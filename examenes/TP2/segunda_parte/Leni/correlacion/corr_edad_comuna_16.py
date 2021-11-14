import pandas as pd, matplotlib.pyplot as plt, geopandas as gpd, contextily as ctx, numpy as np

#%%

# Importo .csv:

promedio_edad_circuito = pd.read_csv("D:/UBA/4to Cuarto año/Segundo cuatrimestre/Metodología de análisis en opinión pública/GITHUB_ANTERIOR/examenes/TP2/segunda_parte/Lena/correlacion/media_edad_completa.csv")

elecciones = pd.read_csv("D:/UBA/4to Cuarto año/Segundo cuatrimestre/Metodología de análisis en opinión pública/GITHUB_ANTERIOR/examenes/TP2/segunda_parte/Lena/resultados.csv")

#%%

# Construyo DF con promedio_edad_circuito y la columna de votos al FIT de elecciones

corr_edad_pres_fit_comuna = pd.merge(promedio_edad_circuito, elecciones[["CODIGO_CIRCUITO", "VOTOS_FIT_PRES",
                                                                           "PORCENTAJE_FIT_PRES"]], on="CODIGO_CIRCUITO")


#%%

matriz_corr_circ = corr_edad_pres_fit_comuna.corr()