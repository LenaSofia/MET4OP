#%%

import pandas as pd, matplotlib as plt, geopandas as gpd, contextily as ctx, numpy as np



# %% [markdown]
### Mapas
#%%
resultados = gpd.read_file(r'C:\Users\Usuario\Desktop\MAOP\TP_2\MET4OP\dataset\elecciones_2019\CABA.shp')
censo = gpd.read_file(r'C:\Users\Usuario\Desktop\MAOP\TP_2\MET4OP\dataset\censo2010\radios_censales\Codgeo_CABA_con_datos\cabaxrdatos.shp')

# %%
circuitos = resultados.to_crs(epsg=3857)
radios = censo.to_crs(epsg=3857)

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
censo_persona_edad = censo_persona[["PERSONA_REF_ID", "HOGAR_REF_ID", "P03"]]
censo_persona_edad

# %% 
# Me gustaría conseguir el promedio de edad por hogar, ¿cómo hago eso?
censo_persona_edad.groupby(["HOGAR_REF_ID"])["P03"].mean().to_frame()
# %%
censo_completo = pd.merge(censo_persona, censo_hogar, on="HOGAR_REF_ID")
censo_completo = pd.merge(censo_completo, censo_vivienda, on="VIVIENDA_REF_ID")
censo_completo = pd.merge(censo_completo, censo_radio, on="RADIO_REF_ID")
censo_completo = pd.merge(censo_completo, censo_fraccion, on="FRAC_REF_ID")
censo_completo = pd.merge(censo_completo, censo_dpto, on="DPTO_REF_ID")
censo_completo = pd.merge(censo_completo, censo_prov, on="PROV_REF_ID")

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
circuitos["LINK_circuito"] = circuitos["distrito"] + circuitos['indec_d'] + circuitos['circuito']
circuitos

#%%
# Me quedo solo con las columnas que me interesan
sub_circuitos = circuitos[["LINK_circuito", "geometry"]]
sub_circuitos.sort_values(by=["LINK_circuito"])

# %%
# Hago el condenado Spatial Join
join = gpd.sjoin(sub_radios, sub_circuitos, how='left', op= 'within')

# Y listo
#%% [markdown]
#### Prueba para ver si esta bien hecho el merge
#%%
join.sort_values(by= "LINK_circuito").head(20)
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


# COINCIDEN A LA PERFECCIÓN
# %%
