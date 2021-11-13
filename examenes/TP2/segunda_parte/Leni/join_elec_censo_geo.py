
import pandas as pd, matplotlib as plt, geopandas as gpd, contextily as ctx, numpy as np

#%%

# Importo los archivos y borro el indice:

join_radios_circuitos = pd.read_csv("geom_join.csv")
join_radios_circuitos = join_radios_circuitos.drop(join_radios_circuitos.columns[[0, 0]], axis='columns')


elecciones = pd.read_csv("elecciones_cortado.csv")
elecciones = elecciones.drop(elecciones.columns[[0, 0]], axis='columns')


censo = pd.read_csv("censo_cortado.csv")
censo = censo.drop(censo.columns[[0, 0]], axis='columns')

#%%

# Joineo toodo

#DF_completo = pd.merge(join_radios_circuitos, elecciones, on="CODIGO_CIRCUITO")

#%%

DF_completo = pd.merge(join_radios_circuitos, censo, on="LINK")