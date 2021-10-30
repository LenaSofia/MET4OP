import pandas as pd

distrib_pres_comuna = pd.read_csv("distrib_pres_comuna.csv")

print(distrib_pres_comuna)

# Matriz de correlación entre datos electorales y comuna:
print("La correlación entre partidos y comunas es: \n")

distrib_corr = distrib_pres_comuna.corr()
print('')