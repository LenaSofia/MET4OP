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

resultCABA_Com14_total = resultCABA[resultCABA["NOMBRE_CATEGORIA"] == "Junta Comunal Ciudad Autónoma de Buenos Aires - Comuna 14"]

resultCABA_Com14_total.reset_index(inplace=True, drop=True)


#%%


#FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD:

resultCABA_Com14_FIT = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Junta Comunal Ciudad Autónoma de Buenos Aires - Comuna 14") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD")]

resultCABA_Com14_FIT.reset_index(inplace=True, drop=True)

# Porcentaje del FIT por circuito
porc_Com14_circuito_FIT = porcentaje_circuito(resultCABA_Com14_total, resultCABA_Com14_FIT)


# Porcentaje del FIT por comuna
porc_Com14_comuna_FIT = porcentaje_comuna(porc_Com14_circuito_FIT)

# Cambio de nombres FIT circuito
porc_Com14_circuito_FIT = porc_Com14_circuito_FIT.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_COM14",
                                                          "VOTOS_AGRUPACION": "VOTOS_FIT_COM14",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_FIT_COM14"})

# Cambio de nombres FIT comuna
porc_Com14_comuna_FIT = porc_Com14_comuna_FIT.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_COM14",
                                                          "VOTOS_AGRUPACION": "VOTOS_FIT_COM14",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_FIT_COM14"})

# Guardo FIT circuito
porc_Com14_circuito_FIT.to_csv("data/comuna_14/FIT/Com14_FIT_circuito.csv", encoding="utf-8")

# Guardo FIT comuna
porc_Com14_comuna_FIT.to_csv("data/comuna_14/FIT/Com14_FIT_comuna.csv", encoding="utf-8")


#%%


# FRENTE NOS

resultCABA_Com14_NOS = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Junta Comunal Ciudad Autónoma de Buenos Aires - Comuna 14") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "FRENTE NOS")]

resultCABA_Com14_NOS.reset_index(inplace=True, drop=True)

# Porcentaje del NOS por circuito
porc_Com14_circuito_NOS = porcentaje_circuito(resultCABA_Com14_total, resultCABA_Com14_NOS)


# Porcentaje del NOS por comuna
porc_Com14_comuna_NOS = porcentaje_comuna(porc_Com14_circuito_NOS)

# Cambio de nombres NOS circuito
porc_Com14_circuito_NOS = porc_Com14_circuito_NOS.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_COM14",
                                                          "VOTOS_AGRUPACION": "VOTOS_NOS_COM14",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_NOS_COM14"})

# Cambio de nombres NOS comuna
porc_Com14_comuna_NOS = porc_Com14_comuna_NOS.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_COM14",
                                                          "VOTOS_AGRUPACION": "VOTOS_NOS_COM14",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_NOS_COM14"})

# Guardo NOS circuito
porc_Com14_circuito_NOS.to_csv("data/comuna_14/NOS/Com14_NOS_circuito.csv", encoding="utf-8")

# Guardo NOS comuna
porc_Com14_comuna_NOS.to_csv("data/comuna_14/NOS/Com14_NOS_comuna.csv", encoding="utf-8")


#%%


# JUNTOS POR EL CAMBIO

resultCABA_Com14_JXC = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Junta Comunal Ciudad Autónoma de Buenos Aires - Comuna 14") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "JUNTOS POR EL CAMBIO")]

resultCABA_Com14_JXC.reset_index(inplace=True, drop=True)

# Porcentaje del JXC por circuito
porc_Com14_circuito_JXC = porcentaje_circuito(resultCABA_Com14_total, resultCABA_Com14_JXC)


# Porcentaje del JXC por comuna
porc_Com14_comuna_JXC = porcentaje_comuna(porc_Com14_circuito_JXC)

# Cambio de nombres JXC circuito
porc_Com14_circuito_JXC = porc_Com14_circuito_JXC.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_COM14",
                                                          "VOTOS_AGRUPACION": "VOTOS_JXC_COM14",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_JXC_COM14"})

