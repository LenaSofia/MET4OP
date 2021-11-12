
import pandas as pd, matplotlib.pyplot as plt, geopandas as gpd, contextily as ctx, numpy as np

# %%

# Mapas

elecciones_completo = pd.read_csv(r'elecc_comp_geo.csv')

#%%

elecciones_recortado = elecciones_completo.drop(elecciones_completo.columns[[0, 0]], axis='columns')
elecciones_recortado = elecciones_recortado.drop(columns=["distrito", "provincia", "cabecera", "indec_p",
                                                "indec_d", "CODIGO_DISTRITO", "CODIGO_AGRUPACION", "departamen"],
                                                 axis=1)

#%%

elecciones_recortado.to_csv("elecciones_recortado.csv")