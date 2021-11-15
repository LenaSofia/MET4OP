
import pandas as pd, matplotlib.pyplot as plt, geopandas as gpd, contextily as ctx, numpy as np

# %%

# Mapas

#resultados = gpd.read_file(r'../elecciones_2019/CABA.shp')

# %%

#resultados = resultados.to_crs(epsg=3857)
#resultados.plot(figsize=(10,10), alpha=0.35, edgecolor='k')
#plt.show()

# %%

# Datos

resultados = pd.read_csv('../elecciones_2019/resultados/120819-054029/datos_agrup.csv')

#%%

# Agrego la columna "CODIGO_CIRCUITO" al DF resultados (georeferenciados) para unir ambos DF

#elecc_comp_geo = resultados.assign(CODIGO_CIRCUITO="")

# Lleno la columna "CODIGO_CIRCUITO" con los datos correspondientes (codigo sección + circuito)

#dato = 0

#for fila in range(0, 167):
#    dato = "1" + str(elecc_comp_geo.loc[fila, "indec_d"])
#    dato += "00" + str(elecc_comp_geo.loc[fila, "circuito"])

#    elecc_comp_geo.loc[fila, "CODIGO_CIRCUITO"] = int(dato)

#%%

#elecciones_recortado = resultados.drop(resultados.columns[[0, 0]], axis='columns')
elecciones_recortado = resultados.drop(columns=["CODIGO_DISTRITO", "CODIGO_AGRUPACION", "CODIGO_SECCION"],
                                                 axis=1)

#%%

elecciones_recortado.to_csv("elecciones_cortado.csv")