# Cambio de nombres JXC comuna
porc_Com14_comuna_JXC = porc_Com14_comuna_JXC.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_COM14",
                                                          "VOTOS_AGRUPACION": "VOTOS_JXC_COM14",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_JXC_COM14"})

# Guardo JXC circuito
porc_Com14_circuito_JXC.to_csv("data/comuna_14/JXC/Com14_JXC_circuito.csv", encoding="utf-8")

# Guardo JXC comuna
porc_Com14_comuna_JXC.to_csv("data/comuna_14/JXC/Com14_JXC_comuna.csv", encoding="utf-8")


#%%


# FRENTE DE TODOS

resultCABA_Com14_FDT = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Junta Comunal Ciudad Autónoma de Buenos Aires - Comuna 14") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "FRENTE DE TODOS")]

resultCABA_Com14_FDT.reset_index(inplace=True, drop=True)

# Porcentaje del FDT por circuito
porc_Com14_circuito_FDT = porcentaje_circuito(resultCABA_Com14_total, resultCABA_Com14_FDT)


# Porcentaje del FDT por comuna
porc_Com14_comuna_FDT = porcentaje_comuna(porc_Com14_circuito_FDT)

# Cambio de nombres FDT circuito
porc_Com14_circuito_FDT = porc_Com14_circuito_FDT.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_COM14",
                                                          "VOTOS_AGRUPACION": "VOTOS_FDT_COM14",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_FDT_COM14"})

# Cambio de nombres FDT comuna
porc_Com14_comuna_FDT = porc_Com14_comuna_FDT.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_COM14",
                                                          "VOTOS_AGRUPACION": "VOTOS_FDT_COM14",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_FDT_COM14"})

# Guardo FDT circuito
porc_Com14_circuito_FDT.to_csv("data/comuna_14/FDT/Com14_FDT_circuito.csv", encoding="utf-8")

# Guardo FDT comuna
porc_Com14_comuna_FDT.to_csv("data/comuna_14/FDT/Com14_FDT_comuna.csv", encoding="utf-8")


#%%


# CONSENSO FEDERAL

resultCABA_Com14_CF = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Junta Comunal Ciudad Autónoma de Buenos Aires - Comuna 14") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "CONSENSO FEDERAL")]

resultCABA_Com14_CF.reset_index(inplace=True, drop=True)

# Porcentaje del CF por circuito
porc_Com14_circuito_CF = porcentaje_circuito(resultCABA_Com14_total, resultCABA_Com14_CF)


# Porcentaje del CF por comuna
porc_Com14_comuna_CF = porcentaje_comuna(porc_Com14_circuito_CF)

# Cambio de nombres CF circuito
porc_Com14_circuito_CF = porc_Com14_circuito_CF.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_COM14",
                                                          "VOTOS_AGRUPACION": "VOTOS_CF_COM14",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_CF_COM14"})

# Cambio de nombres CF comuna
porc_Com14_comuna_CF = porc_Com14_comuna_CF.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_COM14",
                                                          "VOTOS_AGRUPACION": "VOTOS_CF_COM14",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_CF_COM14"})

# Guardo CF circuito
porc_Com14_circuito_CF.to_csv("data/comuna_14/CF/Com14_CF_circuito.csv", encoding="utf-8")

# Guardo CF comuna
porc_Com14_comuna_CF.to_csv("data/comuna_14/CF/Com14_CF_comuna.csv", encoding="utf-8")


#%%


# UNITE POR LA LIBERTAD Y LA DIGNIDAD

resultCABA_Com14_ULD = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Junta Comunal Ciudad Autónoma de Buenos Aires - Comuna 14") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "UNITE POR LA LIBERTAD Y LA DIGNIDAD")]

resultCABA_Com14_ULD.reset_index(inplace=True, drop=True)

# Porcentaje del ULD por circuito
porc_Com14_circuito_ULD = porcentaje_circuito(resultCABA_Com14_total, resultCABA_Com14_ULD)


