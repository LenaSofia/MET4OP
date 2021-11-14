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
# %%
# Esperanza de edad de cada circuito:
# Primero calculo la probabilidad de pertenecer a cada grupo de edad

# Necesito que me cuente en cada circuito cuantas personas tengo de cada categoría
DF_16_mas.sort_values(by="EDAD_AG")
prob_edad = DF_16_mas.pivot_table(index=["CODIGO_CIRCUITO"], columns=["EDAD_AG"], aggfunc= "size")
# prob_edad

#%%
# AHora necesito saber el porcentaje de que una persona pertenezca a cada rango
# df['Fruit Total']= df.iloc[:, -4:-1].sum(axis=1)

prob_edad["POB_CIRC"] = prob_edad.iloc[:,:].sum(axis=1)
prob_edad
# %%
# Con esto ya puedo saber la probabilidad de cada categoría, dividiendo la categoría por el total
# (Debe existir una manera más eficiente de lograr esto, es bastante horrible)


prob_edad["PROB_0"] = prob_edad[0] / prob_edad["POB_CIRC"]
prob_edad["PROB_1"] = prob_edad[1] / prob_edad["POB_CIRC"]
prob_edad["PROB_2"] = prob_edad[2] / prob_edad["POB_CIRC"]
prob_edad["PROB_3"] = prob_edad[3] / prob_edad["POB_CIRC"]
prob_edad["PROB_4"] = prob_edad[4] / prob_edad["POB_CIRC"]


prob_edad

# %%
# Y con esto ya puedo sacar la esperanza

prob_edad["ESPERANZA"] = (prob_edad['PROB_0'] * 0) + (prob_edad['PROB_1'] * 1) + (prob_edad['PROB_2'] * 2) + (prob_edad['PROB_3'] * 3) + (prob_edad['PROB_4'] * 4)
prob_edad

# Ahora a sacar la varianza
# %%
# ME quedo solo con la esperanza para mergear con la tabla original
esperanza_circ = prob_edad[["POB_CIRC","ESPERANZA"]]
# %%
esperanza_circ
# %%
DF_16_esp = pd.merge(DF_16_mas, esperanza_circ, on="CODIGO_CIRCUITO")


#%%
# Media de todas las edades posibles y existentes




DF_edad_mean = DF_edad.groupby(["NOMBRE_REGION", "CODIGO_CIRCUITO"])["P03"].mean().to_frame()
DF_edad_mean
# %% 
# Media solo más 16

prom_edad_16_mas = DF_16_mas.groupby(["NOMBRE_REGION", "CODIGO_CIRCUITO"])["P03"].mean().to_frame()
prom_edad_16_mas


# %%
