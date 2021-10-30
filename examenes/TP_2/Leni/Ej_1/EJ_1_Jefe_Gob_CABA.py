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


#%%


# Resultados totales en cada mesa solo para Presidente

resultCABA_JefGob_total = resultCABA[resultCABA["NOMBRE_CATEGORIA"] == "Jefe de Gobierno Ciudad Autónoma de Buenos Aires"]

resultCABA_JefGob_total.reset_index(inplace=True, drop=True)


#%%


#FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD:

resultCABA_JefGob_FIT = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Jefe de Gobierno Ciudad Autónoma de Buenos Aires") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD")]

resultCABA_JefGob_FIT.reset_index(inplace=True, drop=True)

# Porcentaje del FIT por circuito
porc_JefGob_circuito_FIT = porcentaje_circuito(resultCABA_JefGob_total, resultCABA_JefGob_FIT)


# Porcentaje del FIT por comuna
porc_JefGob_comuna_FIT = porcentaje_comuna(porc_JefGob_circuito_FIT)

# Cambio de nombres FIT circuito
porc_JefGob_circuito_FIT = porc_JefGob_circuito_FIT.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_JEFGOB",
                                                          "VOTOS_AGRUPACION": "VOTOS_FIT_JEFGOB",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_FIT_JEFGOB"})

# Cambio de nombres FIT comuna
porc_JefGob_comuna_FIT = porc_JefGob_comuna_FIT.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_JEFGOB",
                                                          "VOTOS_AGRUPACION": "VOTOS_FIT_JEFGOB",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_FIT_JEFGOB"})

# Guardo FIT circuito
porc_JefGob_circuito_FIT.to_csv("data/jefe_gobierno/FIT/jefe_gob_FIT_circuito.csv", encoding="utf-8")

# Guardo FIT comuna
porc_JefGob_comuna_FIT.to_csv("data/jefe_gobierno/FIT/jefe_gob_FIT_comuna.csv", encoding="utf-8")


#%%


# FRENTE NOS

resultCABA_JefGob_NOS = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Jefe de Gobierno Ciudad Autónoma de Buenos Aires") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "FRENTE NOS")]

resultCABA_JefGob_NOS.reset_index(inplace=True, drop=True)

# Porcentaje del NOS por circuito
porc_JefGob_circuito_NOS = porcentaje_circuito(resultCABA_JefGob_total, resultCABA_JefGob_NOS)


# Porcentaje del NOS por comuna
porc_JefGob_comuna_NOS = porcentaje_comuna(porc_JefGob_circuito_NOS)

# Cambio de nombres NOS circuito
porc_JefGob_circuito_NOS = porc_JefGob_circuito_NOS.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_JEFGOB",
                                                          "VOTOS_AGRUPACION": "VOTOS_NOS_JEFGOB",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_NOS_JEFGOB"})

# Cambio de nombres NOS comuna
porc_JefGob_comuna_NOS = porc_JefGob_comuna_NOS.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_JEFGOB",
                                                          "VOTOS_AGRUPACION": "VOTOS_NOS_JEFGOB",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_NOS_JEFGOB"})

# Guardo NOS circuito
porc_JefGob_circuito_NOS.to_csv("data/jefe_gobierno/NOS/jefe_gob_NOS_circuito.csv", encoding="utf-8")

# Guardo NOS comuna
porc_JefGob_comuna_NOS.to_csv("data/jefe_gobierno/NOS/jefe_gob_NOS_comuna.csv", encoding="utf-8")


#%%


# JUNTOS POR EL CAMBIO

resultCABA_JefGob_JXC = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Jefe de Gobierno Ciudad Autónoma de Buenos Aires") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "JUNTOS POR EL CAMBIO")]

resultCABA_JefGob_JXC.reset_index(inplace=True, drop=True)

# Porcentaje del JXC por circuito
porc_JefGob_circuito_JXC = porcentaje_circuito(resultCABA_JefGob_total, resultCABA_JefGob_JXC)


# Porcentaje del JXC por comuna
porc_JefGob_comuna_JXC = porcentaje_comuna(porc_JefGob_circuito_JXC)