# Porcentaje del ULD por comuna
porc_Com14_comuna_ULD = porcentaje_comuna(porc_Com14_circuito_ULD)

# Cambio de nombres ULD circuito
porc_Com14_circuito_ULD = porc_Com14_circuito_ULD.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_COM14",
                                                          "VOTOS_AGRUPACION": "VOTOS_ULD_COM14",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_ULD_COM14"})

# Cambio de nombres ULD comuna
porc_Com14_comuna_ULD = porc_Com14_comuna_ULD.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_COM14",
                                                          "VOTOS_AGRUPACION": "VOTOS_ULD_COM14",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_ULD_COM14"})

# Guardo ULD circuito
porc_Com14_circuito_ULD.to_csv("data/comuna_14/ULD/Com14_ULD_circuito.csv", encoding="utf-8")

# Guardo ULD comuna
porc_Com14_comuna_ULD.to_csv("data/comuna_14/ULD/Com14_ULD_comuna.csv", encoding="utf-8")


#%%


# BLANCO

resultCABA_Com14_BLANCO = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Junta Comunal Ciudad Autónoma de Buenos Aires - Comuna 14") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "BLANCO")]

resultCABA_Com14_BLANCO.reset_index(inplace=True, drop=True)

# Porcentaje del BLANCO por circuito
porc_Com14_circuito_BLANCO = porcentaje_circuito(resultCABA_Com14_total, resultCABA_Com14_BLANCO)


# Porcentaje del BLANCO por comuna
porc_Com14_comuna_BLANCO = porcentaje_comuna(porc_Com14_circuito_BLANCO)

# Cambio de nombres BLANCO circuito
porc_Com14_circuito_BLANCO = porc_Com14_circuito_BLANCO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_COM14",
                                                          "VOTOS_AGRUPACION": "VOTOS_BLANCO_COM14",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_BLANCO_COM14"})

# Cambio de nombres BLANCO comuna
porc_Com14_comuna_BLANCO = porc_Com14_comuna_BLANCO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_COM14",
                                                          "VOTOS_AGRUPACION": "VOTOS_BLANCO_COM14",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_BLANCO_COM14"})

# Guardo BLANCO circuito
porc_Com14_circuito_BLANCO.to_csv("data/comuna_14/BLANCO/Com14_BLANCO_circuito.csv", encoding="utf-8")

# Guardo BLANCO comuna
porc_Com14_comuna_BLANCO.to_csv("data/comuna_14/BLANCO/Com14_BLANCO_comuna.csv", encoding="utf-8")


#%%


# IMPUGNADO

resultCABA_Com14_IMPUGNADO = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Junta Comunal Ciudad Autónoma de Buenos Aires - Comuna 14") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "IMPUGNADO")]

resultCABA_Com14_IMPUGNADO.reset_index(inplace=True, drop=True)

# Porcentaje del IMPUGNADO por circuito
porc_Com14_circuito_IMPUGNADO = porcentaje_circuito(resultCABA_Com14_total, resultCABA_Com14_IMPUGNADO)


# Porcentaje del IMPUGNADO por comuna
porc_Com14_comuna_IMPUGNADO = porcentaje_comuna(porc_Com14_circuito_IMPUGNADO)

# Cambio de nombres IMPUGNADO circuito
porc_Com14_circuito_IMPUGNADO = porc_Com14_circuito_IMPUGNADO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_COM14",
                                                          "VOTOS_AGRUPACION": "VOTOS_IMPUGNADO_COM14",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_IMPUGNADO_COM14"})

# Cambio de nombres IMPUGNADO comuna
porc_Com14_comuna_IMPUGNADO = porc_Com14_comuna_IMPUGNADO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_COM14",
                                                          "VOTOS_AGRUPACION": "VOTOS_IMPUGNADO_COM14",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_IMPUGNADO_COM14"})

