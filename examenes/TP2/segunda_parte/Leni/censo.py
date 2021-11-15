import pandas as pd, matplotlib.pyplot as plt, geopandas as gpd, contextily as ctx, numpy as np

# %% [markdown]

### Mapas
# %%

# %%

censo = gpd.read_file(r'..\censo2010\radios_censales\Codgeo_CABA_con_datos\cabaxrdatos.shp')
#censo.crs

# %%
#censo.to_crs(epsg=3857)

# %%

#censo.plot(figsize=(10, 10), alpha=0.25, edgecolor='k', color='yellow')
#plt.show()

# %% [markdown]

### Datos

# %%

# Importo csvs

censo_persona = pd.read_csv(r'..\censo2010\persona.csv')
censo_persona = censo_persona.drop(
    columns=["P01", "P05", "P06", "P07", "P12", "P08", "P09", "P10", "CONDACT"], axis=1)

censo_hogar = pd.read_csv(r'..\censo2010\hogar.csv')
censo_hogar = censo_hogar.drop(
    columns=["H05", "H06", "H07", "H08", "H09", "H10", "H11", "H12", "H13", "H14", "H15", "H16", "H19A", "H19B", "H19C",
             "H19D", "PROP", "INDHAC"
             ], axis=1)

censo_vivienda = pd.read_csv(r'..\censo2010\vivienda.csv')
censo_vivienda = censo_vivienda.drop(
    columns=[
        "TIPVV", "V01", "V02", "V00", "URP", "INCALSERV", "INMAT", "MUNI", "LOCAL", "INCALCONS", "TOTHOG"
    ], axis=1)

censo_radio = pd.read_csv(r'..\censo2010\radio.csv')

censo_fraccion = pd.read_csv(r'..\censo2010\frac.csv')

censo_dpto = pd.read_csv(r'..\censo2010\dpto.csv')
censo_dpto = censo_dpto.drop(
    columns=["IDDPTO"], axis=1)

censo_prov = pd.read_csv(r'..\censo2010\prov.csv')
censo_prov = censo_prov.drop(
    columns=["CPV2010_REF_ID", "IDPROV", "PROV", "NOMPROV"], axis=1)

# %%

# Voy a unir las tablas del censo de radio en adelante (radio, fracción, comuna y provincia):

censo_reducido = pd.merge(censo_radio, censo_fraccion, on="FRAC_REF_ID")
censo_reducido = pd.merge(censo_reducido, censo_dpto, on="DPTO_REF_ID")
censo_reducido = pd.merge(censo_reducido, censo_prov, on="PROV_REF_ID")

# %%

# Creo una columna vacía con el nombre LINK

censo_reducido = censo_reducido.assign(LINK="")

# Agrego la data a la columna LINK en censo_reducido

dato = 0

for fila in range(0, 3552):
    dato = "0" + str(censo_reducido.loc[fila, "DPTO"])

    if censo_reducido.loc[fila, "IDFRAC"] > 9:
        dato += str(censo_reducido.loc[fila, "IDFRAC"])
    elif 0 < censo_reducido.loc[fila, "IDFRAC"] < 10:
        dato += "0" + str(censo_reducido.loc[fila, "IDFRAC"])

    if censo_reducido.loc[fila, "IDRADIO"] > 9:
        dato += str(censo_reducido.loc[fila, "IDRADIO"])
    elif 0 < censo_reducido.loc[fila, "IDRADIO"] < 10:
        dato += "0" + str(censo_reducido.loc[fila, "IDFRAC"])

    censo_reducido.loc[fila, "LINK"] = str(dato)

# %%

# Voy a unir todas las tablas del censo para generar censo_cortado (censo reducido + vivienda, hogar y persona):

censo_cortado = pd.merge(censo_reducido, censo_vivienda, on="RADIO_REF_ID")
censo_cortado = pd.merge(censo_cortado, censo_hogar, on="VIVIENDA_REF_ID")
censo_cortado = pd.merge(censo_cortado, censo_persona, on="HOGAR_REF_ID")

# Lo guardo en un csv

censo_cortado.to_csv("censo_cortado.csv")

# %%

# Ahora uno el censo cortado con el censo geo-referenciado mediante el link:

#censo_cort_geo = pd.merge(censo_cortado, censo, on="LINK")

#censo_cort_geo.to_csv("censo_cort_geo.csv")