# Cambio de nombres JXC circuito
porc_JefGob_circuito_JXC = porc_JefGob_circuito_JXC.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_JEFGOB",
                                                          "VOTOS_AGRUPACION": "VOTOS_JXC_JEFGOB",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_JXC_JEFGOB"})

# Cambio de nombres JXC comuna
porc_JefGob_comuna_JXC = porc_JefGob_comuna_JXC.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_JEFGOB",
                                                          "VOTOS_AGRUPACION": "VOTOS_JXC_JEFGOB",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_JXC_JEFGOB"})

# Guardo JXC circuito
porc_JefGob_circuito_JXC.to_csv("data/jefe_gobierno/JXC/jefe_gob_JXC_circuito.csv", encoding="utf-8")

# Guardo JXC comuna
porc_JefGob_comuna_JXC.to_csv("data/jefe_gobierno/JXC/jefe_gob_JXC_comuna.csv", encoding="utf-8")


#%%


# FRENTE DE TODOS

resultCABA_JefGob_FDT = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Jefe de Gobierno Ciudad Autónoma de Buenos Aires") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "FRENTE DE TODOS")]

resultCABA_JefGob_FDT.reset_index(inplace=True, drop=True)

# Porcentaje del FDT por circuito
porc_JefGob_circuito_FDT = porcentaje_circuito(resultCABA_JefGob_total, resultCABA_JefGob_FDT)


# Porcentaje del FDT por comuna
porc_JefGob_comuna_FDT = porcentaje_comuna(porc_JefGob_circuito_FDT)

# Cambio de nombres FDT circuito
porc_JefGob_circuito_FDT = porc_JefGob_circuito_FDT.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_JEFGOB",
                                                          "VOTOS_AGRUPACION": "VOTOS_FDT_JEFGOB",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_FDT_JEFGOB"})

# Cambio de nombres FDT comuna
porc_JefGob_comuna_FDT = porc_JefGob_comuna_FDT.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_JEFGOB",
                                                          "VOTOS_AGRUPACION": "VOTOS_FDT_JEFGOB",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_FDT_JEFGOB"})

# Guardo FDT circuito
porc_JefGob_circuito_FDT.to_csv("data/jefe_gobierno/FDT/jefe_gob_FDT_circuito.csv", encoding="utf-8")

# Guardo FDT comuna
porc_JefGob_comuna_FDT.to_csv("data/jefe_gobierno/FDT/jefe_gob_FDT_comuna.csv", encoding="utf-8")


#%%


# CONSENSO FEDERAL

resultCABA_JefGob_CF = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Jefe de Gobierno Ciudad Autónoma de Buenos Aires") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "CONSENSO FEDERAL")]

resultCABA_JefGob_CF.reset_index(inplace=True, drop=True)

# Porcentaje del CF por circuito
porc_JefGob_circuito_CF = porcentaje_circuito(resultCABA_JefGob_total, resultCABA_JefGob_CF)


# Porcentaje del CF por comuna
porc_JefGob_comuna_CF = porcentaje_comuna(porc_JefGob_circuito_CF)

# Cambio de nombres CF circuito
porc_JefGob_circuito_CF = porc_JefGob_circuito_CF.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_JEFGOB",
                                                          "VOTOS_AGRUPACION": "VOTOS_CF_JEFGOB",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_CF_JEFGOB"})

# Cambio de nombres CF comuna
porc_JefGob_comuna_CF = porc_JefGob_comuna_CF.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_JEFGOB",
                                                          "VOTOS_AGRUPACION": "VOTOS_CF_JEFGOB",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_CF_JEFGOB"})

# Guardo CF circuito
porc_JefGob_circuito_CF.to_csv("data/jefe_gobierno/CF/jefe_gob_CF_circuito.csv", encoding="utf-8")

# Guardo CF comuna
porc_JefGob_comuna_CF.to_csv("data/jefe_gobierno/CF/jefe_gob_CF_comuna.csv", encoding="utf-8")


#%%


# UNITE POR LA LIBERTAD Y LA DIGNIDAD

resultCABA_JefGob_ULD = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Jefe de Gobierno Ciudad Autónoma de Buenos Aires") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "UNITE POR LA LIBERTAD Y LA DIGNIDAD")]

resultCABA_JefGob_ULD.reset_index(inplace=True, drop=True)

