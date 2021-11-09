

import pandas as pd, matplotlib.pyplot as plt, geopandas as gpd, contextily as ctx, numpy as np

# %% [markdown]

### Mapas
#%%

resultados = gpd.read_file(r'../elecciones_2019/CABA.shp')

# %%

resultados = resultados.to_crs(epsg=3857)
resultados.plot(figsize=(10,10), alpha=0.35, edgecolor='k')
plt.show()

#%%

censo = gpd.read_file(r'..\censo2010\radios_censales\Codgeo_CABA_con_datos\cabaxrdatos.shp')
censo.crs
# %%
censo.to_crs(epsg=3857)
# %%
censo.plot(figsize= (10,10), alpha= 0.25, edgecolor= 'k', color= 'yellow')
plt.show()

# %% [markdown]

### Datos

#%%
# Importo csv's
censo_persona = pd.read_csv(r'..\censo2010\persona.csv')
censo_hogar = pd.read_csv(r'..\censo2010\hogar.csv')
censo_vivienda = pd.read_csv(r'..\censo2010\vivienda.csv')
censo_radio = pd.read_csv(r'..\censo2010\radio.csv')
censo_fraccion = pd.read_csv(r'..\censo2010\frac.csv')
censo_dpto = pd.read_csv(r'..\censo2010\dpto.csv')
censo_prov = pd.read_csv(r'..\censo2010\prov.csv')
rosetta = pd.read_csv(r'..\elecciones_2019\rosetta.csv')
#%%

# Voy a unir las tablas del censo:

censo_completo = pd.merge(censo_persona, censo_hogar, on="HOGAR_REF_ID")
censo_completo = pd.merge(censo_completo, censo_vivienda, on="VIVIENDA_REF_ID")
censo_completo = pd.merge(censo_completo, censo_radio, on="RADIO_REF_ID")
censo_completo = pd.merge(censo_completo, censo_fraccion, on="FRAC_REF_ID")
censo_completo = pd.merge(censo_completo, censo_dpto, on="DPTO_REF_ID")
censo_completo = pd.merge(censo_completo, censo_prov, on="PROV_REF_ID")

# Lo guardo en un csv

censo_completo.to_csv("censo_completo.csv")

# Ahora lo que tengo que hacer es unir mi DF censo_completo con mi DF censo, para tener en un mismo
# DF la geometría y toda la data, para hacer eso tengo que crear una columna en mi DF censo_completo que sea LINK
# uniendo la provincia (que va a ser 02), con la comuna (001, 002 ... 014, 015), fracción (la má grande es 21)
# y el radio (13 por ejemplo), y después mergeo los dos DF a través de esa columna