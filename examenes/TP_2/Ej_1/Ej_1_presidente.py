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

resultCABA_pres_total = resultCABA[resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República"]

resultCABA_pres_total.reset_index(inplace=True, drop=True)


#%%


#FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD:

resultCABA_pres_FIT = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD")]

resultCABA_pres_FIT.reset_index(inplace=True, drop=True)

# Porcentaje del FIT por circuito
porc_pres_circuito_FIT = porcentaje_circuito(resultCABA_pres_total, resultCABA_pres_FIT)


# Porcentaje del FIT por comuna
porc_pres_comuna_FIT = porcentaje_comuna(porc_pres_circuito_FIT)

# Cambio de nombres FIT circuito
porc_pres_circuito_FIT = porc_pres_circuito_FIT.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_PRES",
                                                          "VOTOS_AGRUPACION": "VOTOS_FIT_PRES",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_FIT_PRES"})

# Cambio de nombres FIT comuna
porc_pres_comuna_FIT = porc_pres_comuna_FIT.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_PRES",
                                                          "VOTOS_AGRUPACION": "VOTOS_FIT_PRES",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_FIT_PRES"})

# Guardo FIT circuito
porc_pres_circuito_FIT.to_csv("data/presidente/FIT/pres_FIT_circuito.csv", encoding="utf-8")

# Guardo FIT comuna
porc_pres_comuna_FIT.to_csv("data/presidente/FIT/pres_FIT_comuna.csv", encoding="utf-8")


#%%


# FRENTE NOS

resultCABA_pres_NOS = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "FRENTE NOS")]

resultCABA_pres_NOS.reset_index(inplace=True, drop=True)

# Porcentaje del NOS por circuito
porc_pres_circuito_NOS = porcentaje_circuito(resultCABA_pres_total, resultCABA_pres_NOS)


# Porcentaje del NOS por comuna
porc_pres_comuna_NOS = porcentaje_comuna(porc_pres_circuito_NOS)

# Cambio de nombres NOS circuito
porc_pres_circuito_NOS = porc_pres_circuito_NOS.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_PRES",
                                                          "VOTOS_AGRUPACION": "VOTOS_NOS_PRES",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_NOS_PRES"})

# Cambio de nombres NOS comuna
porc_pres_comuna_NOS = porc_pres_comuna_NOS.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_PRES",
                                                          "VOTOS_AGRUPACION": "VOTOS_NOS_PRES",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_NOS_PRES"})

# Guardo NOS circuito
porc_pres_circuito_NOS.to_csv("data/presidente/NOS/pres_NOS_circuito.csv", encoding="utf-8")

# Guardo NOS comuna
porc_pres_comuna_NOS.to_csv("data/presidente/NOS/pres_NOS_comuna.csv", encoding="utf-8")


#%%


# JUNTOS POR EL CAMBIO

resultCABA_pres_JXC = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "JUNTOS POR EL CAMBIO")]

resultCABA_pres_JXC.reset_index(inplace=True, drop=True)

# Porcentaje del JXC por circuito
porc_pres_circuito_JXC = porcentaje_circuito(resultCABA_pres_total, resultCABA_pres_JXC)


# Porcentaje del JXC por comuna
porc_pres_comuna_JXC = porcentaje_comuna(porc_pres_circuito_JXC)

# Cambio de nombres JXC circuito
porc_pres_circuito_JXC = porc_pres_circuito_JXC.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_PRES",
                                                          "VOTOS_AGRUPACION": "VOTOS_JXC_PRES",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_JXC_PRES"})

# Cambio de nombres JXC comuna
porc_pres_comuna_JXC = porc_pres_comuna_JXC.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_PRES",
                                                          "VOTOS_AGRUPACION": "VOTOS_JXC_PRES",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_JXC_PRES"})

# Guardo JXC circuito
porc_pres_circuito_JXC.to_csv("data/presidente/JXC/pres_JXC_circuito.csv", encoding="utf-8")

# Guardo JXC comuna
porc_pres_comuna_JXC.to_csv("data/presidente/JXC/pres_JXC_comuna.csv", encoding="utf-8")


#%%


# FRENTE DE TODOS

resultCABA_pres_FDT = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "FRENTE DE TODOS")]

resultCABA_pres_FDT.reset_index(inplace=True, drop=True)

# Porcentaje del FDT por circuito
porc_pres_circuito_FDT = porcentaje_circuito(resultCABA_pres_total, resultCABA_pres_FDT)


# Porcentaje del FDT por comuna
porc_pres_comuna_FDT = porcentaje_comuna(porc_pres_circuito_FDT)

