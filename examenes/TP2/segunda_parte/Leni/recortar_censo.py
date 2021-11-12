
import pandas as pd, matplotlib.pyplot as plt, geopandas as gpd, contextily as ctx, numpy as np

# %%

# Mapas

censo_completo = pd.read_csv(r'censo_completo.csv')

#%%

censo_recortado = censo_completo.drop(censo_completo.columns[[0, 0]], axis='columns')
censo_recortado = censo_recortado.drop(columns=["PROV_REF_ID", "IDDPTO", "DPTO", "CPV2010_REF_ID", "IDPROV", "PROV",
                                               "NOMPROV", "V02", "URP", "MUNI", "LOCAL", "H05", "H06", "H07", "H08",
                                               "H09", "H10", "H11", "H12", "H13", "H14", "H15", "H16", "H19A", "H19B",
                                               "H19C", "H19D", "P01", "P06", "P08"], axis=1)

#%%

censo_recortado.to_csv("censo_recortado.csv")