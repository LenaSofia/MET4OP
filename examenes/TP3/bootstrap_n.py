#%%
from os import replace
import numpy as np
import pandas as pd
from numpy import random
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
persona = pd.read_csv('persona.csv')
#%%
persona.columns
# %%
# Variables del censo a utilizar: X = EDADQUI (edades quinquenales), Y = P12 (utiliza computadora)

d = persona[['PERSONA_REF_ID','EDADQUI', 'P12']]
i = list(range(len(d)))
i
# %%
# DIccionarios de etiquetas: EDADQUI
p12_ref = {1: '0-4', 2: '5-9', 3: '10-14', 4: '15-19', 5:'20-24', 6: '25-29', 7: '30-34', 8: '35-39', 9: '40-44', 10: '45-49',11: '50-54', 12: '55-59', 13: '60-64', 14: '65-69', 15:'70-74', 16: '75-79', 17:'80-84', 18:'85-89', 19: '90-94',20: '95 y más', 21: 'NOTAPPLICABLE', 22: 'MISSING'} 
p12_ref

#%%
# DIccionarios de etiquetas: P12
edadqui_ref = {1: 'Sí', 2: 'No', 3: 'MISSING', 4: 'NOTAPPLICABLE'}
# %%
# Ahora lo que quiero es elegir al azar n filas de PERSONA_REF_ID, pero que cada vez que se saque una 'bolilla' se vuelva a colocar

I_k = np.random.choice(len(i), size = [len(i)], replace= True)
I_k

# %%
# Ahora necesito agarrar las filas I_k de D para formar D_k
# De esta manera lo que logro es que se forme un nuevo DF donde solo aparecen las filas cuyos indices estan en I_k
# Debería conseguir que se puedan repetir los valores de I_k, porque esta evitando eso y entonces df no queda de tamaño n

df = d[d.index.isin(I_k)]
# %%
df

# %%
d.head(6)
# %%
