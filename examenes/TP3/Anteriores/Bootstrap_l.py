import numpy as np


# Función:

def armar_muestras(muestra, repeticiones):
    """Se le pasa como parámetro una muestra y la cantidad de repeticiones esperadas. Devuelve una lista de listas,
    cada una tiene el largo de la original y está conformada por los elementos de la misma repetidos aleatoriamente"""

    conjunto_muestras = [muestra]

    for elemento in range(0, repeticiones):
        conjunto_muestras.append(list(np.random.choice(muestra, len(muestra))))

    return conjunto_muestras


# Ejemplo:

lista = [True, "coso", 0.3, 34, "f"]

intento1 = armar_muestras(lista, 100)

print(intento1)