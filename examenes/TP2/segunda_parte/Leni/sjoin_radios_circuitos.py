#%%

import pandas as pd, matplotlib as plt, geopandas as gpd, contextily as ctx, numpy as np

# %% [markdown]
### Mapas
#%%

resultados = gpd.read_file(r'..\elecciones_2019\CABA.shp')
censo = gpd.read_file(r'..\censo2010\radios_censales\Codgeo_CABA_con_datos\cabaxrdatos.shp')

# %%

circuitos = resultados.to_crs(epsg=3857)
radios = censo.to_crs(epsg=3857)

# %% [markdown]
### Datos

#censo_completo = pd.read_csv("censo_cortado.csv")
#elecciones_completo = pd.read_csv("elecciones_cortado.csv")

# %% [markdown]
#### El merge de Radios y Circuitos

#%%
# Primero calculo el centroide de los radios electorales
radios['centroide'] = radios['geometry'].centroid
# %%
# Luego hago esos centroides su columna de geometrias
radios_cent = radios.set_geometry('centroide')
# %%
# Me quedo solamente con las columnas que em interesan
sub_radios = radios_cent[['LINK', 'geometry', 'centroide']]
sub_radios.sort_values(by=["LINK"])
# %%
# Construyo el link de los circuitos concatenando columnas

dato = 0

for fila in range(0, 167):
    dato = "1" + str(circuitos.loc[fila, "indec_d"])
    dato += "00" + str(circuitos.loc[fila, "circuito"])
    circuitos.loc[fila, "CODIGO_CIRCUITO"] = str(dato)
#    if pd.isna(circuitos.loc[fila, "CODIGO_CIRCUITO"]):
#        circuitos = circuitos.drop([fila, "CODIGO-CIRCUITO"])

#%%
# Me quedo solo con las columnas que me interesan
sub_circuitos = circuitos[["CODIGO_CIRCUITO", "geometry"]]
sub_circuitos.sort_values(by=["CODIGO_CIRCUITO"])

# %%
# Hago el condenado Spatial Join
join = gpd.sjoin(sub_radios, sub_circuitos, how='left', op= 'within')

# Y listo
#%% [markdown]
#### Prueba para ver si esta bien hecho el merge
#%%
join.sort_values(by= "CODIGO_CIRCUITO").head(20)
# %%
# Construyo un DF que solo contenga los radios que corresponden al circuito 01001001
prueba_radios = sub_radios.iloc[[2387, 2442, 2390, 2328, 2588, 2483, 2330, 2488, 2439, 2332, 2552, 2498, 2498, 2544, 2541, 2598, 2394, 2549, 2434, 2339]]

# %%
# Construyo un DF que solo contenga el circuito 01001001
prueba_circuitos = sub_circuitos.iloc[[7]]

#%%
# Chequeo en qué zona están los radios respecto al basemap
ax = prueba_radios.plot(figsize= (10,10), color= 'red')
ctx.add_basemap(ax, zoom=16)

# %%
# Chequeo en qué zona está el circuito respecto al basemap

ax2 = prueba_circuitos.plot(figsize= (10,10), alpha= 0.35)
ctx.add_basemap(ax2, zoom= 16)


# %%
# Exporto el join a un .csv

join.to_csv("geom_join.csv")