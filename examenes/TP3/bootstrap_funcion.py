# %%
from os import replace
import numpy as np
import pandas as pd
from numpy import fabs, random
from patsy import dmatrix, dmatrices
from statsmodels.formula.api import ols
import statsmodels.api as sm
import os
import seaborn as sns
import matplotlib.pyplot as plt

#%%

# Definimos las funciones:

# %%

def armar_DF(x, y):
    data_frame = pd.DataFrame(list(zip(x, y)), columns=['x', 'y'])
    return data_frame

#%%

def generar_bootstrap(DF, repeticiones):

    DF_coeficientes = pd.DataFrame()

    for repeticion in range(0, repeticiones):
        # Construye una nueva lista "DF_sampleado" a partir del sampleo con repeticiones de DF
        DF_sampleado = DF.sample(n=len(DF), replace=True, random_state=None, axis=0,
                                 ignore_index=False)

        # Agrega la constante para calcular regresión
        DF_sampleado = sm.add_constant(DF_sampleado)

        reg = sm.OLS(DF_sampleado["y"], DF_sampleado[["x", "const"]]).fit()

        coef = reg.params
        coef_DF = coef.to_frame()
        coef_DF = coef_DF.transpose()

        # Agrego el DF del coeficiente actual al DF final
        DF_coeficientes = DF_coeficientes.append(coef_DF, ignore_index=True)

    DF_coeficientes = DF_coeficientes.rename(columns={'x': 'coef_x',
                                                    'const': 'coef_const'})

    return DF_coeficientes

#%%

def sacar_cuantiles(*args):

    cuantiles = pd.DataFrame()

    for argumento in args:
        cuantiles[argumento.columns] = argumento.quantile([0.025, 0.25, 0.5, 0.75, 0.975])

    return cuantiles

#%%

def hacer_graficos(*args):

    indice = 0
    fig, axes = plt.subplots(1, 2, sharey=True, squeeze=True, figsize=(12, 7))
    for argumento in args:
        sns.histplot(argumento, ax=axes[indice])
        indice += 1

    plt.show()

#%%

# Predicción del 'y' a partir de un 'nuevo x':

def predecir_y_nuevo(x_nuevo, DF_coeficientes):

    DF_y_predichos = DF_coeficientes.copy(deep=True)

    DF_y_predichos = DF_y_predichos.assign(x_nuevo=x_nuevo, y_predicho="")


    for fila in range(0, len(DF_y_predichos)):
        DF_y_predichos.loc[DF_y_predichos.index.get_loc(fila), "y_predicho"] = \
            DF_y_predichos.loc[DF_y_predichos.index.get_loc(fila), "coef_const"] \
            + (DF_y_predichos.loc[DF_y_predichos.index.get_loc(fila), "coef_x"]
               * DF_y_predichos.loc[DF_y_predichos.index.get_loc(fila), "x_nuevo"])

    DF_y_predichos["y_predicho"] = DF_y_predichos.y_predicho.astype(float)

    return DF_y_predichos


#%%

# Funciones agrupadas:

def encontrar_coeficientes(x, y, repeticiones):

    DataFrame = armar_DF(x, y)
    DF_bootstrap_coef = generar_bootstrap(DataFrame, repeticiones)

    return DF_bootstrap_coef


def analizar_resultados(*args):

    cuantiles = sacar_cuantiles(*args)
    graficos = hacer_graficos(*args)

    return cuantiles

#%%


#Prueba reducida:

auto = pd.read_csv('Anteriores/auto.csv')
x = auto['weight'].tolist()
y = auto['price'].tolist()

DF_coeficientes_variacion = encontrar_coeficientes(x, y, 10000)

analisis_coeficientes = analizar_resultados(DF_coeficientes_variacion[['coef_x']], DF_coeficientes_variacion[['coef_const']])

DF_y_predicho = predecir_y_nuevo(5432, DF_coeficientes_variacion)

analisis_y_predicho = analizar_resultados(DF_y_predicho[['coef_x']], DF_y_predicho[['y_predicho']])