# Guardo IMPUGNADO circuito
porc_Com14_circuito_IMPUGNADO.to_csv("data/comuna_14/IMPUGNADO/Com14_IMPUGNADO_circuito.csv", encoding="utf-8")

# Guardo IMPUGNADO comuna
porc_Com14_comuna_IMPUGNADO.to_csv("data/comuna_14/IMPUGNADO/Com14_IMPUGNADO_comuna.csv", encoding="utf-8")


#%%


# NULO

resultCABA_Com14_NULO = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Junta Comunal Ciudad Autónoma de Buenos Aires - Comuna 14") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "NULO")]

resultCABA_Com14_NULO.reset_index(inplace=True, drop=True)

# Porcentaje del NULO por circuito
porc_Com14_circuito_NULO = porcentaje_circuito(resultCABA_Com14_total, resultCABA_Com14_NULO)


# Porcentaje del NULO por comuna
porc_Com14_comuna_NULO = porcentaje_comuna(porc_Com14_circuito_NULO)

# Cambio de nombres NULO circuito
porc_Com14_circuito_NULO = porc_Com14_circuito_NULO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_COM14",
                                                          "VOTOS_AGRUPACION": "VOTOS_NULO_COM14",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_NULO_COM14"})

# Cambio de nombres NULO comuna
porc_Com14_comuna_NULO = porc_Com14_comuna_NULO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_COM14",
                                                          "VOTOS_AGRUPACION": "VOTOS_NULO_COM14",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_NULO_COM14"})

# Guardo NULO circuito
porc_Com14_circuito_NULO.to_csv("data/comuna_14/NULO/Com14_NULO_circuito.csv", encoding="utf-8")

# Guardo NULO comuna
porc_Com14_comuna_NULO.to_csv("data/comuna_14/NULO/Com14_NULO_comuna.csv", encoding="utf-8")


#%%


# RECURRIDO

resultCABA_Com14_RECURRIDO = resultCABA[(resultCABA["NOMBRE_CATEGORIA"] == "Junta Comunal Ciudad Autónoma de Buenos Aires - Comuna 14") &
                                 (resultCABA["NOMBRE_AGRUPACION"] == "RECURRIDO")]

resultCABA_Com14_RECURRIDO.reset_index(inplace=True, drop=True)

# Porcentaje del RECURRIDO por circuito
porc_Com14_circuito_RECURRIDO = porcentaje_circuito(resultCABA_Com14_total, resultCABA_Com14_RECURRIDO)


# Porcentaje del RECURRIDO por comuna
porc_Com14_comuna_RECURRIDO = porcentaje_comuna(porc_Com14_circuito_RECURRIDO)

# Cambio de nombres RECURRIDO circuito
porc_Com14_circuito_RECURRIDO = porc_Com14_circuito_RECURRIDO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_COM14",
                                                          "VOTOS_AGRUPACION": "VOTOS_RECURRIDO_COM14",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_RECURRIDO_COM14"})

# Cambio de nombres RECURRIDO comuna
porc_Com14_comuna_RECURRIDO = porc_Com14_comuna_RECURRIDO.rename(columns={"VOTOS_TOTALES": "VOTOS_TOTALES_COM14",
                                                          "VOTOS_AGRUPACION": "VOTOS_RECURRIDO_COM14",
                                                          "PORCENTAJE_AGRUPACION": "PORCENTAJE_RECURRIDO_COM14"})

# Guardo RECURRIDO circuito
porc_Com14_circuito_RECURRIDO.to_csv("data/comuna_14/RECURRIDO/Com14_RECURRIDO_circuito.csv", encoding="utf-8")

# Guardo RECURRIDO comuna
porc_Com14_comuna_RECURRIDO.to_csv("data/comuna_14/RECURRIDO/Com14_RECURRIDO_comuna.csv", encoding="utf-8")


#%%

# DataFrame con porcentaje resultados comuna 14 completo, circuito


