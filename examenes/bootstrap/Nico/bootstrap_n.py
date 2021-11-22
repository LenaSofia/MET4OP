#%%
from os import replace
import os
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
# Persona está dentro de persona.rar
# El csv por sí solo es demasiado grande para github
persona = pd.read_csv('persona.csv')
#%%
persona.columns
# %%
# Variables del censo a utilizar: X = EDADQUI (edades quinquenales), Y = P12 (utiliza computadora)

d = persona[['EDADQUI', 'P12']]
i = list(range(len(d)))
i
# %%
# DIccionarios de etiquetas: EDADQUI
p12_ref = {1: '0-4', 2: '5-9', 3: '10-14', 4: '15-19', 5:'20-24', 6: '25-29', 7: '30-34', 8: '35-39', 9: '40-44', 10: '45-49',11: '50-54', 12: '55-59', 13: '60-64', 14: '65-69', 15:'70-74', 16: '75-79', 17:'80-84', 18:'85-89', 19: '90-94',20: '95 y más', 21: 'NOTAPPLICABLE', 22: 'MISSING'} 
p12_ref

#%%
# DIccionarios de etiquetas: P12
edadqui_ref = {1: 'Sí', 2: 'No', 3: 'MISSING', 4: 'NOTAPPLICABLE'}
edadqui_ref
# %%
# Ahora lo que quiero es elegir al azar n filas de PERSONA_REF_ID, pero que cada vez que se saque una 'bolilla' se vuelva a colocar

I_k = np.random.choice(len(i), size = [len(i)], replace= True)
I_k

# %%
# II) 
# Ahora necesito agarrar las filas I_k de D para formar D_k

d_k = d.iloc[I_k]
d_k.sort_index().head(20)
# %%
# III)

# Es recontra por acá
d2 = persona[['EDADQUI', 'P12']]
i2 = list(range(len(d2)))

I2_k = np.random.choice(len(i2), size = [len(i2)], replace= True)
d2_k = d2.iloc[I2_k]

y = d2_k['P12'].tolist()
x = d2_k['EDADQUI'].tolist()
x = sm.add_constant(x)


result = sm.OLS(y,x).fit()
result.summary()


# 0.7962
# 0.7952
# 0.7957
# %%