# Porcentaje del ULD por circuito
porc_JefGob_circuito_ULD = porcentaje_circuito(resultCABA_JefGob_total, resultCABA_JefGob_ULD)


# Porcentaje del ULD por comuna
porc_JefGob_comuna_ULD = porcentaje_comuna(porc_JefGob_circuito_ULD)

# Cambio de nombres ULD circuito
porc_JefGob_circuito_ULD = porc_JefGob_circuito_ULD.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_JEFGOB",
                                                          "VOTOS_AGRUPACION": "VOTOS_ULD_JEFGOB",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_ULD_JEFGOB"})

# Cambio de nombres ULD comuna
porc_JefGob_comuna_ULD = porc_JefGob_comuna_ULD.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_JEFGOB",
                                                          "VOTOS_AGRUPACION": "VOTOS_ULD_JEFGOB",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_ULD_JEFGOB"})

# Guardo ULD circuito
porc_JefGob_circuito_ULD.to_csv("data/jefe_gobierno/ULD/jefe_gob_ULD_circuito.csv", encoding="utf-8")

# Guardo ULD comuna
porc_JefGob_comuna_ULD.to_csv("data/jefe_gobierno/ULD/jefe_gob_ULD_comuna.csv", encoding="utf-8")


#%%


# BLANCO

resultCABA_JefGob_BLANCO = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Jefe de Gobierno Ciudad Autónoma de Buenos Aires") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "BLANCO")]

resultCABA_JefGob_BLANCO.reset_index(inplace=True, drop=True)

# Porcentaje del BLANCO por circuito
porc_JefGob_circuito_BLANCO = porcentaje_circuito(resultCABA_JefGob_total, resultCABA_JefGob_BLANCO)


# Porcentaje del BLANCO por comuna
porc_JefGob_comuna_BLANCO = porcentaje_comuna(porc_JefGob_circuito_BLANCO)

# Cambio de nombres BLANCO circuito
porc_JefGob_circuito_BLANCO = porc_JefGob_circuito_BLANCO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_JEFGOB",
                                                          "VOTOS_AGRUPACION": "VOTOS_BLANCO_JEFGOB",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_BLANCO_JEFGOB"})

# Cambio de nombres BLANCO comuna
porc_JefGob_comuna_BLANCO = porc_JefGob_comuna_BLANCO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_JEFGOB",
                                                          "VOTOS_AGRUPACION": "VOTOS_BLANCO_JEFGOB",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_BLANCO_JEFGOB"})

# Guardo BLANCO circuito
porc_JefGob_circuito_BLANCO.to_csv("data/jefe_gobierno/BLANCO/jefe_gob_BLANCO_circuito.csv", encoding="utf-8")

# Guardo BLANCO comuna
porc_JefGob_comuna_BLANCO.to_csv("data/jefe_gobierno/BLANCO/jefe_gob_BLANCO_comuna.csv", encoding="utf-8")


#%%


# IMPUGNADO

resultCABA_JefGob_IMPUGNADO = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Jefe de Gobierno Ciudad Autónoma de Buenos Aires") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "IMPUGNADO")]

resultCABA_JefGob_IMPUGNADO.reset_index(inplace=True, drop=True)

# Porcentaje del IMPUGNADO por circuito
porc_JefGob_circuito_IMPUGNADO = porcentaje_circuito(resultCABA_JefGob_total, resultCABA_JefGob_IMPUGNADO)


# Porcentaje del IMPUGNADO por comuna
porc_JefGob_comuna_IMPUGNADO = porcentaje_comuna(porc_JefGob_circuito_IMPUGNADO)

# Cambio de nombres IMPUGNADO circuito
porc_JefGob_circuito_IMPUGNADO = porc_JefGob_circuito_IMPUGNADO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_JEFGOB",
                                                          "VOTOS_AGRUPACION": "VOTOS_IMPUGNADO_JEFGOB",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_IMPUGNADO_JEFGOB"})

# Cambio de nombres IMPUGNADO comuna
porc_JefGob_comuna_IMPUGNADO = porc_JefGob_comuna_IMPUGNADO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_JEFGOB",
                                                          "VOTOS_AGRUPACION": "VOTOS_IMPUGNADO_JEFGOB",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_IMPUGNADO_JEFGOB"})