# Cambio de nombres FDT circuito
porc_pres_circuito_FDT = porc_pres_circuito_FDT.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_PRES",
                                                          "VOTOS_AGRUPACION": "VOTOS_FDT_PRES",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_FDT_PRES"})

# Cambio de nombres FDT comuna
porc_pres_comuna_FDT = porc_pres_comuna_FDT.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_PRES",
                                                          "VOTOS_AGRUPACION": "VOTOS_FDT_PRES",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_FDT_PRES"})

# Guardo FDT circuito
porc_pres_circuito_FDT.to_csv("data/presidente/FDT/pres_FDT_circuito.csv", encoding="utf-8")

# Guardo FDT comuna
porc_pres_comuna_FDT.to_csv("data/presidente/FDT/pres_FDT_comuna.csv", encoding="utf-8")


#%%


# CONSENSO FEDERAL

resultCABA_pres_CF = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "CONSENSO FEDERAL")]

resultCABA_pres_CF.reset_index(inplace=True, drop=True)

# Porcentaje del CF por circuito
porc_pres_circuito_CF = porcentaje_circuito(resultCABA_pres_total, resultCABA_pres_CF)


# Porcentaje del CF por comuna
porc_pres_comuna_CF = porcentaje_comuna(porc_pres_circuito_CF)

# Cambio de nombres CF circuito
porc_pres_circuito_CF = porc_pres_circuito_CF.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_PRES",
                                                          "VOTOS_AGRUPACION": "VOTOS_CF_PRES",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_CF_PRES"})

# Cambio de nombres CF comuna
porc_pres_comuna_CF = porc_pres_comuna_CF.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_PRES",
                                                          "VOTOS_AGRUPACION": "VOTOS_CF_PRES",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_CF_PRES"})

# Guardo CF circuito
porc_pres_circuito_CF.to_csv("data/presidente/CF/pres_CF_circuito.csv", encoding="utf-8")

# Guardo CF comuna
porc_pres_comuna_CF.to_csv("data/presidente/CF/pres_CF_comuna.csv", encoding="utf-8")


#%%


# UNITE POR LA LIBERTAD Y LA DIGNIDAD

resultCABA_pres_ULD = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "UNITE POR LA LIBERTAD Y LA DIGNIDAD")]

resultCABA_pres_ULD.reset_index(inplace=True, drop=True)

# Porcentaje del ULD por circuito
porc_pres_circuito_ULD = porcentaje_circuito(resultCABA_pres_total, resultCABA_pres_ULD)


# Porcentaje del ULD por comuna
porc_pres_comuna_ULD = porcentaje_comuna(porc_pres_circuito_ULD)

# Cambio de nombres ULD circuito
porc_pres_circuito_ULD = porc_pres_circuito_ULD.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_PRES",
                                                          "VOTOS_AGRUPACION": "VOTOS_ULD_PRES",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_ULD_PRES"})

# Cambio de nombres ULD comuna
porc_pres_comuna_ULD = porc_pres_comuna_ULD.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_PRES",
                                                          "VOTOS_AGRUPACION": "VOTOS_ULD_PRES",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_ULD_PRES"})

# Guardo ULD circuito
porc_pres_circuito_ULD.to_csv("data/presidente/ULD/pres_ULD_circuito.csv", encoding="utf-8")

# Guardo ULD comuna
porc_pres_comuna_ULD.to_csv("data/presidente/ULD/pres_ULD_comuna.csv", encoding="utf-8")


#%%


# BLANCO

resultCABA_pres_BLANCO = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "BLANCO")]

resultCABA_pres_BLANCO.reset_index(inplace=True, drop=True)

# Porcentaje del BLANCO por circuito
porc_pres_circuito_BLANCO = porcentaje_circuito(resultCABA_pres_total, resultCABA_pres_BLANCO)


# Porcentaje del BLANCO por comuna
porc_pres_comuna_BLANCO = porcentaje_comuna(porc_pres_circuito_BLANCO)

# Cambio de nombres BLANCO circuito
porc_pres_circuito_BLANCO = porc_pres_circuito_BLANCO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_PRES",
                                                          "VOTOS_AGRUPACION": "VOTOS_BLANCO_PRES",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_BLANCO_PRES"})

# Cambio de nombres BLANCO comuna
porc_pres_comuna_BLANCO = porc_pres_comuna_BLANCO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_PRES",
                                                          "VOTOS_AGRUPACION": "VOTOS_BLANCO_PRES",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_BLANCO_PRES"})

