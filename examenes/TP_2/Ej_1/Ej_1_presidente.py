import numpy as np
import pandas as pd

resultCABA = pd.read_csv (                          # Resultados totales
    "datos_agrup.csv"
)


#%%


def porcentaje_circuito(result_total, result_agrupacion):
    """
    Función que a partir de tablas con el cargo en disputa y una agrupación en específico,
    calcula el porcentaje por circuito electoral
    """

    # Primero suma la cantidad de votos totales por circuito
    result_total_acotado = result_total[["CODIGO_CIRCUITO", "CODIGO_MESA", "VOTOS_AGRUPACION", "NOMBRE_REGION", "NOMBRE_AGRUPACION"]]

    result_total_circuito = (result_total_acotado.groupby(["NOMBRE_REGION", "CODIGO_CIRCUITO"]).sum())
    print(result_total_circuito)

    result_total_circuito = result_total_circuito.rename(columns={"VOTOS_AGRUPACION": "VOTOS_TOTALES"})
    print(result_total_circuito)

    # Luego suma la cantidad de votos de determinada agrupacion por circuito
    result_agrupacion_acotado = result_agrupacion[["CODIGO_CIRCUITO", "CODIGO_MESA", "VOTOS_AGRUPACION", "NOMBRE_REGION", "NOMBRE_AGRUPACION"]]
    print(result_agrupacion_acotado)

    result_agrupacion_circuito = (result_agrupacion_acotado.groupby(["NOMBRE_REGION", "CODIGO_CIRCUITO"]).sum())
    print(result_agrupacion_circuito)

    # Luego hace un merge, y calcula el porcentaje diviendo votos de la agrupacion por totales
    porcentaje_circuito = pd.merge(result_total_circuito, result_agrupacion_circuito, on=["NOMBRE_REGION","CODIGO_CIRCUITO"])
    print(porcentaje_circuito)

    porcentaje_circuito["PORCENTAJE_AGRUPACION"] = ((porcentaje_circuito["VOTOS_AGRUPACION"] / porcentaje_circuito["VOTOS_TOTALES"]) * 100).round(2)
    print(porcentaje_circuito)

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


#%%


# Resultados totales en cada mesa solo para Presidente

resultCABA_pres_total = resultCABA[resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República"]

resultCABA_pres_total.reset_index(inplace=True, drop=True)


#%%


#FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD:

resultCABA_pres_FIT = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD")]

resultCABA_pres_FIT.reset_index(inplace=True, drop=True)

# Porcentaje del FIT por circuito
porc_pres_circuito_FIT = porcentaje_circuito(resultCABA_pres_total, resultCABA_pres_FIT)
porc_pres_circuito_FIT.to_csv("data/presidente/FIT/pres_FIT_circuito.csv", encoding="utf-8")

# Porcentaje del FIT por comuna
porc_pres_comuna_FIT = porcentaje_comuna(porc_pres_circuito_FIT)
porc_pres_comuna_FIT.to_csv("data/presidente/FIT/pres_FIT_comuna.csv", encoding="utf-8")


#%%


# FRENTE NOS

resultCABA_pres_NOS = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "FRENTE NOS")]

resultCABA_pres_NOS.reset_index(inplace=True, drop=True)

# Porcentaje del NOS por circuito
porc_pres_circuito_NOS = porcentaje_circuito(resultCABA_pres_total, resultCABA_pres_NOS)
porc_pres_circuito_NOS.to_csv("data/presidente/NOS/pres_NOS_circuito.csv", encoding="utf-8")

# Porcentaje del NOS por comuna
porc_pres_comuna_NOS = porcentaje_comuna(porc_pres_circuito_NOS)
porc_pres_comuna_NOS.to_csv("data/presidente/NOS/pres_NOS_comuna.csv", encoding="utf-8")


#%%


# JUNTOS POR EL CAMBIO

resultCABA_pres_JXC = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "JUNTOS POR EL CAMBIO")]

resultCABA_pres_JXC.reset_index(inplace=True, drop=True)

# Porcentaje del JXC por circuito
porc_pres_circuito_JXC = porcentaje_circuito(resultCABA_pres_total, resultCABA_pres_JXC)
porc_pres_circuito_JXC.to_csv("data/presidente/JXC/pres_JXC_circuito.csv", encoding="utf-8")


# Porcentaje del JXC por comuna
porc_pres_comuna_JXC = porcentaje_comuna(porc_pres_circuito_JXC)
porc_pres_comuna_JXC.to_csv("data/presidente/JXC/pres_JXC_comuna.csv", encoding="utf-8")


#%%


# FRENTE DE TODOS

resultCABA_pres_FDT = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "FRENTE DE TODOS")]

resultCABA_pres_FDT.reset_index(inplace=True, drop=True)

# Porcentaje del FDT por circuito
porc_pres_circuito_FDT = porcentaje_circuito(resultCABA_pres_total, resultCABA_pres_FDT)
porc_pres_circuito_FDT.to_csv("data/presidente/FDT/pres_FDT_circuito.csv", encoding="utf-8")


