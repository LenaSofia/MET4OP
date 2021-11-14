import pandas as pd, matplotlib.pyplot as plt, geopandas as gpd, contextily as ctx, numpy as np

#%%

# Importo .csv:

DF_completo = pd.read_csv("D:/UBA/4to Cuarto año/Segundo cuatrimestre/Metodología de análisis en opinión pública/"
                          "GITHUB_ANTERIOR/examenes/TP2/segunda_parte/Lena/correlacion/esperanza_agrupada_votos.csv")

#%%

# Uso sólo las columnas que necesito:

# Total
DF_para_corr = DF_completo[["VOTOS_FIT_PRES", "PORCENTAJE_FIT_PRES", "ESPERANZA_EDAD_AGRUPADA"]]

#%%

# Armo las matrices de correlación

# Total
matriz_DF_corr = DF_para_corr.corr()
