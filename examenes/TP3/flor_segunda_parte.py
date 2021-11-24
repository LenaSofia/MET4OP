# -*- coding: utf-8 -*-
"""flor_segunda_parte.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tppaWgaGkkV4vcVDqFeuw66kqZLxrTOx
"""

# Commented out IPython magic to ensure Python compatibility.
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
# %matplotlib inline

"""Dada una muestra D=(X,Y) de tamaño n indexadas con un variable I = list(range(n))  

Repetir K veces el siguiente procedimiento:

1) Samplear con repetición de I un vector I*_k de tamaño n

2) Elegir las I*_k filas de D para generar un data set D*_k (de tamaño n)

3) Usar D*_k para calcular un modelo de regresión f al que llameremos M*_k

4) Extraer de M*_k los coeficientes del modelo al cual llamaremos b*_k

Si quiero la distribución de los coeficientes:

i) Calcular para cada coeficiente los cuantiles 0.025,0.25,0.5,0.75,0.9725 (en un mundo benigno, obtinese un intervalo de confianza de nivel alpha=0.95

ii) Histograma de cada coeficiente


"""

def armar_DF(x, y):

    data_frame = pd.DataFrame(list(zip(x, y)), columns=['x', 'y'])
    # data_frame = data_frame.assign(indice="")

    return data_frame

def generar_bootstrap(DF, repeticiones):

    DF_coeficientes = pd.DataFrame()

    for repeticion in range(0, repeticiones):
        # Construye una nueva lista "DF_sampleado" a partir del sampleo con repeticiones de DF
        DF_sampleado = DF.sample(n=len(DF), replace=True, random_state=None, axis=0,
                                 ignore_index=False)

        # Agrega la constante para calcular regresión
        DF_sampleado = sm.add_constant(DF_sampleado)

        # Calcula la regresión
        reg = sm.OLS(DF_sampleado["y"], DF_sampleado[["x", "const"]]).fit()
        # El de arriba tengo que revisarlo, parecería que me lo toma bien porque imprime que cada vez
        # que x aumenta 1, y aumenta 2 (si no entiendo mal), si lo invierto me aparece y 0.5 (que también tiene sentido)

        coef = reg.params
        coef_DF = coef.to_frame()
        coef_DF = coef_DF.transpose()

        # Agrego el DF del coeficiente actual al DF final
        DF_coeficientes = DF_coeficientes.append(coef_DF, ignore_index=True)


    return reg

def sacar_cuantiles(DF_coeficientes):

    cuantiles_const = DF_coeficientes[['const']].quantile([0.025, 0.25, 0.5, 0.75, 0.975])
    cuantiles_x1 = DF_coeficientes[['x']].quantile([0.025, 0.25, 0.5, 0.75, 0.975])
    cuantiles = pd.merge(cuantiles_const, cuantiles_x1, left_index=True, right_index=True)
    return cuantiles

def hacer_graficos(DF_coeficientes):
    fig, axes = plt.subplots(1, 2, sharey=True, squeeze=True, figsize=(12, 7))
    sns.histplot(DF_coeficientes['const'], color='blue', ax=axes[0])
    sns.histplot(DF_coeficientes['x'], color='red', ax=axes[1])
    plt.show()

"""Si quiero la distribución predictiva de y^pred dado un x_nuevo, entonces:


i) itero sobre cada uno de los B*_K (cada uno de los b*_k valores)

i.1) le aplico esos valores al modelo de regresión de f para predecir el valor de y^pred_k con

y^pred_k = f( x_nuevo ; b*_k )
		
ii) Calcular para cada y^pred dado x_new los cuantiles 0.025,0.25,0.5,0.75,0.9725 (en un mundo benigno, obtinese un intervalo de confianza de nivel alpha=0.95

iii) Histograma de cada y^pred que me interese
"""

def y_predicho(X=3, repeticiones):
  
  DF_y_pred = pd.DataFrame()
  
  for i in range(0, repeticiones):
  y_pred = (DF_coeficientes["const"] + DF_coeficientes["x"] * "X")

def sacar_cuantiles(DF_y_pred):

    cuantiles_y_pred = DF_y_pred[['y_pred']].quantile([0.025, 0.25, 0.5, 0.75, 0.975])

def hacer_graficos(DF_y_pred):
  sns.histplot(DF_coeficientes['y_pred'], color='green', ax=axes[1])
    plt.show()