
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

# Importo csvs

censo_persona = pd.read_csv(r'..\censo2010\persona.csv')
censo_hogar = pd.read_csv(r'..\censo2010\hogar.csv')
censo_vivienda = pd.read_csv(r'..\censo2010\vivienda.csv')
censo_radio = pd.read_csv(r'..\censo2010\radio.csv')
censo_fraccion = pd.read_csv(r'..\censo2010\frac.csv')
censo_dpto = pd.read_csv(r'..\censo2010\dpto.csv')
censo_prov = pd.read_csv(r'..\censo2010\prov.csv')
rosetta = pd.read_csv(r'..\elecciones_2019\rosetta.csv')

#%%

# Voy a unir las tablas del censo de radio en adelante (radio, fracción, comuna y provincia):

censo_reducido = pd.merge(censo_radio, censo_fraccion, on="FRAC_REF_ID")
censo_reducido = pd.merge(censo_reducido, censo_dpto, on="DPTO_REF_ID")
censo_reducido = pd.merge(censo_reducido, censo_prov, on="PROV_REF_ID")

# Lo guardo en un csv

censo_reducido.to_csv("censo_reducido.csv")

#%%

# Creo una columna vacía con el nombre LINK

censo_reducido = censo_reducido.assign(LINK="")

# Agrego la data a la columna LINK en censo_reducido

dato = 0

for fila in range(0, 3552):
    dato = "0" + str(censo_reducido.loc[fila, "DPTO"])
    dato += "0" + str(censo_reducido.loc[fila, "IDFRAC"])
    dato += "0" + str(censo_reducido.loc[fila, "IDRADIO"])
    censo_reducido.loc[fila, "LINK"] = dato

#%%

# Voy a unir todas las tablas del censo para generar censo_completo (censo reducido + vivienda, hogar y persona):

censo_completo = pd.merge(censo_reducido, censo_vivienda, on="RADIO_REF_ID")
censo_completo = pd.merge(censo_completo, censo_hogar, on="VIVIENDA_REF_ID")
censo_completo = pd.merge(censo_completo, censo_persona, on="HOGAR_REF_ID")


# Lo guardo en un csv

censo_completo.to_csv("censo_completo.csv")

#%%

# Ahora uno el censo completo con el censo geo-referenciado mediante el link:

censo_comp_geo = pd.merge(censo_completo, censo, on="LINK")

censo_comp_geo.to_csv("censo_comp_geo.csv")

#%%
# pruebas

