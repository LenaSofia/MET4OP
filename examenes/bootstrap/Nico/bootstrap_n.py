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
persona = pd.read_csv(r'C:\Users\Usuario\Desktop\MAOP\TP_2\MET4OP\examenes\TP2\segunda_parte\censo2010\persona.csv')
#%%
persona.columns
# %%
# Variables del censo a utilizar: X = EDADQUI (edades quinquenales), Y = P12 (utiliza computadora)

d = persona[['PERSONA_REF_ID','EDADQUI', 'P12']]
i = list(range(len(d)))
i
# %%
# Tabla de etiquetas
ref = pd.read_excel(r'C:\Users\Usuario\Desktop\edadqui_p12.xlsx')
ref
# %%
# Ahora lo que quiero es elegir al azar n filas de PERSONA_REF_ID, pero que cada vez que se saque una 'bolilla' se vuelva a colocar

I_k = np.random.choice(len(i), size = [len(i)], replace= True)

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