# Porcentaje del FDT por comuna
porc_pres_comuna_FDT = porcentaje_comuna(porc_pres_circuito_FDT)
porc_pres_comuna_FDT.to_csv("data/presidente/FDT/pres_FDT_comuna.csv", encoding="utf-8")


#%%


# CONSENSO FEDERAL

resultCABA_pres_CF = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "CONSENSO FEDERAL")]

resultCABA_pres_CF.reset_index(inplace=True, drop=True)

# Porcentaje del CF por circuito
porc_pres_circuito_CF = porcentaje_circuito(resultCABA_pres_total, resultCABA_pres_CF)
porc_pres_circuito_CF.to_csv("data/presidente/CF/pres_CF_circuito.csv", encoding="utf-8")

# Porcentaje del CF por comuna
porc_pres_comuna_CF = porcentaje_comuna(porc_pres_circuito_CF)
porc_pres_comuna_CF.to_csv("data/presidente/CF/pres_CF_comuna.csv", encoding="utf-8")


#%%


# UNITE POR LA LIBERTAD Y LA DIGNIDAD

resultCABA_pres_ULD = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "UNITE POR LA LIBERTAD Y LA DIGNIDAD")]

resultCABA_pres_ULD.reset_index(inplace=True, drop=True)

# Porcentaje del ULD por circuito
porc_pres_circuito_ULD = porcentaje_circuito(resultCABA_pres_total, resultCABA_pres_ULD)
porc_pres_circuito_ULD.to_csv("data/presidente/ULD/pres_ULD_circuito.csv", encoding="utf-8")


# Porcentaje del ULD por comuna
porc_pres_comuna_ULD = porcentaje_comuna(porc_pres_circuito_ULD)
porc_pres_comuna_ULD.to_csv("data/presidente/ULD/pres_ULD_comuna.csv", encoding="utf-8")


#%%


# BLANCO

resultCABA_pres_BLANCO = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "BLANCO")]

resultCABA_pres_BLANCO.reset_index(inplace=True, drop=True)

# Porcentaje del BLANCO por circuito
porc_pres_circuito_BLANCO = porcentaje_circuito(resultCABA_pres_total, resultCABA_pres_BLANCO)
porc_pres_circuito_BLANCO.to_csv("data/presidente/BLANCO/pres_BLANCO_circuito.csv", encoding="utf-8")


# Porcentaje del BLANCO por comuna
porc_pres_comuna_BLANCO = porcentaje_comuna(porc_pres_circuito_BLANCO)
porc_pres_comuna_BLANCO.to_csv("data/presidente/BLANCO/pres_BLANCO_comuna.csv", encoding="utf-8")


#%%


# IMPUGNADO

resultCABA_pres_IMPUGNADO = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "IMPUGNADO")]

resultCABA_pres_IMPUGNADO.reset_index(inplace=True, drop=True)

# Porcentaje del IMPUGNADO por circuito
porc_pres_circuito_IMPUGNADO = porcentaje_circuito(resultCABA_pres_total, resultCABA_pres_IMPUGNADO)
porc_pres_circuito_IMPUGNADO.to_csv("data/presidente/IMPUGNADO/pres_IMPUGNADO_circuito.csv", encoding="utf-8")


# Porcentaje del IMPUGNADO por comuna
porc_pres_comuna_IMPUGNADO = porcentaje_comuna(porc_pres_circuito_IMPUGNADO)
porc_pres_comuna_IMPUGNADO.to_csv("data/presidente/IMPUGNADO/pres_IMPUGNADO_comuna.csv", encoding="utf-8")


#%%


# NULO

resultCABA_pres_NULO = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "NULO")]

resultCABA_pres_NULO.reset_index(inplace=True, drop=True)

# Porcentaje del NULO por circuito
porc_pres_circuito_NULO = porcentaje_circuito(resultCABA_pres_total, resultCABA_pres_NULO)
porc_pres_circuito_NULO.to_csv("data/presidente/NULO/pres_NULO_circuito.csv", encoding="utf-8")


# Porcentaje del NULO por comuna
porc_pres_comuna_NULO = porcentaje_comuna(porc_pres_circuito_NULO)
porc_pres_comuna_NULO.to_csv("data/presidente/NULO/pres_NULO_comuna.csv", encoding="utf-8")


#%%


# RECURRIDO

resultCABA_pres_RECURRIDO = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "RECURRIDO")]

resultCABA_pres_RECURRIDO.reset_index(inplace=True, drop=True)

# Porcentaje del RECURRIDO por circuito
porc_pres_circuito_RECURRIDO = porcentaje_circuito(resultCABA_pres_total, resultCABA_pres_RECURRIDO)
porc_pres_circuito_RECURRIDO.to_csv("data/presidente/RECURRIDO/pres_RECURRIDO_circuito.csv", encoding="utf-8")


# Porcentaje del RECURRIDO por comuna
porc_pres_comuna_RECURRIDO = porcentaje_comuna(porc_pres_circuito_RECURRIDO)
porc_pres_comuna_RECURRIDO.to_csv("data/presidente/RECURRIDO/pres_RECURRIDO_comuna.csv", encoding="utf-8")


#%%


