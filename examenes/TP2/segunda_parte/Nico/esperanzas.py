#%%
import pandas as pd, matplotlib.pyplot as plt, geopandas as gpd, contextily as ctx, numpy as np
from shapely import geometry
from six import b

# %%
from merge_presfit_censo import DF_completo
# %%
DF_completo.head()
# %%
# Voy a filtrar los menores de 16
# resultCABA_pres_total = resultCABA[resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República"]

DF_16_mas = DF_completo[DF_completo["P03"] > 15]
#%% [markdown]
#### Esperanza agrupada

# %%
DF_16_mas.columns
DF_16_mas = DF_16_mas[['geometry', 'centroide', 'CODIGO_CIRCUITO', 'NOMBRE_REGION',
       'VOTOS_TOTALES_PRES', 'VOTOS_FIT_PRES', 'PORCENTAJE_FIT_PRES',
       'RADIO_REF_ID', 'PERSONA_REF_ID', 'P03']]
# %%
# df['age_group'] = pd.cut(df['age'], bins=[0, 12, 19, 61, 100])
DF_16_mas["EDAD_AG"] = pd.cut(DF_16_mas["P03"], bins=[16, 17, 29, 39, 59, np.inf], include_lowest= True, labels= False)

#%%
DF_16_mas.to_csv("edad_agrupada_II.csv")

#%% 
# Probemos de otra forma xD
esperanza_agrupada = DF_16_mas.groupby(["NOMBRE_REGION", "CODIGO_CIRCUITO"])["EDAD_AG"].mean().to_frame()
esperanza_agrupada = esperanza_agrupada.rename(columns={"EDAD_AG": "ESPERANZA_EDAD_AGRUPADA"})
# %%
esperanza_agrupada_votos = pd.merge(DF_16_mas, esperanza_agrupada, on=["NOMBRE_REGION", "CODIGO_CIRCUITO"])
esperanza_agrupada_votos.columns

esperanza_agrupada_votos = esperanza_agrupada_votos[['geometry', 'centroide', 'CODIGO_CIRCUITO', 'NOMBRE_REGION',
       'VOTOS_TOTALES_PRES', 'VOTOS_FIT_PRES', 'PORCENTAJE_FIT_PRES','ESPERANZA_EDAD_AGRUPADA' ]]

esperanza_agrupada_votos.drop_duplicates("CODIGO_CIRCUITO", inplace=True)
esperanza_agrupada_votos.sort_values(by="NOMBRE_REGION", inplace= True)
esperanza_agrupada_votos.to_csv("esperanza_agrupada_votos.csv")
# %% 
# Media solo más 16

prom_edad_16_mas = DF_16_mas.groupby(["NOMBRE_REGION", "CODIGO_CIRCUITO"])["P03"].mean().to_frame()
prom_edad_16_mas

prom_edad_16mas_comuna = DF_16_mas.groupby(["NOMBRE_REGION"])["P03"].mean().to_frame()
prom_edad_16mas_comuna.to_csv("promedio_edad_comuna_16_para_arriba.csv")


# %%
prom_edad_16_mas.to_csv("promedio_edad_circuito_16_para_arriba.csv")

#%%
prom_edad_16_mas = DF_16_mas.groupby(["NOMBRE_REGION", "CODIGO_CIRCUITO"])["P03"].mean().to_frame()
prom_edad_16_mas = prom_edad_16_mas.rename(columns={"P03": "PROMEDIO_EDAD"})
prom_edad_16_mas
#%%
std_edad_16_mas = DF_16_mas.groupby(["NOMBRE_REGION", "CODIGO_CIRCUITO"])["P03"].std().to_frame()
std_edad_16_mas = std_edad_16_mas.rename(columns={"P03": "STD_EDAD"})

std_edad_16_mas


#%% 
prom_std_edad_circuito = pd.merge(prom_edad_16_mas, std_edad_16_mas, on=["NOMBRE_REGION", "CODIGO_CIRCUITO"])
prom_std_edad_circuito.head()

# %%
# Mergeo el promedio de edad con los datos electorales

edad_y_votos = pd.merge(DF_16_mas, prom_std_edad_circuito, on= ["NOMBRE_REGION", "CODIGO_CIRCUITO"])
edad_y_votos = edad_y_votos[['geometry', 'centroide', 'CODIGO_CIRCUITO', 'NOMBRE_REGION',
       'VOTOS_TOTALES_PRES', 'VOTOS_FIT_PRES', 'PORCENTAJE_FIT_PRES', 'PROMEDIO_EDAD',
       'STD_EDAD']]
# %%
# Elimina las edades particulares para que me quede el promedio de edad de cada circuito
edad_y_votos.drop_duplicates("CODIGO_CIRCUITO", inplace=True)

# %%
# Media completa (no solo +16)

media_edad_completa = DF_completo.groupby(["NOMBRE_REGION", "CODIGO_CIRCUITO"])["P03"].mean().to_frame()
media_edad_completa.to_csv("media_edad_completa.csv")
# %%
# Mediana de edades más 16 por circuito:
mediana_edad_mas16 = DF_16_mas.groupby(["NOMBRE_REGION", "CODIGO_CIRCUITO"])["P03"].median().to_frame()
mediana_edad_mas16.rename(columns={"P03": "MEDIANA_EDAD"}, inplace= True)
mediana_edad_mas16.to_csv("mediana_edad_mas16.csv")

# %%
# Media entre 16 y 70
DF_16_70 = DF_16_mas[DF_16_mas["P03"] < 70]
DF_16_70.sort_values(by= "P03", ascending=False)
# %%
media_edad_16_70_circ = DF_16_70.groupby(["NOMBRE_REGION", "CODIGO_CIRCUITO"])["P03"].mean().to_frame()
media_edad_16_70_circ.to_csv("media_circuito_16_70.csv")
# %%