# Guardo BLANCO circuito
porc_pres_circuito_BLANCO.to_csv("data/presidente/BLANCO/pres_BLANCO_circuito.csv", encoding="utf-8")

# Guardo BLANCO comuna
porc_pres_comuna_BLANCO.to_csv("data/presidente/BLANCO/pres_BLANCO_comuna.csv", encoding="utf-8")


#%%


# IMPUGNADO

resultCABA_pres_IMPUGNADO = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "IMPUGNADO")]

resultCABA_pres_IMPUGNADO.reset_index(inplace=True, drop=True)

# Porcentaje del IMPUGNADO por circuito
porc_pres_circuito_IMPUGNADO = porcentaje_circuito(resultCABA_pres_total, resultCABA_pres_IMPUGNADO)


# Porcentaje del IMPUGNADO por comuna
porc_pres_comuna_IMPUGNADO = porcentaje_comuna(porc_pres_circuito_IMPUGNADO)

# Cambio de nombres IMPUGNADO circuito
porc_pres_circuito_IMPUGNADO = porc_pres_circuito_IMPUGNADO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_PRES",
                                                          "VOTOS_AGRUPACION": "VOTOS_IMPUGNADO_PRES",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_IMPUGNADO_PRES"})

# Cambio de nombres IMPUGNADO comuna
porc_pres_comuna_IMPUGNADO = porc_pres_comuna_IMPUGNADO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_PRES",
                                                          "VOTOS_AGRUPACION": "VOTOS_IMPUGNADO_PRES",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_IMPUGNADO_PRES"})

# Guardo IMPUGNADO circuito
porc_pres_circuito_IMPUGNADO.to_csv("data/presidente/IMPUGNADO/pres_IMPUGNADO_circuito.csv", encoding="utf-8")

# Guardo IMPUGNADO comuna
porc_pres_comuna_IMPUGNADO.to_csv("data/presidente/IMPUGNADO/pres_IMPUGNADO_comuna.csv", encoding="utf-8")


#%%


# NULO

resultCABA_pres_NULO = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "NULO")]

resultCABA_pres_NULO.reset_index(inplace=True, drop=True)

# Porcentaje del NULO por circuito
porc_pres_circuito_NULO = porcentaje_circuito(resultCABA_pres_total, resultCABA_pres_NULO)


# Porcentaje del NULO por comuna
porc_pres_comuna_NULO = porcentaje_comuna(porc_pres_circuito_NULO)

# Cambio de nombres NULO circuito
porc_pres_circuito_NULO = porc_pres_circuito_NULO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_PRES",
                                                          "VOTOS_AGRUPACION": "VOTOS_NULO_PRES",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_NULO_PRES"})

# Cambio de nombres NULO comuna
porc_pres_comuna_NULO = porc_pres_comuna_NULO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_PRES",
                                                          "VOTOS_AGRUPACION": "VOTOS_NULO_PRES",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_NULO_PRES"})

# Guardo NULO circuito
porc_pres_circuito_NULO.to_csv("data/presidente/NULO/pres_NULO_circuito.csv", encoding="utf-8")

# Guardo NULO comuna
porc_pres_comuna_NULO.to_csv("data/presidente/NULO/pres_NULO_comuna.csv", encoding="utf-8")


#%%


# RECURRIDO

resultCABA_pres_RECURRIDO = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Presidente y Vicepresidente de la República") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "RECURRIDO")]

resultCABA_pres_RECURRIDO.reset_index(inplace=True, drop=True)

# Porcentaje del RECURRIDO por circuito
porc_pres_circuito_RECURRIDO = porcentaje_circuito(resultCABA_pres_total, resultCABA_pres_RECURRIDO)


# Porcentaje del RECURRIDO por comuna
porc_pres_comuna_RECURRIDO = porcentaje_comuna(porc_pres_circuito_RECURRIDO)

# Cambio de nombres RECURRIDO circuito
porc_pres_circuito_RECURRIDO = porc_pres_circuito_RECURRIDO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_PRES",
                                                          "VOTOS_AGRUPACION": "VOTOS_RECURRIDO_PRES",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_RECURRIDO_PRES"})

# Cambio de nombres RECURRIDO comuna
porc_pres_comuna_RECURRIDO = porc_pres_comuna_RECURRIDO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_PRES",
                                                          "VOTOS_AGRUPACION": "VOTOS_RECURRIDO_PRES",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_RECURRIDO_PRES"})

# Guardo RECURRIDO circuito
porc_pres_circuito_RECURRIDO.to_csv("data/presidente/RECURRIDO/pres_RECURRIDO_circuito.csv", encoding="utf-8")