porc_Com14_circuito = pd.merge(left=porc_Com14_circuito_FIT, right=porc_Com14_circuito_CF, left_index=True, right_index=True, suffixes=('', '_1'))
porc_Com14_circuito = pd.merge(left=porc_Com14_circuito, right=porc_Com14_circuito_FDT, left_index=True, right_index=True, suffixes=('', '_3'))
porc_Com14_circuito = pd.merge(left=porc_Com14_circuito, right=porc_Com14_circuito_JXC, left_index=True, right_index=True, suffixes=('', '_5'))
porc_Com14_circuito = pd.merge(left=porc_Com14_circuito, right=porc_Com14_circuito_NULO, left_index=True, right_index=True, suffixes=('', '_11'))
porc_Com14_circuito = pd.merge(left=porc_Com14_circuito, right=porc_Com14_circuito_RECURRIDO, left_index=True, right_index=True, suffixes=('', '_13'))
porc_Com14_circuito = pd.merge(left=porc_Com14_circuito, right=porc_Com14_circuito_IMPUGNADO, left_index=True, right_index=True, suffixes=('', '_15'))
porc_Com14_circuito = pd.merge(left=porc_Com14_circuito, right=porc_Com14_circuito_BLANCO, left_index=True, right_index=True, suffixes=('', '_17'))

porc_Com14_circuito.drop(['VOTOS_TOTALES_COM14_1', 'VOTOS_TOTALES_COM14_3', 'VOTOS_TOTALES_COM14_5',
                         'VOTOS_TOTALES_COM14_11', 'VOTOS_TOTALES_COM14_13',
                         'VOTOS_TOTALES_COM14_15', 'VOTOS_TOTALES_COM14_17'], axis=1, inplace=True)

porc_Com14_circuito.to_csv("data/comuna_14/Com14_circuito.csv", encoding="utf-8")


#%%

# Le agrego una columna al df con el porcentaje de voto de otras agrupaciones

porc_Com14_circuito_OTROS = pd.read_csv("data/comuna_14/Com14_circuito.csv")

lista_restos = pd.Series()

for n in range(0, 10):
    resto = porc_Com14_circuito_OTROS.iloc[n, 2] - (porc_Com14_circuito_OTROS.iloc[n, 3] +
                                                   porc_Com14_circuito_OTROS.iloc[n, 5] +
                                                   porc_Com14_circuito_OTROS.iloc[n, 7] +
                                                   porc_Com14_circuito_OTROS.iloc[n, 9] +
                                                   porc_Com14_circuito_OTROS.iloc[n, 11] +
                                                   porc_Com14_circuito_OTROS.iloc[n, 13] +
                                                   porc_Com14_circuito_OTROS.iloc[n, 15] +
                                                   porc_Com14_circuito_OTROS.iloc[n, 17])
    resto = pd.Series(resto)
    lista_restos = lista_restos.append(resto, ignore_index=True)


porc_Com14_circuito_OTROS['VOTOS_OTROS_COM14'] = lista_restos

porcentajes_OTROS = pd.Series()


for n in range(0, 10):
    porcentaje = ((porc_Com14_circuito_OTROS.iloc[n, -1] / porc_Com14_circuito_OTROS.iloc[n, 2] * 100).round(2))
    porcentaje = pd.Series(porcentaje)
    porcentajes_OTROS = porcentajes_OTROS.append(porcentaje, ignore_index=True)

porc_Com14_circuito_OTROS['PORCENTAJE_OTROS_COM14'] = porcentajes_OTROS

porc_Com14_circuito_OTROS.index = porc_Com14_circuito_OTROS['NOMBRE_REGION']

porc_Com14_circuito_OTROS.drop(["NOMBRE_REGION"], axis=1, inplace=True)

porc_Com14_circuito_OTROS.to_csv("data/comuna_14/Com14_circuito_completo.csv", encoding="utf-8")



#%%



# DataFrame con porcentaje resultados comuna 14 completo, por comuna