# Guardo IMPUGNADO circuito
porc_JefGob_circuito_IMPUGNADO.to_csv("data/jefe_gobierno/IMPUGNADO/jefe_gob_IMPUGNADO_circuito.csv", encoding="utf-8")

# Guardo IMPUGNADO comuna
porc_JefGob_comuna_IMPUGNADO.to_csv("data/jefe_gobierno/IMPUGNADO/jefe_gob_IMPUGNADO_comuna.csv", encoding="utf-8")


#%%


# NULO

resultCABA_JefGob_NULO = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Jefe de Gobierno Ciudad Autónoma de Buenos Aires") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "NULO")]

resultCABA_JefGob_NULO.reset_index(inplace=True, drop=True)

# Porcentaje del NULO por circuito
porc_JefGob_circuito_NULO = porcentaje_circuito(resultCABA_JefGob_total, resultCABA_JefGob_NULO)


# Porcentaje del NULO por comuna
porc_JefGob_comuna_NULO = porcentaje_comuna(porc_JefGob_circuito_NULO)

# Cambio de nombres NULO circuito
porc_JefGob_circuito_NULO = porc_JefGob_circuito_NULO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_JEFGOB",
                                                          "VOTOS_AGRUPACION": "VOTOS_NULO_JEFGOB",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_NULO_JEFGOB"})

# Cambio de nombres NULO comuna
porc_JefGob_comuna_NULO = porc_JefGob_comuna_NULO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_JEFGOB",
                                                          "VOTOS_AGRUPACION": "VOTOS_NULO_JEFGOB",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_NULO_JEFGOB"})

# Guardo NULO circuito
porc_JefGob_circuito_NULO.to_csv("data/jefe_gobierno/NULO/jefe_gob_NULO_circuito.csv", encoding="utf-8")

# Guardo NULO comuna
porc_JefGob_comuna_NULO.to_csv("data/jefe_gobierno/NULO/jefe_gob_NULO_comuna.csv", encoding="utf-8")


#%%


# RECURRIDO

resultCABA_JefGob_RECURRIDO = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Jefe de Gobierno Ciudad Autónoma de Buenos Aires") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "RECURRIDO")]

resultCABA_JefGob_RECURRIDO.reset_index(inplace=True, drop=True)

# Porcentaje del RECURRIDO por circuito
porc_JefGob_circuito_RECURRIDO = porcentaje_circuito(resultCABA_JefGob_total, resultCABA_JefGob_RECURRIDO)


# Porcentaje del RECURRIDO por comuna
porc_JefGob_comuna_RECURRIDO = porcentaje_comuna(porc_JefGob_circuito_RECURRIDO)

# Cambio de nombres RECURRIDO circuito
porc_JefGob_circuito_RECURRIDO = porc_JefGob_circuito_RECURRIDO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_JEFGOB",
                                                          "VOTOS_AGRUPACION": "VOTOS_RECURRIDO_JEFGOB",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_RECURRIDO_JEFGOB"})

# Cambio de nombres RECURRIDO comuna
porc_JefGob_comuna_RECURRIDO = porc_JefGob_comuna_RECURRIDO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_JEFGOB",
                                                          "VOTOS_AGRUPACION": "VOTOS_RECURRIDO_JEFGOB",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_RECURRIDO_JEFGOB"})

# Guardo RECURRIDO circuito
porc_JefGob_circuito_RECURRIDO.to_csv("data/jefe_gobierno/RECURRIDO/jefe_gob_RECURRIDO_circuito.csv", encoding="utf-8")

# Guardo RECURRIDO comuna
porc_JefGob_comuna_RECURRIDO.to_csv("data/jefe_gobierno/RECURRIDO/jefe_gob_RECURRIDO_comuna.csv", encoding="utf-8")


#%%

# DataFrame con porcentaje resultados jefe de gobierno completo, circuito


