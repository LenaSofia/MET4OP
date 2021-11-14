import pandas as pd, matplotlib.pyplot as plt, geopandas as gpd, contextily as ctx, numpy as np

# %%

# Importo .csv:

DF_completo = pd.read_csv(
    "D:/UBA/4to Cuarto año/Segundo cuatrimestre/Metodología de análisis en opinión pública/GITHUB_ANTERIOR/examenes/TP2/segunda_parte/Lena/DF_completo.csv")

# %%

# Armo DF de mayores de 16 años (que pueden votar)
DF_completo_mayores_16 = DF_completo.drop(DF_completo[DF_completo['P03'] < 16].index)

# Armo DF de mayores de 18 años y menores de 70 años (voto obligatorio)
DF_completo_voto_obligatorio = DF_completo.drop(DF_completo[DF_completo['P03'] < 18].index)
DF_completo_voto_obligatorio = DF_completo_voto_obligatorio.drop(
    DF_completo_voto_obligatorio[DF_completo['P03'] > 70].index)

# %%

# Uso sólo las columnas que necesito:

# Total
DF_para_corr = DF_completo[["VOTOS_FIT_DIPNAC",
                            "VOTOS_FDT_DIPNAC",
                            "VOTOS_JXC_DIPNAC",
                            "VOTOS_CF_DIPNAC",
                            "VOTOS_ULD_DIPNAC",
                            "VOTOS_NULO_DIPNAC",
                            "VOTOS_RECURRIDO_DIPNAC",
                            "VOTOS_IMPUGNADO_DIPNAC",
                            "VOTOS_BLANCO_DIPNAC",
                            "VOTOS_OTROS_DIPNAC",
                            "P03"]]

# Mayores de 16
DF_para_corr_mayores = DF_completo_mayores_16[["VOTOS_FIT_DIPNAC",
                            "VOTOS_FDT_DIPNAC",
                            "VOTOS_JXC_DIPNAC",
                            "VOTOS_CF_DIPNAC",
                            "VOTOS_ULD_DIPNAC",
                            "VOTOS_NULO_DIPNAC",
                            "VOTOS_RECURRIDO_DIPNAC",
                            "VOTOS_IMPUGNADO_DIPNAC",
                            "VOTOS_BLANCO_DIPNAC",
                            "VOTOS_OTROS_DIPNAC",
                            "P03"]]

# Mayores de 18 y menores de 70
DF_para_corr_oblig = DF_completo_voto_obligatorio[["VOTOS_FIT_DIPNAC",
                            "VOTOS_FDT_DIPNAC",
                            "VOTOS_JXC_DIPNAC",
                            "VOTOS_CF_DIPNAC",
                            "VOTOS_ULD_DIPNAC",
                            "VOTOS_NULO_DIPNAC",
                            "VOTOS_RECURRIDO_DIPNAC",
                            "VOTOS_IMPUGNADO_DIPNAC",
                            "VOTOS_BLANCO_DIPNAC",
                            "VOTOS_OTROS_DIPNAC",
                            "P03"]]

# %%

# Armo las matrices de correlación

# Total
matriz_DF_corr = DF_para_corr.corr()

# Mayores de 16
matriz_DF_corr_mayores = DF_para_corr_mayores.corr()

# Mayores de 18 y menores de 70
matriz_DF_corr_obligatorio = DF_para_corr_oblig.corr()