# Guardo RECURRIDO comuna
porc_pres_comuna_RECURRIDO.to_csv("data/presidente/RECURRIDO/pres_RECURRIDO_comuna.csv", encoding="utf-8")


#%%

# DataFrame con porcentaje resultados presidenciales completo, circuito


porc_pres_circuito = pd.merge(left=porc_pres_circuito_FIT, right=porc_pres_circuito_CF, left_index=True, right_index=True, suffixes=('', '_1'))
porc_pres_circuito = pd.merge(left=porc_pres_circuito, right=porc_pres_circuito_FDT, left_index=True, right_index=True, suffixes=('', '_3'))
porc_pres_circuito = pd.merge(left=porc_pres_circuito, right=porc_pres_circuito_JXC, left_index=True, right_index=True, suffixes=('', '_5'))
porc_pres_circuito = pd.merge(left=porc_pres_circuito, right=porc_pres_circuito_NOS, left_index=True, right_index=True, suffixes=('', '_7'))
porc_pres_circuito = pd.merge(left=porc_pres_circuito, right=porc_pres_circuito_ULD, left_index=True, right_index=True, suffixes=('', '_9'))
porc_pres_circuito = pd.merge(left=porc_pres_circuito, right=porc_pres_circuito_NULO, left_index=True, right_index=True, suffixes=('', '_11'))
porc_pres_circuito = pd.merge(left=porc_pres_circuito, right=porc_pres_circuito_RECURRIDO, left_index=True, right_index=True, suffixes=('', '_13'))
porc_pres_circuito = pd.merge(left=porc_pres_circuito, right=porc_pres_circuito_IMPUGNADO, left_index=True, right_index=True, suffixes=('', '_15'))
porc_pres_circuito = pd.merge(left=porc_pres_circuito, right=porc_pres_circuito_BLANCO, left_index=True, right_index=True, suffixes=('', '_17'))

porc_pres_circuito.drop(['VOTOS_TOTALES_PRES_1', 'VOTOS_TOTALES_PRES_3', 'VOTOS_TOTALES_PRES_5', 'VOTOS_TOTALES_PRES_7',
                        'VOTOS_TOTALES_PRES_9', 'VOTOS_TOTALES_PRES_11', 'VOTOS_TOTALES_PRES_13',
                         'VOTOS_TOTALES_PRES_15', 'VOTOS_TOTALES_PRES_17'], axis=1, inplace=True)

porc_pres_circuito.to_csv("data/presidente/pres_circuito.csv", encoding="utf-8")


#%%

# Le agrego una columna al df con el porcentaje de voto de otras agrupaciones

porc_pres_circuito_OTROS = pd.read_csv("data/presidente/pres_circuito.csv")

lista_restos = pd.Series()

for n in range(0, 166):
    resto = porc_pres_circuito_OTROS.iloc[n, 2] - (porc_pres_circuito_OTROS.iloc[n, 3] +
                                                   porc_pres_circuito_OTROS.iloc[n, 5] +
                                                   porc_pres_circuito_OTROS.iloc[n, 7] +
                                                   porc_pres_circuito_OTROS.iloc[n, 9] +
                                                   porc_pres_circuito_OTROS.iloc[n, 11] +
                                                   porc_pres_circuito_OTROS.iloc[n, 13] +
                                                   porc_pres_circuito_OTROS.iloc[n, 15] +
                                                   porc_pres_circuito_OTROS.iloc[n, 17] +
                                                   porc_pres_circuito_OTROS.iloc[n, 19] +
                                                   porc_pres_circuito_OTROS.iloc[n, 21])
    resto = pd.Series(resto)
    lista_restos = lista_restos.append(resto, ignore_index=True)


porc_pres_circuito_OTROS['VOTOS_OTROS_PRES'] = lista_restos

porcentajes_OTROS = pd.Series()


for n in range(0, 166):
    porcentaje = ((porc_pres_circuito_OTROS.iloc[n, -1] / porc_pres_circuito_OTROS.iloc[n, 2] * 100).round(2))
    porcentaje = pd.Series(porcentaje)
    porcentajes_OTROS = porcentajes_OTROS.append(porcentaje, ignore_index=True)

porc_pres_circuito_OTROS['PORCENTAJE_OTROS_PRES'] = porcentajes_OTROS

porc_pres_circuito_OTROS.index = porc_pres_circuito_OTROS['NOMBRE_REGION']

