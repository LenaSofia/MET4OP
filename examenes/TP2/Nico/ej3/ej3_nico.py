

import pandas as pd, matplotlib as plt, geopandas as gpd, contextily as ctx, numpy as np



# %% [markdown]
### Mapas
#%%
resultados = gpd.read_file(r'C:\Users\Usuario\Desktop\MAOP\TP_2\MET4OP\dataset\elecciones_2019\CABA.shp')
# %%
resultados = resultados.to_crs(epsg=3857)
resultados.plot(figsize= (10,10), alpha = 0.35, edgecolor = 'k')


#%% 

censo = gpd.read_file(r'C:\Users\Usuario\Desktop\MAOP\TP_2\MET4OP\dataset\censo2010\radios_censales\Codgeo_CABA_con_datos\cabaxrdatos.shp')
censo.crs
# %%
censo.to_crs(epsg=3857)
# %%
censo.plot(figsize= (10,10), alpha= 0.25, edgecolor= 'k', color= 'yellow')
# %% [markdown]
### Datolos

#%%
# Importo csv's
censo_persona = pd.read_csv(r'C:\Users\Usuario\Desktop\MAOP\TP_2\MET4OP\dataset\censo2010\persona.csv')
censo_hogar = pd.read_csv(r'C:\Users\Usuario\Desktop\MAOP\TP_2\MET4OP\dataset\censo2010\hogar.csv')
censo_vivienda = pd.read_csv(r'C:\Users\Usuario\Desktop\MAOP\TP_2\MET4OP\dataset\censo2010\vivienda.csv')
censo_radio = pd.read_csv(r'C:\Users\Usuario\Desktop\MAOP\TP_2\MET4OP\dataset\censo2010\radio.csv')
censo_fraccion = pd.read_csv(r'C:\Users\Usuario\Desktop\MAOP\TP_2\MET4OP\dataset\censo2010\frac.csv')
censo_dpto = pd.read_csv(r'C:\Users\Usuario\Desktop\MAOP\TP_2\MET4OP\dataset\censo2010\dpto.csv')
censo_prov = pd.read_csv(r'C:\Users\Usuario\Desktop\MAOP\TP_2\MET4OP\dataset\censo2010\prov.csv')
rosetta = pd.read_csv(r'C:\Users\Usuario\Desktop\MAOP\TP_2\MET4OP\dataset\elecciones_2019\rosetta.csv')
#%%

rosetta.head()
#%%
censo_persona_edad = censo_persona[["PERSONA_REF_ID", "HOGAR_REF_ID", "P03"]]
censo_persona_edad

# %% 
# Me gustaría conseguir el promedio de edad por hogar, ¿cómo hago eso?
censo_persona_edad.groupby(["HOGAR_REF_ID"])["P03"].mean().to_frame()
# %%
