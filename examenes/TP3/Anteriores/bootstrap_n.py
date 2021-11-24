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


# Dada una muestra D=(X,Y) de tamaño n indexadas con un variable I = list(range(n))

# Repetir K veces el siguiente procedimiento:

# 1) Samplear con repetición de I un vector I*_k de tamaño n

# 2) Elegir las I*_k filas de D para generar un data set D*_k (de tamaño n)

# 3) Usar D*_k para calcular un modelo de regresión f al que llameremos M*_k

# 4) Extraer de M*_k los coeficientes del modelo al cual llamaremos b*_k

# Si quiero la distribución de los coeficientes:

# i) Calcular para cada coeficiente los cuantiles 0.025,0.25,0.5,0.75,0.9725 (en un mundo benigno, obtinese un intervalo de confianza de nivel alpha=0.95

# ii) Histograma de cada coeficiente

# Si quiero la distribución predictiva de y^pred dado un x_nuevo, entonces:


# i) itero sobre cada uno de los B*_K (cada uno de los b*_k valores)

# 	i.1) le aplico esos valores al modelo de regresión de f para predecir el valor de y^pred_k con

# 		y^pred_k = f( x_nuevo ; b*_k )

# ii) Calcular para cada y^pred dado x_new los cuantiles 0.025,0.25,0.5,0.75,0.9725 (en un mundo benigno, obtinese un intervalo de confianza de nivel alpha=0.95

# iii) Histograma de cada y^pred que me interese

# %%

class bootstrap_data:
    def __init__(self, x, y, k):
        self.x = x
        self.y = y
        self.k = k
        self.d = pd.DataFrame(list(zip(self.x, self.y)), columns=['x', 'y'])
        self.i = list(range(len(self.d)))
        """
         - Al llamar la clase, poner como argumentos dos listas
         - 'K' es la cantidad de repeticiones 
         - 'constante' es una variable booleana: Determina si la función le debe agregar constante o no
         - Construye un dataframe "D" con ambas listas, cuyas columnas se llaman 'x' e 'y'
         - Construye una lista "I" con el largo de "D"

        """

    def bootstrap(self):
        coef_df = pd.DataFrame({'constante': [], 'x1': []})

        for i in range(0, self.k):
            # Construye una nueva lista "Ik" a partir del sampleo con repeticiones de I
            Ik = np.random.choice(len(self.i), size=[len(self.i)], replace=True)

            # Construye un nuevo DataFrame "dk" a partir de seleccionar las filas de índice
            # que coinciden con "Ik"
            dk = self.d.iloc[Ik]

            # Covierte las columnas X e Y en listas, para poder agregarles la constane
            # y usarlas en statsmodels
            yk = dk['y'].tolist()
            xk = dk['x'].tolist()

            # Agrega la constante para calcular regresión
            xk = sm.add_constant(xk)

            # Calcula la regresión
            reg = sm.OLS(yk, xk).fit()

            #  coef = reg.params
            coef = reg.summary()
            coef_html = coef.tables[1].as_html()
            summary = pd.read_html(coef_html, header=0, index_col=0)[0]

            # FInalmente, agrega el valor del coeficiente al DataFrame final
            coef_df.loc[len(coef_df), 'constante'] = summary.iloc[0, 0]
            coef_df.loc[len(coef_df) - 1, 'x1'] = summary.iloc[-1, 0]

            # Pasa la tabla de resumen a un html solo para poder agarrar el coeficiente
            # y agregarlo al DF vacío
            # Debería haber una manera más rápida de poder hacer esto, sin tener que pasar a html, pero no la encontré

        cuantiles_c = coef_df[['constante']].quantile([0.025, 0.25, 0.5, 0.75, 0.975])
        cuantiles_x1 = coef_df[['x1']].quantile([0.025, 0.25, 0.5, 0.75, 0.975])
        cuantiles = pd.merge(cuantiles_c, cuantiles_x1, left_index=True, right_index=True)

        fig, axes = plt.subplots(1, 2, sharey=True, figsize=(12, 7))
        sns.histplot(coef_df['constante'], color='blue', ax=axes[0])
        sns.histplot(coef_df['x1'], color='red', ax=axes[1])

        return cuantiles


# %% [markdown]
#### Ejemplos
# Me fijo si la variable 'weight' puede predecir la variable 'price' del dataset 'autos
# %%
# Ejemplo 1
auto = pd.read_csv('auto.csv')
ax = auto['weight'].tolist()
ay = auto['price'].tolist()

ejemploautos = bootstrap_data(ax, ay, 10000)
ejemploautos.bootstrap()

# %%
# Ejemplo 2
auto = pd.read_csv('auto.csv')
ax = auto['weight'].tolist()
ay = auto['price'].tolist()
al = [1] * len(ax)
al
ejemploautos = bootstrap_data(ax, ay, 100, al)
ejemploautos.bootstrap()
# %%
# Me gustaría poder darle un valor por defecto a 'constante', para que no sea necesario ponerlo