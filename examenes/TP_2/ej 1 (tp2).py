#%%
import numpy as np
import pandas as pd

resultCABA = pd.read_csv (                          # Resultados totales
    "datos_agrup.csv"
)
resultCABA.head()

#%% [markdown]
### Funciones para armar tablas de porcentaje por circuito y por comuna
# La idea es que se puedan aplicar a distintas categorías y agrupaciones

#%%
def porcentaje_circuito(result_total, result_agrupacion):
    """
    Función que a partir de tablas con el caro en disputa y una agrupación en específico, 
    calcula el porcentaje por circuito electoral
    """

    # Primero suma la cantidad de votos totales por circuito
    result_total_acotado = result_total[["CODIGO_CIRCUITO", "CODIGO_MESA", "VOTOS_AGRUPACION", "NOMBRE_REGION", "NOMBRE_AGRUPACION"]]

    result_total_circuito = (result_total_acotado.groupby(["NOMBRE_REGION", "CODIGO_CIRCUITO"]).sum())

    result_total_circuito = result_total_circuito.rename(columns={"VOTOS_AGRUPACION": "VOTOS_TOTALES"})


    # Luego suma la cantidad de votos de determinada agrupacion por circuito
    result_agrupacion_acotado = result_agrupacion[["CODIGO_CIRCUITO", "CODIGO_MESA", "VOTOS_AGRUPACION", "NOMBRE_REGION", "NOMBRE_AGRUPACION"]]

    result_agrupacion_circuito = (result_agrupacion_acotado.groupby(["NOMBRE_REGION", "CODIGO_CIRCUITO"]).sum())

    # Luego hace un merge, y calcula el porcentaje diviendo votos de la agrupacion por totales
    porcentaje_circuito = pd.merge(result_total_circuito, result_agrupacion_circuito, on=["NOMBRE_REGION","CODIGO_CIRCUITO"])

    porcentaje_circuito["PORCENTAJE_AGRUPACION"] = ((porcentaje_circuito["VOTOS_AGRUPACION"] / porcentaje_circuito["VOTOS_TOTALES"]) * 100).round(2)


    return porcentaje_circuito
#%%
def porcentaje_comuna(porcentaje_circuito):
    """
    Función que en base al porcentaje por circuito
    calcula el porcentaje por comuna
    """
    porcentaje_comuna = (porcentaje_circuito.groupby("NOMBRE_REGION")["VOTOS_TOTALES", "VOTOS_AGRUPACION"].sum())
    porcentaje_comuna["PORCENTAJE_AGRUPACION"] = ((porcentaje_comuna["VOTOS_AGRUPACION"] / porcentaje_comuna["VOTOS_TOTALES"] * 100).round(2))

    return porcentaje_comuna

#%% [markdown]
### Porcentajes del FIT para categorías Presidente y Vicepresidente
#%%
# Resultados del FIT en cada mesa solo para Presidente
resultCABA_pres_fit = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República") & (resultCABA["NOMBRE_AGRUPACION"] == "FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD")]
resultCABA_pres_fit.reset_index(inplace=True)

#%%
# Resultados totales en cada mesa solo para Presidente
resultCABA_pres_total = resultCABA[resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República"]
resultCABA_pres_total.reset_index(inplace=True)

#%%
# Porcentaje del FIT por circuito
porc_pres_circuito_fit = porcentaje_circuito(resultCABA_pres_total, resultCABA_pres_fit)
porc_pres_circuito_fit

#%%
# Porcentaje del FIT por comuna
porc_pres_comuna_fit = porcentaje_comuna(porc_pres_circuito_fit)
porc_pres_comuna_fit

#%%
# Pendiente: 
# - Ver como georeferenciar las tablas (quiza hacer un mapa)
# - Hacer algunos graficos copados
# - Comparar con el voto legislativo
# - Comparar el voto legislativo con el voto en blanco en presidente