import pandas as pd, matplotlib.pyplot as plt, geopandas as gpd, contextily as ctx, numpy as np

# %%
#%%
#%%

#Censo


#%%

# Importo csvs

censo_persona = pd.read_csv(r'../censo2010/persona.csv')
censo_persona = censo_persona.drop(
    columns=["P01", "P05", "P06", "P07", "P12", "P08", "P09", "P10", "CONDACT"], axis=1)

censo_hogar = pd.read_csv(r'../censo2010/hogar.csv')
censo_hogar = censo_hogar.drop(
    columns=["H05", "H06", "H07", "H08", "H09", "H10", "H11", "H12", "H13", "H14", "H15", "H16", "H19A", "H19B", "H19C",
             "H19D", "PROP", "INDHAC"
             ], axis=1)

censo_vivienda = pd.read_csv(r'../censo2010/vivienda.csv')
censo_vivienda = censo_vivienda.drop(
    columns=[
        "TIPVV", "V01", "V02", "V00", "URP", "INCALSERV", "INMAT", "MUNI", "LOCAL", "INCALCONS", "TOTHOG"
    ], axis=1)

censo_radio = pd.read_csv(r'../censo2010/radio.csv')

censo_fraccion = pd.read_csv(r'../censo2010/frac.csv')

censo_dpto = pd.read_csv(r'../censo2010/dpto.csv')
censo_dpto = censo_dpto.drop(
    columns=["IDDPTO"], axis=1)

censo_prov = pd.read_csv(r'../censo2010/prov.csv')
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



#%%
#%%
#%%

# Elecciones


#%%

# Datos

elec_pres = pd.read_csv("D:/UBA/4to Cuarto año/Segundo cuatrimestre/Metodología de análisis en opinión pública/GITHUB_ANTERIOR/examenes/TP2/segunda_parte/Lena/DFs_elecciones/pres_circuito_completo.csv")
elec_dips =pd.read_csv("D:/UBA/4to Cuarto año/Segundo cuatrimestre/Metodología de análisis en opinión pública/GITHUB_ANTERIOR/examenes/TP2/segunda_parte/Lena/DFs_elecciones/DipNac_circuito_completo.csv")

resultados = pd.merge(elec_pres, elec_dips, on=["CODIGO_CIRCUITO", "NOMBRE_REGION", ])


resultados.to_csv("resultados.csv")



#%%
#%%
#%%


# Join datos georreferenciados

#%%

resultados_gpd = gpd.read_file(r'../elecciones_2019/CABA.shp')
censo_gpd = gpd.read_file(r'../censo2010/radios_censales/Codgeo_CABA_con_datos/cabaxrdatos.shp')

# %%

circuitos = resultados_gpd.to_crs(epsg=3857)
radios = censo_gpd.to_crs(epsg=3857)

# %% [markdown]

#### El merge de Radios y Circuitos

#%%
# Primero calculo el centroide de los radios electorales
radios['centroide'] = radios['geometry'].centroid
# %%
# Luego hago esos centroides su columna de geometrias
radios_cent = radios.set_geometry('centroide')
# %%
# Me quedo solamente con las columnas que em interesan
sub_radios = radios_cent[['LINK', 'geometry', 'centroide']]
sub_radios.sort_values(by=["LINK"])
# %%
# Construyo el link de los circuitos concatenando columnas

dato = 0

for fila in range(0, 167):
    dato = "1" + str(circuitos.loc[fila, "indec_d"])
    dato += "00" + str(circuitos.loc[fila, "circuito"])
    circuitos.loc[fila, "CODIGO_CIRCUITO"] = int(dato)

#%%
# Me quedo solo con las columnas que me interesan
sub_circuitos = circuitos[["CODIGO_CIRCUITO", "geometry"]]
sub_circuitos.sort_values(by=["CODIGO_CIRCUITO"])

# %%
# Hago el condenado Spatial Join
join = gpd.sjoin(sub_radios, sub_circuitos, how='left', op= 'within')

# %%
# Exporto el join a un .csv

join.to_csv("geom_join.csv")



#%%
#%%
#%%

# Join datos georreferenciados combinados con elecciones y con censo

#%%

# Mergeo el join con los datos geográficos y el DF de las elecciones

DF_geo_elecciones = pd.merge(join, resultados, on="CODIGO_CIRCUITO")
#DF_geo_elecciones = DF_geo_elecciones.drop(columns=["index_right", "CODIGO_CATEGORIA"], axis=1)
#DF_geo_elecciones = DF_geo_elecciones.drop(DF_geo_elecciones.columns[[-1, -1]], axis='columns')

# Borro los duplicados
#DF_elecc_drop_duplicates = DF_geo_elecciones.drop_duplicates(subset=None,
#                          keep='first',
#                          inplace=False,
#                          ignore_index=False)


#DF_elecc_drop_duplicates.to_csv("DF_elecc_drop_duplicates.csv")

#%%

DF_geo_censo = pd.merge(join, censo_cortado, on="LINK")
DF_geo_censo = DF_geo_censo.drop(columns=["LINK", "index_right", "FRAC_REF_ID", "IDRADIO", "NHOG", "TOTPERS",
                                          "DPTO_REF_ID", "DPTO", "VIVIENDA_REF_ID", "HOGAR_REF_ID", "ALGUNBI",
                                          "IDFRAC", "PROV_REF_ID"], axis=1)

# Acá con el drop duplicates da el mismo número, osea que no hace falta correrlo


#%%
# Seria ideal mergear estos dos, por ejemplo haciendo:
#DF_completo = pd.merge(DF_geo_censo, resultados, on="CODIGO_CIRCUITO")

DF_completo = pd.merge(DF_geo_elecciones, DF_geo_censo, on="CODIGO_CIRCUITO")