porc_JefGob_circuito = pd.merge(left=porc_JefGob_circuito_FIT, right=porc_JefGob_circuito_CF, left_index=True, right_index=True, suffixes=('', '_1'))
porc_JefGob_circuito = pd.merge(left=porc_JefGob_circuito, right=porc_JefGob_circuito_FDT, left_index=True, right_index=True, suffixes=('', '_3'))
porc_JefGob_circuito = pd.merge(left=porc_JefGob_circuito, right=porc_JefGob_circuito_JXC, left_index=True, right_index=True, suffixes=('', '_5'))
porc_JefGob_circuito = pd.merge(left=porc_JefGob_circuito, right=porc_JefGob_circuito_ULD, left_index=True, right_index=True, suffixes=('', '_9'))
porc_JefGob_circuito = pd.merge(left=porc_JefGob_circuito, right=porc_JefGob_circuito_NULO, left_index=True, right_index=True, suffixes=('', '_11'))
porc_JefGob_circuito = pd.merge(left=porc_JefGob_circuito, right=porc_JefGob_circuito_RECURRIDO, left_index=True, right_index=True, suffixes=('', '_13'))
porc_JefGob_circuito = pd.merge(left=porc_JefGob_circuito, right=porc_JefGob_circuito_IMPUGNADO, left_index=True, right_index=True, suffixes=('', '_15'))
porc_JefGob_circuito = pd.merge(left=porc_JefGob_circuito, right=porc_JefGob_circuito_BLANCO, left_index=True, right_index=True, suffixes=('', '_17'))

porc_JefGob_circuito.drop(['VOTOS_TOTALES_JEFGOB_1', 'VOTOS_TOTALES_JEFGOB_3', 'VOTOS_TOTALES_JEFGOB_5',
                        'VOTOS_TOTALES_JEFGOB_9', 'VOTOS_TOTALES_JEFGOB_11', 'VOTOS_TOTALES_JEFGOB_13',
                         'VOTOS_TOTALES_JEFGOB_15', 'VOTOS_TOTALES_JEFGOB_17'], axis=1, inplace=True)

porc_JefGob_circuito.to_csv("data/jefe_gobierno/jefe_gob_circuito.csv", encoding="utf-8")


#%%

# Le agrego una columna al df con el porcentaje de voto de otras agrupaciones

porc_JefGob_circuito_OTROS = pd.read_csv("data/jefe_gobierno/jefe_gob_circuito.csv")

lista_restos = pd.Series()

for n in range(0, 166):
    resto = porc_JefGob_circuito_OTROS.iloc[n, 2] - (porc_JefGob_circuito_OTROS.iloc[n, 3] +
                                                   porc_JefGob_circuito_OTROS.iloc[n, 5] +
                                                   porc_JefGob_circuito_OTROS.iloc[n, 7] +
                                                   porc_JefGob_circuito_OTROS.iloc[n, 9] +
                                                   porc_JefGob_circuito_OTROS.iloc[n, 11] +
                                                   porc_JefGob_circuito_OTROS.iloc[n, 13] +
                                                   porc_JefGob_circuito_OTROS.iloc[n, 15] +
                                                   porc_JefGob_circuito_OTROS.iloc[n, 17] +
                                                   porc_JefGob_circuito_OTROS.iloc[n, 19])
    resto = pd.Series(resto)
    lista_restos = lista_restos.append(resto, ignore_index=True)


porc_JefGob_circuito_OTROS['VOTOS_OTROS_JEFGOB'] = lista_restos

porcentajes_OTROS = pd.Series()


for n in range(0, 166):
    porcentaje = ((porc_JefGob_circuito_OTROS.iloc[n, -1] / porc_JefGob_circuito_OTROS.iloc[n, 2] * 100).round(2))
    porcentaje = pd.Series(porcentaje)
    porcentajes_OTROS = porcentajes_OTROS.append(porcentaje, ignore_index=True)

porc_JefGob_circuito_OTROS['PORCENTAJE_OTROS_JEFGOB'] = porcentajes_OTROS

porc_JefGob_circuito_OTROS.index = porc_JefGob_circuito_OTROS['NOMBRE_REGION']

porc_JefGob_circuito_OTROS.drop(['NOMBRE_REGION'], axis=1, inplace=True)

porc_JefGob_circuito_OTROS.to_csv("data/jefe_gobierno/jefe_gob_circuito_completo.csv", encoding="utf-8")



#%%



# DataFrame con porcentaje resultados jefe de gobierno completo, por comuna