porc_pres_circuito_OTROS.to_csv("data/presidente/pres_circuito_OTROS.csv", encoding="utf-8")



#%%



# DataFrame con porcentaje resultados presidenciales completo


porc_pres_comuna = pd.merge(left=porc_pres_comuna_FIT, right=porc_pres_comuna_CF, left_index=True, right_index=True, suffixes=('', '_1'))
porc_pres_comuna = pd.merge(left=porc_pres_comuna, right=porc_pres_comuna_FDT, left_index=True, right_index=True, suffixes=('', '_3'))
porc_pres_comuna = pd.merge(left=porc_pres_comuna, right=porc_pres_comuna_JXC, left_index=True, right_index=True, suffixes=('', '_5'))
porc_pres_comuna = pd.merge(left=porc_pres_comuna, right=porc_pres_comuna_NOS, left_index=True, right_index=True, suffixes=('', '_7'))
porc_pres_comuna = pd.merge(left=porc_pres_comuna, right=porc_pres_comuna_ULD, left_index=True, right_index=True, suffixes=('', '_9'))
porc_pres_comuna = pd.merge(left=porc_pres_comuna, right=porc_pres_comuna_NULO, left_index=True, right_index=True, suffixes=('', '_11'))
porc_pres_comuna = pd.merge(left=porc_pres_comuna, right=porc_pres_comuna_RECURRIDO, left_index=True, right_index=True, suffixes=('', '_13'))
porc_pres_comuna = pd.merge(left=porc_pres_comuna, right=porc_pres_comuna_IMPUGNADO, left_index=True, right_index=True, suffixes=('', '_15'))
porc_pres_comuna = pd.merge(left=porc_pres_comuna, right=porc_pres_comuna_BLANCO, left_index=True, right_index=True, suffixes=('', '_17'))

porc_pres_comuna.drop(['VOTOS_TOTALES_PRES_1', 'VOTOS_TOTALES_PRES_3', 'VOTOS_TOTALES_PRES_5', 'VOTOS_TOTALES_PRES_7',
                        'VOTOS_TOTALES_PRES_9', 'VOTOS_TOTALES_PRES_11', 'VOTOS_TOTALES_PRES_13',
                         'VOTOS_TOTALES_PRES_15', 'VOTOS_TOTALES_PRES_17'], axis=1, inplace=True)

porc_pres_comuna.to_csv("data/presidente/pres_comuna.csv", encoding="utf-8")


#%%

# Le agrego una columna al df con el porcentaje de voto de otras agrupaciones

porc_pres_comuna_OTROS = pd.read_csv("data/presidente/pres_comuna.csv")

lista_restos_comuna = pd.Series()

for n in range(0, 15):
    resto_comuna = porc_pres_comuna_OTROS.iloc[n, 1] - (porc_pres_comuna_OTROS.iloc[n, 2] +
                                                   porc_pres_comuna_OTROS.iloc[n, 4] +
                                                   porc_pres_comuna_OTROS.iloc[n, 6] +
                                                   porc_pres_comuna_OTROS.iloc[n, 8] +
                                                   porc_pres_comuna_OTROS.iloc[n, 10] +
                                                   porc_pres_comuna_OTROS.iloc[n, 12] +
                                                   porc_pres_comuna_OTROS.iloc[n, 14] +
                                                   porc_pres_comuna_OTROS.iloc[n, 16] +
                                                   porc_pres_comuna_OTROS.iloc[n, 18] +
                                                   porc_pres_comuna_OTROS.iloc[n, 20])
    resto_comuna = pd.Series(resto_comuna)
    lista_restos_comuna = lista_restos_comuna.append(resto_comuna, ignore_index=True)


porc_pres_comuna_OTROS['VOTOS_OTROS_PRES'] = lista_restos_comuna

porcentajes_OTROS_comuna = pd.Series()


for n in range(0, 15):
    porcentaje_comuna = ((porc_pres_comuna_OTROS.iloc[n, -1] / porc_pres_comuna_OTROS.iloc[n, 1] * 100).round(2))
    porcentaje_comuna = pd.Series(porcentaje_comuna)
    porcentajes_OTROS_comuna = porcentajes_OTROS.append(porcentaje_comuna, ignore_index=True)

porc_pres_comuna_OTROS['PORCENTAJE_OTROS_PRES'] = porcentajes_OTROS_comuna

porc_pres_comuna_OTROS.index = porc_pres_comuna_OTROS['NOMBRE_REGION']
porc_pres_comuna_OTROS.to_csv("data/presidente/pres_comuna_OTROS.csv", encoding="utf-8")