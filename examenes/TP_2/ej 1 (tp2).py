#%%
import numpy as np
import pandas as pd

resultCABA = pd.read_csv (                          # Resultados totales
    "datos_agrup.csv"
)
resultCABA.head()

#%%
# Resultados del FIT en cada mesa solo para Presidente
resultCABA_PRES_FIT = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República") & (resultCABA["NOMBRE_AGRUPACION"] == "FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD")]
resultCABA_PRES_FIT.reset_index(inplace=True)

#%% 
# Me saco de encima las columnas que no me interesan. Igual la verdad es que no sé si es necesario este paso
resultCABA_PRES_FITa= resultCABA_PRES_FIT[["CODIGO_CIRCUITO", "CODIGO_MESA", "VOTOS_AGRUPACION", "NOMBRE_REGION", "NOMBRE_AGRUPACION"]]
resultCABA_PRES_FITa

#%%
# Suma los votos del FIT en cada mesa para obtener el total por circuito electoral

votos_fit_por_circuito = (resultCABA_PRES_FITa.groupby(["NOMBRE_REGION", "CODIGO_CIRCUITO"]).sum())
votos_fit_por_circuito = votos_fit_por_circuito.rename(columns={"VOTOS_AGRUPACION": "VOTOS_FIT"})
votos_fit_por_circuito

# %%
# A partir de aquí repito el proceso anterior de agrupar las mesas en circuitos pero con todos los partidos (no solo el FIT), 
# para poder calcular el porcentaje del FIT en cada circuito

# Me saco de encima las columnas que no me interesa
resultCABA_circuito = resultCABA[["CODIGO_CIRCUITO", "CODIGO_MESA", "VOTOS_AGRUPACION", "NOMBRE_CATEGORIA", "NOMBRE_AGRUPACION", "NOMBRE_REGION"]]
resultCABA_circuito_pres = resultCABA_circuito[resultCABA_circuito["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República"]
resultCABA_circuito_pres

#%%

# Agrupo las mesas en totales por circuito
votos_circuito_pres = (resultCABA_circuito_pres.groupby(["NOMBRE_REGION", "CODIGO_CIRCUITO"]).sum())
votos_circuito_pres = votos_circuito_pres.rename(columns={"VOTOS_AGRUPACION": "VOTOS_TOTALES"})
votos_circuito_pres
# %%
# Hago Merge de la tabla con los votos totales y la tabla con los votos del FIT

votos_total_fit = pd.merge(votos_circuito_pres, votos_fit_por_circuito, on=["NOMBRE_REGION","CODIGO_CIRCUITO"])
votos_total_fit
# %%
# Agrego la columna PORCENTAJE_FIT que divide los votos del FIT por sobre el total de votos en cada circuito (y multiplica por 100) obteniendo el porcentaje

votos_total_fit["PORCENTAJE_FIT"] = ((votos_total_fit["VOTOS_FIT"] / votos_total_fit["VOTOS_TOTALES"]) * 100).round(2)

votos_total_fit # Esta es la tabla que tiene el porcentaje de FIT en cada circuito
votos_total_fit.sort_values(by="PORCENTAJE_FIT")



# %%
# Agrupo los circuitos en cada Comuna, y luego calculo el porcentaje
 
votos_comuna = (votos_total_fit.groupby("NOMBRE_REGION")["VOTOS_TOTALES", "VOTOS_FIT"].sum())
votos_comuna["PORCENTAJE_FIT"] = ((votos_comuna["VOTOS_FIT"] / votos_comuna["VOTOS_TOTALES"] * 100).round(2))
votos_comuna # Esta es la tabla que tiene el porcentaje de FIT en cada comuna
# %%
# Las dos tablas que hice hasta ahora, ordenadas de mayor a menor. 
# Podría verse como georeferenciarlas
votos_total_fit.sort_values(by="PORCENTAJE_FIT", ascending=False)
votos_comuna.sort_values(by=["PORCENTAJE_FIT"], ascending=False)

#%%
# Pendiente: 
# - Ver como georeferenciar las tablas (quiza hacer un mapa)
# - Hacer algunos graficos copados
# - Comparar con el voto legislativo
# - Comparar el voto legislativo con el voto en blanco en presidente