porc_JefGob_comuna = pd.merge(left=porc_JefGob_comuna_FIT, right=porc_JefGob_comuna_CF, left_index=True, right_index=True, suffixes=('', '_1'))
porc_JefGob_comuna = pd.merge(left=porc_JefGob_comuna, right=porc_JefGob_comuna_FDT, left_index=True, right_index=True, suffixes=('', '_3'))
porc_JefGob_comuna = pd.merge(left=porc_JefGob_comuna, right=porc_JefGob_comuna_JXC, left_index=True, right_index=True, suffixes=('', '_5'))
porc_JefGob_comuna = pd.merge(left=porc_JefGob_comuna, right=porc_JefGob_comuna_ULD, left_index=True, right_index=True, suffixes=('', '_9'))
porc_JefGob_comuna = pd.merge(left=porc_JefGob_comuna, right=porc_JefGob_comuna_NULO, left_index=True, right_index=True, suffixes=('', '_11'))
porc_JefGob_comuna = pd.merge(left=porc_JefGob_comuna, right=porc_JefGob_comuna_RECURRIDO, left_index=True, right_index=True, suffixes=('', '_13'))
porc_JefGob_comuna = pd.merge(left=porc_JefGob_comuna, right=porc_JefGob_comuna_IMPUGNADO, left_index=True, right_index=True, suffixes=('', '_15'))
porc_JefGob_comuna = pd.merge(left=porc_JefGob_comuna, right=porc_JefGob_comuna_BLANCO, left_index=True, right_index=True, suffixes=('', '_17'))

porc_JefGob_comuna.drop(['VOTOS_TOTALES_JEFGOB_1', 'VOTOS_TOTALES_JEFGOB_3', 'VOTOS_TOTALES_JEFGOB_5',
                        'VOTOS_TOTALES_JEFGOB_9', 'VOTOS_TOTALES_JEFGOB_11', 'VOTOS_TOTALES_JEFGOB_13',
                         'VOTOS_TOTALES_JEFGOB_15', 'VOTOS_TOTALES_JEFGOB_17'], axis=1, inplace=True)

porc_JefGob_comuna.to_csv("data/jefe_gobierno/jefe_gob_comuna.csv", encoding="utf-8")


#%%

# Le agrego una columna al df con el porcentaje de voto de otras agrupaciones por comuna

porc_JefGob_comuna_OTROS = pd.read_csv("data/jefe_gobierno/jefe_gob_comuna.csv")

lista_restos_comuna = pd.Series()

for n in range(0, 15):
    resto_comuna = porc_JefGob_comuna_OTROS.iloc[n, 1] - (porc_JefGob_comuna_OTROS.iloc[n, 2] +
                                                   porc_JefGob_comuna_OTROS.iloc[n, 4] +
                                                   porc_JefGob_comuna_OTROS.iloc[n, 6] +
                                                   porc_JefGob_comuna_OTROS.iloc[n, 8] +
                                                   porc_JefGob_comuna_OTROS.iloc[n, 10] +
                                                   porc_JefGob_comuna_OTROS.iloc[n, 12] +
                                                   porc_JefGob_comuna_OTROS.iloc[n, 14] +
                                                   porc_JefGob_comuna_OTROS.iloc[n, 16] +
                                                   porc_JefGob_comuna_OTROS.iloc[n, 18])
    resto_comuna = pd.Series(resto_comuna)
    lista_restos_comuna = lista_restos_comuna.append(resto_comuna, ignore_index=True)


porc_JefGob_comuna_OTROS['VOTOS_OTROS_JEFGOB'] = lista_restos_comuna

porcentajes_OTROS_comuna = pd.Series()


for n in range(0, 15):
    porcentaje_comuna = ((porc_JefGob_comuna_OTROS.iloc[n, -1] / porc_JefGob_comuna_OTROS.iloc[n, 1] * 100).round(2))
    porcentaje_comuna = pd.Series(porcentaje_comuna)
    porcentajes_OTROS_comuna = porcentajes_OTROS.append(porcentaje_comuna, ignore_index=True)

porc_JefGob_comuna_OTROS['PORCENTAJE_OTROS_JEFGOB'] = porcentajes_OTROS_comuna

porc_JefGob_comuna_OTROS.index = porc_JefGob_comuna_OTROS['NOMBRE_REGION']