porc_Com14_comuna = pd.merge(left=porc_Com14_comuna_FIT, right=porc_Com14_comuna_CF, left_index=True, right_index=True, suffixes=('', '_1'))
porc_Com14_comuna = pd.merge(left=porc_Com14_comuna, right=porc_Com14_comuna_FDT, left_index=True, right_index=True, suffixes=('', '_3'))
porc_Com14_comuna = pd.merge(left=porc_Com14_comuna, right=porc_Com14_comuna_JXC, left_index=True, right_index=True, suffixes=('', '_5'))
porc_Com14_comuna = pd.merge(left=porc_Com14_comuna, right=porc_Com14_comuna_NULO, left_index=True, right_index=True, suffixes=('', '_11'))
porc_Com14_comuna = pd.merge(left=porc_Com14_comuna, right=porc_Com14_comuna_RECURRIDO, left_index=True, right_index=True, suffixes=('', '_13'))
porc_Com14_comuna = pd.merge(left=porc_Com14_comuna, right=porc_Com14_comuna_IMPUGNADO, left_index=True, right_index=True, suffixes=('', '_15'))
porc_Com14_comuna = pd.merge(left=porc_Com14_comuna, right=porc_Com14_comuna_BLANCO, left_index=True, right_index=True, suffixes=('', '_17'))

porc_Com14_comuna.drop(['VOTOS_TOTALES_COM14_1', 'VOTOS_TOTALES_COM14_3', 'VOTOS_TOTALES_COM14_5',
                         'VOTOS_TOTALES_COM14_11', 'VOTOS_TOTALES_COM14_13',
                         'VOTOS_TOTALES_COM14_15', 'VOTOS_TOTALES_COM14_17'], axis=1, inplace=True)

porc_Com14_comuna.to_csv("data/comuna_14/Com14_comuna.csv", encoding="utf-8")


#%%

# Le agrego una columna al df con el porcentaje de voto de otras agrupaciones por comuna

porc_Com14_comuna_OTROS = pd.read_csv("data/comuna_14/Com14_comuna.csv")

lista_restos_comuna = pd.Series()

for n in range(0, 1):
    resto_comuna = porc_Com14_comuna_OTROS.iloc[n, 1] - (porc_Com14_comuna_OTROS.iloc[n, 2] +
                                                   porc_Com14_comuna_OTROS.iloc[n, 4] +
                                                   porc_Com14_comuna_OTROS.iloc[n, 6] +
                                                   porc_Com14_comuna_OTROS.iloc[n, 8] +
                                                   porc_Com14_comuna_OTROS.iloc[n, 10] +
                                                   porc_Com14_comuna_OTROS.iloc[n, 12] +
                                                   porc_Com14_comuna_OTROS.iloc[n, 14] +
                                                   porc_Com14_comuna_OTROS.iloc[n, 16])
    resto_comuna = pd.Series(resto_comuna)
    lista_restos_comuna = lista_restos_comuna.append(resto_comuna, ignore_index=True)


porc_Com14_comuna_OTROS['VOTOS_OTROS_COM14'] = lista_restos_comuna

porcentajes_OTROS_comuna = pd.Series()


for n in range(0, 1):
    porcentaje_comuna = ((porc_Com14_comuna_OTROS.iloc[n, -1] / porc_Com14_comuna_OTROS.iloc[n, 1] * 100).round(2))
    porcentaje_comuna = pd.Series(porcentaje_comuna)
    porcentajes_OTROS_comuna = porcentajes_OTROS.append(porcentaje_comuna, ignore_index=True)

porc_Com14_comuna_OTROS['PORCENTAJE_OTROS_COM14'] = porcentajes_OTROS_comuna

porc_Com14_comuna_OTROS.index = porc_Com14_comuna_OTROS['NOMBRE_REGION']
porc_Com14_comuna_OTROS.drop(["NOMBRE_REGION"], axis=1, inplace=True)
porc_Com14_comuna_OTROS.to_csv("data/comuna_14/Com14_comuna_completo.csv", encoding="utf-8")