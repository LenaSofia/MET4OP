
import pandas as pd, matplotlib as plt, geopandas as gpd, contextily as ctx, numpy as np

#%%

# Importo los archivos y borro el indice:

join_radios_circuitos = pd.read_csv("geom_join.csv")
join_radios_circuitos = join_radios_circuitos.drop(join_radios_circuitos.columns[[0, 0]], axis='columns')


elecciones_completo = pd.read_csv("elecciones_recortado.csv")
elecciones_completo = elecciones_completo.drop(elecciones_completo.columns[[0, 0]], axis='columns')


censo_cortado = pd.read_csv("censo_cortado.csv")
censo_cortado = censo_cortado.drop(censo_cortado.columns[[0, 0]], axis='columns')

#%%

# Joineo toodo

DF_completo = pd.merge(join_radios_circuitos, elecciones_completo, on="CODIGO_CIRCUITO")

#%%

DF_completo = pd.merge(DF_completo, censo_cortado, on="LINK")