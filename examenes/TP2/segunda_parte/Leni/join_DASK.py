#%%

import pandas as pd, matplotlib as plt, geopandas as gpd, contextily as ctx, numpy as np
import dask.dataframe as dd

#%%

# Importo los archivos y borro el indice:

join_radios_circuitos = dd.read_csv("geom_join.csv", assume_missing=True)
join_radios_circuitos = join_radios_circuitos.drop(join_radios_circuitos.columns[[0, 0]], axis='columns')

#%%

elecciones_completo = dd.read_csv("elecciones_recortado.csv", assume_missing=True)
elecciones_completo = elecciones_completo.drop(elecciones_completo.columns[[0, 0]], axis='columns')

#%%
censo_cortado = dd.read_csv("censo_cortado.csv", assume_missing=True)
censo_cortado = censo_cortado.drop(censo_cortado.columns[[0, 0]], axis='columns')



#%%

# Joineo toodo

DF_completo = dd.merge(join_radios_circuitos, elecciones_completo, on="CODIGO_CIRCUITO")

#%%

DF_completo = dd.merge(DF_completo, censo_cortado, on="LINK")

DF_completo.to_csv("JOIN_con_DASK.csv")

DF_DASK = dd.read_csv("JOIN_con_DASK.csv", assume_missing=True)

print("aaa")