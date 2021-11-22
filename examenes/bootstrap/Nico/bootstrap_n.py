#%%
from os import replace
import numpy as np
import pandas as pd
from numpy import random
from patsy import dmatrix, dmatrices
from statsmodels.formula.api import ols
import statsmodels.api as sm
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

#%%

class bootstrap_data:
    def __init__(self, x, y, k, constante):
        self.x = x
        self.y = y
        self.k = k
        self.d = pd.DataFrame(list(zip(self.x, self.y)), columns =['x', 'y'])
        self.i = list(range(len(self.d)))
        self.constante = constante
        """
         - Al llamar la clase, poner como argumentos dos listas
         - 'K' es la cantidad de repeticiones 
         - 'constante' es una variable booleana: Determina si la función le debe agregar constante o no
         - Construye un dataframe "D" con ambas listas, cuyas columnas se llaman 'x' e 'y'
         - Construye una lista "I" con el largo de "D"

        """

    def bootstrap(self):
        
        coef_df = pd.DataFrame({'coeficientes': []})
             

        for i in range(0, self.k):
            # Construye una nueva lista "Ik" a partir del sampleo con repeticiones de I
            Ik = np.random.choice(len(self.i), size = [len(self.i)], replace= True)

            # Construye un nuevo DataFrame "dk" a partir de seleccionar las filas de índice
            # que coinciden con "Ik"
            dk = self.d.iloc[Ik]
            
            if self.constante == False:
                # Covierte las columnas X e Y en listas, para poder agregarles la constane 
                # y usarlas en statsmodels
                yk = dk['y'].tolist()
                xk = dk['x'].tolist()

                # Agrega la constante para calcular regresión
                xk = sm.add_constant(xk)

                # Calcula la regresión
                reg = sm.OLS(yk,xk).fit()
            
            elif self.constante == True:

                reg = sm.OLS(dk['y'], dk['x']).fit()
            
            # Pasa la tabla de resumen a un html solo para poder agarrar el coeficiente
            # y agregarlo al DF vacío
            # Debería haber una manera más rápida de poder hacer esto, sin tener que pasar a html, pero no la encontré
        
            coef = reg.summary()
            coef_html = coef.tables[1].as_html()
            summary = pd.read_html(coef_html, header=0, index_col=0)[0]

            # FInalmente, agrega el valor del coeficiente al DataFrame final
            coef_df.loc[len(coef_df)] = summary.iloc[-1,0]
            
        return coef_df
        

#%% [markdown]
#### Ejemplo
# Utilizo las variables EDADQUI y P12 (Usa o no computadora) del censo 
# %%
persona = pd.read_csv('persona.csv')
px = persona['EDADQUI'].tolist()
py = persona['P12'].tolist()

# %%
# DIccionarios de etiquetas: EDADQUI
p12_ref = {1: '0-4', 2: '5-9', 3: '10-14', 4: '15-19', 5:'20-24', 6: '25-29', 7: '30-34', 8: '35-39', 9: '40-44', 10: '45-49',11: '50-54', 12: '55-59', 13: '60-64', 14: '65-69', 15:'70-74', 16: '75-79', 17:'80-84', 18:'85-89', 19: '90-94',20: '95 y más', 21: 'NOTAPPLICABLE', 22: 'MISSING'} 
p12_ref

#%%
# DIccionarios de etiquetas: P12
edadqui_ref = {1: 'Sí', 2: 'No', 3: 'MISSING', 4: 'NOTAPPLICABLE'}
edadqui_ref

# %%
ejemplo = bootstrap_data(px, py, 5, False)
ejemplo.bootstrap()



ejemplo2 = bootstrap_data(px, py, 5, True)
ejemplo2.bootstrap()
# %%
# Me gustaría poder darle un valor por defecto a 'constante', para que no sea necesario ponerlo