porc_JefGob_comuna_OTROS.drop(['NOMBRE_REGION'], axis=1, inplace=True)

porc_JefGob_comuna_OTROS.to_csv("data/jefe_gobierno/jefe_gob_comuna_completo.csv", encoding="utf-8")


#%%


# Distribución total (sin porcentajes)
# Circuitos

distrib_JefGob_circuito = porc_JefGob_circuito_OTROS.drop(["PORCENTAJE_FIT_JEFGOB", "PORCENTAJE_CF_JEFGOB",
                                                       "PORCENTAJE_FDT_JEFGOB", "PORCENTAJE_JXC_JEFGOB",
                                                       "PORCENTAJE_ULD_JEFGOB",
                                                        "PORCENTAJE_NULO_JEFGOB", "PORCENTAJE_RECURRIDO_JEFGOB",
                                                       "PORCENTAJE_IMPUGNADO_JEFGOB", "PORCENTAJE_BLANCO_JEFGOB",
                                                       "PORCENTAJE_OTROS_JEFGOB", "NOMBRE_REGION"
                                                       ], axis=1, inplace=False)

distrib_JefGob_circuito.to_csv("data/jefe_gobierno/distrib_JefGob_circuito.csv", encoding="utf-8")



# Distribución total (sin porcentajes)
# Comunas

distrib_JefGob_comuna = porc_JefGob_comuna_OTROS.drop(["PORCENTAJE_FIT_JEFGOB", "PORCENTAJE_CF_JEFGOB",
                                                       "PORCENTAJE_FDT_JEFGOB", "PORCENTAJE_JXC_JEFGOB",
                                                       "PORCENTAJE_ULD_JEFGOB",
                                                        "PORCENTAJE_NULO_JEFGOB", "PORCENTAJE_RECURRIDO_JEFGOB",
                                                       "PORCENTAJE_IMPUGNADO_JEFGOB", "PORCENTAJE_BLANCO_JEFGOB",
                                                       "PORCENTAJE_OTROS_JEFGOB", "NOMBRE_REGION"
                                                   ], axis=1, inplace=False)

distrib_JefGob_comuna.to_csv("data/jefe_gobierno/distrib_JefGob_comuna.csv", encoding="utf-8")


# Distribución de porcentajes
# Circuito

porcentajes_JefGob_circuito = porc_JefGob_circuito_OTROS.drop(["VOTOS_FIT_JEFGOB","VOTOS_CF_JEFGOB","VOTOS_FDT_JEFGOB",
                                                       "VOTOS_JXC_JEFGOB", "VOTOS_ULD_JEFGOB",
                                                       "VOTOS_NULO_JEFGOB","VOTOS_RECURRIDO_JEFGOB",
                                                       "VOTOS_IMPUGNADO_JEFGOB","VOTOS_BLANCO_JEFGOB",
                                                       "VOTOS_OTROS_JEFGOB", "NOMBRE_REGION"
                                                           ], axis=1, inplace=False)

for x in range(0, 166):
    porcentajes_JefGob_circuito.iloc[x, 1] = 100

porcentajes_JefGob_circuito.to_csv("data/jefe_gobierno/porcentajes_JefGob_circuito.csv", encoding="utf-8")


# Distribución de porcentajes
# Comuna

porcentajes_JefGob_comuna = porc_JefGob_comuna_OTROS.drop(["VOTOS_FIT_JEFGOB","VOTOS_CF_JEFGOB","VOTOS_FDT_JEFGOB",
                                                       "VOTOS_JXC_JEFGOB", "VOTOS_ULD_JEFGOB",
                                                       "VOTOS_NULO_JEFGOB","VOTOS_RECURRIDO_JEFGOB",
                                                       "VOTOS_IMPUGNADO_JEFGOB","VOTOS_BLANCO_JEFGOB",
                                                       "VOTOS_OTROS_JEFGOB", "NOMBRE_REGION"
                                                       ], axis=1, inplace=False)

for x in range(0, 15):
    porcentajes_JefGob_comuna.iloc[x, 0] = 100

porcentajes_JefGob_comuna.to_csv("data/jefe_gobierno/porcentajes_JefGob_comuna.csv", encoding="utf-8")