import pandas as pd

# Comunas:

comunas = pd.Series(
    ["COMUNA 01", "COMUNA 01", "COMUNA 01", "COMUNA 01", "COMUNA 01", "COMUNA 01", "COMUNA 01", "COMUNA 01",
     "COMUNA 01", "COMUNA 01", "COMUNA 01", "COMUNA 02", "COMUNA 02", "COMUNA 02", "COMUNA 02", "COMUNA 02",
     "COMUNA 02", "COMUNA 02", "COMUNA 02", "COMUNA 02", "COMUNA 02", "COMUNA 02", "COMUNA 03", "COMUNA 03",
     "COMUNA 03", "COMUNA 03", "COMUNA 03", "COMUNA 03", "COMUNA 03", "COMUNA 03", "COMUNA 03", "COMUNA 03",
     "COMUNA 03", "COMUNA 04", "COMUNA 04", "COMUNA 04", "COMUNA 04", "COMUNA 04", "COMUNA 04", "COMUNA 04",
     "COMUNA 04", "COMUNA 04", "COMUNA 04", "COMUNA 04", "COMUNA 05", "COMUNA 05", "COMUNA 05", "COMUNA 05",
     "COMUNA 05", "COMUNA 05", "COMUNA 05", "COMUNA 05", "COMUNA 05", "COMUNA 05", "COMUNA 05", "COMUNA 06",
     "COMUNA 06", "COMUNA 06", "COMUNA 06", "COMUNA 06", "COMUNA 06", "COMUNA 06", "COMUNA 06", "COMUNA 06",
     "COMUNA 06", "COMUNA 06", "COMUNA 07", "COMUNA 07", "COMUNA 07", "COMUNA 07", "COMUNA 07", "COMUNA 07",
     "COMUNA 07", "COMUNA 07", "COMUNA 07", "COMUNA 07", "COMUNA 07", "COMUNA 08", "COMUNA 08", "COMUNA 08",
     "COMUNA 08", "COMUNA 08", "COMUNA 08", "COMUNA 08", "COMUNA 08", "COMUNA 08", "COMUNA 08", "COMUNA 08",
     "COMUNA 09", "COMUNA 09", "COMUNA 09", "COMUNA 09", "COMUNA 09", "COMUNA 09", "COMUNA 09", "COMUNA 09",
     "COMUNA 09", "COMUNA 09", "COMUNA 09", "COMUNA 10", "COMUNA 10", "COMUNA 10", "COMUNA 10",
     "COMUNA 10", "COMUNA 10", "COMUNA 10", "COMUNA 10", "COMUNA 10", "COMUNA 10", "COMUNA 10",
     "COMUNA 11", "COMUNA 11", "COMUNA 11", "COMUNA 11", "COMUNA 11", "COMUNA 11", "COMUNA 11",
     "COMUNA 11", "COMUNA 11", "COMUNA 11", "COMUNA 11", "COMUNA 12", "COMUNA 12", "COMUNA 12",
     "COMUNA 12", "COMUNA 12", "COMUNA 12", "COMUNA 12", "COMUNA 12", "COMUNA 12", "COMUNA 12",
     "COMUNA 12", "COMUNA 13", "COMUNA 13", "COMUNA 13", "COMUNA 13", "COMUNA 13", "COMUNA 13",
     "COMUNA 13", "COMUNA 13", "COMUNA 13", "COMUNA 13", "COMUNA 13", "COMUNA 14", "COMUNA 14",
     "COMUNA 14", "COMUNA 14", "COMUNA 14", "COMUNA 14", "COMUNA 14", "COMUNA 14", "COMUNA 14",
     "COMUNA 14", "COMUNA 14", "COMUNA 15", "COMUNA 15", "COMUNA 15", "COMUNA 15", "COMUNA 15",
     "COMUNA 15", "COMUNA 15", "COMUNA 15", "COMUNA 15", "COMUNA 15", "COMUNA 15"])

# %%

# Partidos:

partidos = pd.Series(["FIT", "FDT", "JXC", "CF", "ULD", "NOS", "BLANCO", "NULO", "RECURRIDO",
                      "IMPUGNADO", "OTROS", "FIT", "FDT", "JXC", "CF", "ULD", "NOS", "BLANCO",
                      "NULO", "RECURRIDO", "IMPUGNADO", "OTROS", "FIT", "FDT", "JXC", "CF", "ULD",
                      "NOS", "BLANCO", "NULO", "RECURRIDO", "IMPUGNADO", "OTROS", "FIT", "FDT",
                      "JXC", "CF", "ULD", "NOS", "BLANCO", "NULO", "RECURRIDO", "IMPUGNADO",
                      "OTROS", "FIT", "FDT", "JXC", "CF", "ULD", "NOS", "BLANCO", "NULO",
                      "RECURRIDO", "IMPUGNADO", "OTROS", "FIT", "FDT", "JXC", "CF", "ULD", "NOS",
                      "BLANCO", "NULO", "RECURRIDO", "IMPUGNADO", "OTROS", "FIT", "FDT", "JXC",
                      "CF", "ULD", "NOS", "BLANCO", "NULO", "RECURRIDO", "IMPUGNADO", "OTROS",
                      "FIT", "FDT", "JXC", "CF", "ULD", "NOS", "BLANCO", "NULO", "RECURRIDO",
                      "IMPUGNADO", "OTROS", "FIT", "FDT", "JXC", "CF", "ULD", "NOS", "BLANCO",
                      "NULO", "RECURRIDO", "IMPUGNADO", "OTROS", "FIT", "FDT", "JXC", "CF", "ULD",
                      "NOS", "BLANCO", "NULO", "RECURRIDO", "IMPUGNADO", "OTROS", "FIT", "FDT",
                      "JXC", "CF", "ULD", "NOS", "BLANCO", "NULO", "RECURRIDO", "IMPUGNADO",
                      "OTROS", "FIT", "FDT", "JXC", "CF", "ULD", "NOS", "BLANCO", "NULO",
                      "RECURRIDO", "IMPUGNADO", "OTROS", "FIT", "FDT", "JXC", "CF", "ULD", "NOS",
                      "BLANCO", "NULO", "RECURRIDO", "IMPUGNADO", "OTROS", "FIT", "FDT", "JXC",
                      "CF", "ULD", "NOS", "BLANCO", "NULO", "RECURRIDO", "IMPUGNADO", "OTROS",
                      "FIT", "FDT", "JXC", "CF", "ULD", "NOS", "BLANCO", "NULO", "RECURRIDO",
                      "IMPUGNADO", "OTROS"])

# %%

# Presidente:

porcentaje_presidente = pd.read_csv("data/presidente/porcentajes_pres_comuna.csv")

porcentaje_presidente_renombrado = porcentaje_presidente.rename(columns={"NOMBRE_REGION": "Comuna",
                                                                         "VOTOS_TOTALES_PRES": "TOTALES",
                                                                         "PORCENTAJE_FIT_PRES": "FIT",
                                                                         "PORCENTAJE_CF_PRES": "CF",
                                                                         "PORCENTAJE_FDT_PRES": "FDT",
                                                                         "PORCENTAJE_JXC_PRES": "JXC",
                                                                         "PORCENTAJE_NOS_PRES": "NOS",
                                                                         "PORCENTAJE_ULD_PRES": "ULD",
                                                                         "PORCENTAJE_NULO_PRES": "NULO",
                                                                         "PORCENTAJE_RECURRIDO_PRES": "RECURRIDO",
                                                                         "PORCENTAJE_IMPUGNADO_PRES": "IMPUGNADO",
                                                                         "PORCENTAJE_BLANCO_PRES": "BLANCO",
                                                                         "PORCENTAJE_OTROS_PRES": "OTROS"},
                                                                inplace=False)

Data_Frame_General = pd.DataFrame(
    {"Comuna": comunas,
     "Partido": partidos,
     "Porc_Pres": [
         porcentaje_presidente_renombrado.iloc[0]["FIT"],
         porcentaje_presidente_renombrado.iloc[0]["FDT"],
         porcentaje_presidente_renombrado.iloc[0]["JXC"],
         porcentaje_presidente_renombrado.iloc[0]["CF"],
         porcentaje_presidente_renombrado.iloc[0]["ULD"],
         porcentaje_presidente_renombrado.iloc[0]["NOS"],
         porcentaje_presidente_renombrado.iloc[0]["BLANCO"],
         porcentaje_presidente_renombrado.iloc[0]["NULO"],
         porcentaje_presidente_renombrado.iloc[0]["RECURRIDO"],
         porcentaje_presidente_renombrado.iloc[0]["IMPUGNADO"],
         porcentaje_presidente_renombrado.iloc[0]["OTROS"],
         porcentaje_presidente_renombrado.iloc[1]["FIT"],
         porcentaje_presidente_renombrado.iloc[1]["FDT"],
         porcentaje_presidente_renombrado.iloc[1]["JXC"],
         porcentaje_presidente_renombrado.iloc[1]["CF"],
         porcentaje_presidente_renombrado.iloc[1]["ULD"],
         porcentaje_presidente_renombrado.iloc[1]["NOS"],
         porcentaje_presidente_renombrado.iloc[1]["BLANCO"],
         porcentaje_presidente_renombrado.iloc[1]["NULO"],
         porcentaje_presidente_renombrado.iloc[1]["RECURRIDO"],
         porcentaje_presidente_renombrado.iloc[1]["IMPUGNADO"],
         porcentaje_presidente_renombrado.iloc[1]["OTROS"],
         porcentaje_presidente_renombrado.iloc[2]["FIT"],
         porcentaje_presidente_renombrado.iloc[2]["FDT"],
         porcentaje_presidente_renombrado.iloc[2]["JXC"],
         porcentaje_presidente_renombrado.iloc[2]["CF"],
         porcentaje_presidente_renombrado.iloc[2]["ULD"],
         porcentaje_presidente_renombrado.iloc[2]["NOS"],
         porcentaje_presidente_renombrado.iloc[2]["BLANCO"],
         porcentaje_presidente_renombrado.iloc[2]["NULO"],
         porcentaje_presidente_renombrado.iloc[2]["RECURRIDO"],
         porcentaje_presidente_renombrado.iloc[2]["IMPUGNADO"],
         porcentaje_presidente_renombrado.iloc[2]["OTROS"],
         porcentaje_presidente_renombrado.iloc[3]["FIT"],
         porcentaje_presidente_renombrado.iloc[3]["FDT"],
         porcentaje_presidente_renombrado.iloc[3]["JXC"],
         porcentaje_presidente_renombrado.iloc[3]["CF"],
         porcentaje_presidente_renombrado.iloc[3]["ULD"],
         porcentaje_presidente_renombrado.iloc[3]["NOS"],
         porcentaje_presidente_renombrado.iloc[3]["BLANCO"],
         porcentaje_presidente_renombrado.iloc[3]["NULO"],
         porcentaje_presidente_renombrado.iloc[3]["RECURRIDO"],
         porcentaje_presidente_renombrado.iloc[3]["IMPUGNADO"],
         porcentaje_presidente_renombrado.iloc[3]["OTROS"],
         porcentaje_presidente_renombrado.iloc[4]["FIT"],
         porcentaje_presidente_renombrado.iloc[4]["FDT"],
         porcentaje_presidente_renombrado.iloc[4]["JXC"],
         porcentaje_presidente_renombrado.iloc[4]["CF"],
         porcentaje_presidente_renombrado.iloc[4]["ULD"],
         porcentaje_presidente_renombrado.iloc[4]["NOS"],
         porcentaje_presidente_renombrado.iloc[4]["BLANCO"],
         porcentaje_presidente_renombrado.iloc[4]["NULO"],
         porcentaje_presidente_renombrado.iloc[4]["RECURRIDO"],
         porcentaje_presidente_renombrado.iloc[4]["IMPUGNADO"],
         porcentaje_presidente_renombrado.iloc[4]["OTROS"],
         porcentaje_presidente_renombrado.iloc[5]["FIT"],
         porcentaje_presidente_renombrado.iloc[5]["FDT"],
         porcentaje_presidente_renombrado.iloc[5]["JXC"],
         porcentaje_presidente_renombrado.iloc[5]["CF"],
         porcentaje_presidente_renombrado.iloc[5]["ULD"],
         porcentaje_presidente_renombrado.iloc[5]["NOS"],
         porcentaje_presidente_renombrado.iloc[5]["BLANCO"],
         porcentaje_presidente_renombrado.iloc[5]["NULO"],
         porcentaje_presidente_renombrado.iloc[5]["RECURRIDO"],
         porcentaje_presidente_renombrado.iloc[5]["IMPUGNADO"],
         porcentaje_presidente_renombrado.iloc[5]["OTROS"],
         porcentaje_presidente_renombrado.iloc[6]["FIT"],
         porcentaje_presidente_renombrado.iloc[6]["FDT"],
         porcentaje_presidente_renombrado.iloc[6]["JXC"],
         porcentaje_presidente_renombrado.iloc[6]["CF"],
         porcentaje_presidente_renombrado.iloc[6]["ULD"],
         porcentaje_presidente_renombrado.iloc[6]["NOS"],
         porcentaje_presidente_renombrado.iloc[6]["BLANCO"],
         porcentaje_presidente_renombrado.iloc[6]["NULO"],
         porcentaje_presidente_renombrado.iloc[6]["RECURRIDO"],
         porcentaje_presidente_renombrado.iloc[6]["IMPUGNADO"],
         porcentaje_presidente_renombrado.iloc[6]["OTROS"],
         porcentaje_presidente_renombrado.iloc[7]["FIT"],
         porcentaje_presidente_renombrado.iloc[7]["FDT"],
         porcentaje_presidente_renombrado.iloc[7]["JXC"],
         porcentaje_presidente_renombrado.iloc[7]["CF"],
         porcentaje_presidente_renombrado.iloc[7]["ULD"],
         porcentaje_presidente_renombrado.iloc[7]["NOS"],
         porcentaje_presidente_renombrado.iloc[7]["BLANCO"],
         porcentaje_presidente_renombrado.iloc[7]["NULO"],
         porcentaje_presidente_renombrado.iloc[7]["RECURRIDO"],
         porcentaje_presidente_renombrado.iloc[7]["IMPUGNADO"],
         porcentaje_presidente_renombrado.iloc[7]["OTROS"],
         porcentaje_presidente_renombrado.iloc[8]["FIT"],
         porcentaje_presidente_renombrado.iloc[8]["FDT"],
         porcentaje_presidente_renombrado.iloc[8]["JXC"],
         porcentaje_presidente_renombrado.iloc[8]["CF"],
         porcentaje_presidente_renombrado.iloc[8]["ULD"],
         porcentaje_presidente_renombrado.iloc[8]["NOS"],
         porcentaje_presidente_renombrado.iloc[8]["BLANCO"],
         porcentaje_presidente_renombrado.iloc[8]["NULO"],
         porcentaje_presidente_renombrado.iloc[8]["RECURRIDO"],
         porcentaje_presidente_renombrado.iloc[8]["IMPUGNADO"],
         porcentaje_presidente_renombrado.iloc[8]["OTROS"],
         porcentaje_presidente_renombrado.iloc[9]["FIT"],
         porcentaje_presidente_renombrado.iloc[9]["FDT"],
         porcentaje_presidente_renombrado.iloc[9]["JXC"],
         porcentaje_presidente_renombrado.iloc[9]["CF"],
         porcentaje_presidente_renombrado.iloc[9]["ULD"],
         porcentaje_presidente_renombrado.iloc[9]["NOS"],
         porcentaje_presidente_renombrado.iloc[9]["BLANCO"],
         porcentaje_presidente_renombrado.iloc[9]["NULO"],
         porcentaje_presidente_renombrado.iloc[9]["RECURRIDO"],
         porcentaje_presidente_renombrado.iloc[9]["IMPUGNADO"],
         porcentaje_presidente_renombrado.iloc[9]["OTROS"],
         porcentaje_presidente_renombrado.iloc[10]["FIT"],
         porcentaje_presidente_renombrado.iloc[10]["FDT"],
         porcentaje_presidente_renombrado.iloc[10]["JXC"],
         porcentaje_presidente_renombrado.iloc[10]["CF"],
         porcentaje_presidente_renombrado.iloc[10]["ULD"],
         porcentaje_presidente_renombrado.iloc[10]["NOS"],
         porcentaje_presidente_renombrado.iloc[10]["BLANCO"],
         porcentaje_presidente_renombrado.iloc[10]["NULO"],
         porcentaje_presidente_renombrado.iloc[10]["RECURRIDO"],
         porcentaje_presidente_renombrado.iloc[10]["IMPUGNADO"],
         porcentaje_presidente_renombrado.iloc[10]["OTROS"],
         porcentaje_presidente_renombrado.iloc[11]["FIT"],
         porcentaje_presidente_renombrado.iloc[11]["FDT"],
         porcentaje_presidente_renombrado.iloc[11]["JXC"],
         porcentaje_presidente_renombrado.iloc[11]["CF"],
         porcentaje_presidente_renombrado.iloc[11]["ULD"],
         porcentaje_presidente_renombrado.iloc[11]["NOS"],
         porcentaje_presidente_renombrado.iloc[11]["BLANCO"],
         porcentaje_presidente_renombrado.iloc[11]["NULO"],
         porcentaje_presidente_renombrado.iloc[11]["RECURRIDO"],
         porcentaje_presidente_renombrado.iloc[11]["IMPUGNADO"],
         porcentaje_presidente_renombrado.iloc[11]["OTROS"],
         porcentaje_presidente_renombrado.iloc[12]["FIT"],
         porcentaje_presidente_renombrado.iloc[12]["FDT"],
         porcentaje_presidente_renombrado.iloc[12]["JXC"],
         porcentaje_presidente_renombrado.iloc[12]["CF"],
         porcentaje_presidente_renombrado.iloc[12]["ULD"],
         porcentaje_presidente_renombrado.iloc[12]["NOS"],
         porcentaje_presidente_renombrado.iloc[12]["BLANCO"],
         porcentaje_presidente_renombrado.iloc[12]["NULO"],
         porcentaje_presidente_renombrado.iloc[12]["RECURRIDO"],
         porcentaje_presidente_renombrado.iloc[12]["IMPUGNADO"],
         porcentaje_presidente_renombrado.iloc[12]["OTROS"],
         porcentaje_presidente_renombrado.iloc[13]["FIT"],
         porcentaje_presidente_renombrado.iloc[13]["FDT"],
         porcentaje_presidente_renombrado.iloc[13]["JXC"],
         porcentaje_presidente_renombrado.iloc[13]["CF"],
         porcentaje_presidente_renombrado.iloc[13]["ULD"],
         porcentaje_presidente_renombrado.iloc[13]["NOS"],
         porcentaje_presidente_renombrado.iloc[13]["BLANCO"],
         porcentaje_presidente_renombrado.iloc[13]["NULO"],
         porcentaje_presidente_renombrado.iloc[13]["RECURRIDO"],
         porcentaje_presidente_renombrado.iloc[13]["IMPUGNADO"],
         porcentaje_presidente_renombrado.iloc[13]["OTROS"],
         porcentaje_presidente_renombrado.iloc[14]["FIT"],
         porcentaje_presidente_renombrado.iloc[14]["FDT"],
         porcentaje_presidente_renombrado.iloc[14]["JXC"],
         porcentaje_presidente_renombrado.iloc[14]["CF"],
         porcentaje_presidente_renombrado.iloc[14]["ULD"],
         porcentaje_presidente_renombrado.iloc[14]["NOS"],
         porcentaje_presidente_renombrado.iloc[14]["BLANCO"],
         porcentaje_presidente_renombrado.iloc[14]["NULO"],
         porcentaje_presidente_renombrado.iloc[14]["RECURRIDO"],
         porcentaje_presidente_renombrado.iloc[14]["IMPUGNADO"],
         porcentaje_presidente_renombrado.iloc[14]["OTROS"]
     ]})

# %%

# Diputados nacionales

porcentaje_DipNac = pd.read_csv("data/diputados_nacionales/porcentajes_DipNac_comuna.csv")

porcentaje_DipNac_renombrado = porcentaje_DipNac.rename(columns={"NOMBRE_REGION": "Comuna",
                                                                 "VOTOS_TOTALES_DIPNAC": "TOTALES",
                                                                 "PORCENTAJE_FIT_DIPNAC": "FIT",
                                                                 "PORCENTAJE_CF_DIPNAC": "CF",
                                                                 "PORCENTAJE_FDT_DIPNAC": "FDT",
                                                                 "PORCENTAJE_JXC_DIPNAC": "JXC",
                                                                 "PORCENTAJE_NOS_DIPNAC": "NOS",
                                                                 "PORCENTAJE_ULD_DIPNAC": "ULD",
                                                                 "PORCENTAJE_NULO_DIPNAC": "NULO",
                                                                 "PORCENTAJE_RECURRIDO_DIPNAC": "RECURRIDO",
                                                                 "PORCENTAJE_IMPUGNADO_DIPNAC": "IMPUGNADO",
                                                                 "PORCENTAJE_BLANCO_DIPNAC": "BLANCO",
                                                                 "PORCENTAJE_OTROS_DIPNAC": "OTROS"},
                                                        inplace=False)

Data_Frame_General = Data_Frame_General.assign(Porc_DipNac=
[
    porcentaje_DipNac_renombrado.iloc[0]["FIT"],
    porcentaje_DipNac_renombrado.iloc[0]["FDT"],
    porcentaje_DipNac_renombrado.iloc[0]["JXC"],
    porcentaje_DipNac_renombrado.iloc[0]["CF"],
    porcentaje_DipNac_renombrado.iloc[0]["ULD"],
    0,
    porcentaje_DipNac_renombrado.iloc[0]["BLANCO"],
    porcentaje_DipNac_renombrado.iloc[0]["NULO"],
    porcentaje_DipNac_renombrado.iloc[0]["RECURRIDO"],
    porcentaje_DipNac_renombrado.iloc[0]["IMPUGNADO"],
    porcentaje_DipNac_renombrado.iloc[0]["OTROS"],
    porcentaje_DipNac_renombrado.iloc[1]["FIT"],
    porcentaje_DipNac_renombrado.iloc[1]["FDT"],
    porcentaje_DipNac_renombrado.iloc[1]["JXC"],
    porcentaje_DipNac_renombrado.iloc[1]["CF"],
    porcentaje_DipNac_renombrado.iloc[1]["ULD"],
    0,
    porcentaje_DipNac_renombrado.iloc[1]["BLANCO"],
    porcentaje_DipNac_renombrado.iloc[1]["NULO"],
    porcentaje_DipNac_renombrado.iloc[1]["RECURRIDO"],
    porcentaje_DipNac_renombrado.iloc[1]["IMPUGNADO"],
    porcentaje_DipNac_renombrado.iloc[1]["OTROS"],
    porcentaje_DipNac_renombrado.iloc[2]["FIT"],
    porcentaje_DipNac_renombrado.iloc[2]["FDT"],
    porcentaje_DipNac_renombrado.iloc[2]["JXC"],
    porcentaje_DipNac_renombrado.iloc[2]["CF"],
    porcentaje_DipNac_renombrado.iloc[2]["ULD"],
    0,
    porcentaje_DipNac_renombrado.iloc[2]["BLANCO"],
    porcentaje_DipNac_renombrado.iloc[2]["NULO"],
    porcentaje_DipNac_renombrado.iloc[2]["RECURRIDO"],
    porcentaje_DipNac_renombrado.iloc[2]["IMPUGNADO"],
    porcentaje_DipNac_renombrado.iloc[2]["OTROS"],
    porcentaje_DipNac_renombrado.iloc[3]["FIT"],
    porcentaje_DipNac_renombrado.iloc[3]["FDT"],
    porcentaje_DipNac_renombrado.iloc[3]["JXC"],
    porcentaje_DipNac_renombrado.iloc[3]["CF"],
    porcentaje_DipNac_renombrado.iloc[3]["ULD"],
    0,
    porcentaje_DipNac_renombrado.iloc[3]["BLANCO"],
    porcentaje_DipNac_renombrado.iloc[3]["NULO"],
    porcentaje_DipNac_renombrado.iloc[3]["RECURRIDO"],
    porcentaje_DipNac_renombrado.iloc[3]["IMPUGNADO"],
    porcentaje_DipNac_renombrado.iloc[3]["OTROS"],
    porcentaje_DipNac_renombrado.iloc[4]["FIT"],
    porcentaje_DipNac_renombrado.iloc[4]["FDT"],
    porcentaje_DipNac_renombrado.iloc[4]["JXC"],
    porcentaje_DipNac_renombrado.iloc[4]["CF"],
    porcentaje_DipNac_renombrado.iloc[4]["ULD"],
    0,
    porcentaje_DipNac_renombrado.iloc[4]["BLANCO"],
    porcentaje_DipNac_renombrado.iloc[4]["NULO"],
    porcentaje_DipNac_renombrado.iloc[4]["RECURRIDO"],
    porcentaje_DipNac_renombrado.iloc[4]["IMPUGNADO"],
    porcentaje_DipNac_renombrado.iloc[4]["OTROS"],
    porcentaje_DipNac_renombrado.iloc[5]["FIT"],
    porcentaje_DipNac_renombrado.iloc[5]["FDT"],
    porcentaje_DipNac_renombrado.iloc[5]["JXC"],
    porcentaje_DipNac_renombrado.iloc[5]["CF"],
    porcentaje_DipNac_renombrado.iloc[5]["ULD"],
    0,
    porcentaje_DipNac_renombrado.iloc[5]["BLANCO"],
    porcentaje_DipNac_renombrado.iloc[5]["NULO"],
    porcentaje_DipNac_renombrado.iloc[5]["RECURRIDO"],
    porcentaje_DipNac_renombrado.iloc[5]["IMPUGNADO"],
    porcentaje_DipNac_renombrado.iloc[5]["OTROS"],
    porcentaje_DipNac_renombrado.iloc[6]["FIT"],
    porcentaje_DipNac_renombrado.iloc[6]["FDT"],
    porcentaje_DipNac_renombrado.iloc[6]["JXC"],
    porcentaje_DipNac_renombrado.iloc[6]["CF"],
    porcentaje_DipNac_renombrado.iloc[6]["ULD"],
    0,
    porcentaje_DipNac_renombrado.iloc[6]["BLANCO"],
    porcentaje_DipNac_renombrado.iloc[6]["NULO"],
    porcentaje_DipNac_renombrado.iloc[6]["RECURRIDO"],
    porcentaje_DipNac_renombrado.iloc[6]["IMPUGNADO"],
    porcentaje_DipNac_renombrado.iloc[6]["OTROS"],
    porcentaje_DipNac_renombrado.iloc[7]["FIT"],
    porcentaje_DipNac_renombrado.iloc[7]["FDT"],
    porcentaje_DipNac_renombrado.iloc[7]["JXC"],
    porcentaje_DipNac_renombrado.iloc[7]["CF"],
    porcentaje_DipNac_renombrado.iloc[7]["ULD"],
    0,
    porcentaje_DipNac_renombrado.iloc[7]["BLANCO"],
    porcentaje_DipNac_renombrado.iloc[7]["NULO"],
    porcentaje_DipNac_renombrado.iloc[7]["RECURRIDO"],
    porcentaje_DipNac_renombrado.iloc[7]["IMPUGNADO"],
    porcentaje_DipNac_renombrado.iloc[7]["OTROS"],
    porcentaje_DipNac_renombrado.iloc[8]["FIT"],
    porcentaje_DipNac_renombrado.iloc[8]["FDT"],
    porcentaje_DipNac_renombrado.iloc[8]["JXC"],
    porcentaje_DipNac_renombrado.iloc[8]["CF"],
    porcentaje_DipNac_renombrado.iloc[8]["ULD"],
    0,
    porcentaje_DipNac_renombrado.iloc[8]["BLANCO"],
    porcentaje_DipNac_renombrado.iloc[8]["NULO"],
    porcentaje_DipNac_renombrado.iloc[8]["RECURRIDO"],
    porcentaje_DipNac_renombrado.iloc[8]["IMPUGNADO"],
    porcentaje_DipNac_renombrado.iloc[8]["OTROS"],
    porcentaje_DipNac_renombrado.iloc[9]["FIT"],
    porcentaje_DipNac_renombrado.iloc[9]["FDT"],
    porcentaje_DipNac_renombrado.iloc[9]["JXC"],
    porcentaje_DipNac_renombrado.iloc[9]["CF"],
    porcentaje_DipNac_renombrado.iloc[9]["ULD"],
    0,
    porcentaje_DipNac_renombrado.iloc[9]["BLANCO"],
    porcentaje_DipNac_renombrado.iloc[9]["NULO"],
    porcentaje_DipNac_renombrado.iloc[9]["RECURRIDO"],
    porcentaje_DipNac_renombrado.iloc[9]["IMPUGNADO"],
    porcentaje_DipNac_renombrado.iloc[9]["OTROS"],
    porcentaje_DipNac_renombrado.iloc[10]["FIT"],
    porcentaje_DipNac_renombrado.iloc[10]["FDT"],
    porcentaje_DipNac_renombrado.iloc[10]["JXC"],
    porcentaje_DipNac_renombrado.iloc[10]["CF"],
    porcentaje_DipNac_renombrado.iloc[10]["ULD"],
    0,
    porcentaje_DipNac_renombrado.iloc[10]["BLANCO"],
    porcentaje_DipNac_renombrado.iloc[10]["NULO"],
    porcentaje_DipNac_renombrado.iloc[10]["RECURRIDO"],
    porcentaje_DipNac_renombrado.iloc[10]["IMPUGNADO"],
    porcentaje_DipNac_renombrado.iloc[10]["OTROS"],
    porcentaje_DipNac_renombrado.iloc[11]["FIT"],
    porcentaje_DipNac_renombrado.iloc[11]["FDT"],
    porcentaje_DipNac_renombrado.iloc[11]["JXC"],
    porcentaje_DipNac_renombrado.iloc[11]["CF"],
    porcentaje_DipNac_renombrado.iloc[11]["ULD"],
    0,
    porcentaje_DipNac_renombrado.iloc[11]["BLANCO"],
    porcentaje_DipNac_renombrado.iloc[11]["NULO"],
    porcentaje_DipNac_renombrado.iloc[11]["RECURRIDO"],
    porcentaje_DipNac_renombrado.iloc[11]["IMPUGNADO"],
    porcentaje_DipNac_renombrado.iloc[11]["OTROS"],
    porcentaje_DipNac_renombrado.iloc[12]["FIT"],
    porcentaje_DipNac_renombrado.iloc[12]["FDT"],
    porcentaje_DipNac_renombrado.iloc[12]["JXC"],
    porcentaje_DipNac_renombrado.iloc[12]["CF"],
    porcentaje_DipNac_renombrado.iloc[12]["ULD"],
    0,
    porcentaje_DipNac_renombrado.iloc[12]["BLANCO"],
    porcentaje_DipNac_renombrado.iloc[12]["NULO"],
    porcentaje_DipNac_renombrado.iloc[12]["RECURRIDO"],
    porcentaje_DipNac_renombrado.iloc[12]["IMPUGNADO"],
    porcentaje_DipNac_renombrado.iloc[12]["OTROS"],
    porcentaje_DipNac_renombrado.iloc[13]["FIT"],
    porcentaje_DipNac_renombrado.iloc[13]["FDT"],
    porcentaje_DipNac_renombrado.iloc[13]["JXC"],
    porcentaje_DipNac_renombrado.iloc[13]["CF"],
    porcentaje_DipNac_renombrado.iloc[13]["ULD"],
    0,
    porcentaje_DipNac_renombrado.iloc[13]["BLANCO"],
    porcentaje_DipNac_renombrado.iloc[13]["NULO"],
    porcentaje_DipNac_renombrado.iloc[13]["RECURRIDO"],
    porcentaje_DipNac_renombrado.iloc[13]["IMPUGNADO"],
    porcentaje_DipNac_renombrado.iloc[13]["OTROS"],
    porcentaje_DipNac_renombrado.iloc[14]["FIT"],
    porcentaje_DipNac_renombrado.iloc[14]["FDT"],
    porcentaje_DipNac_renombrado.iloc[14]["JXC"],
    porcentaje_DipNac_renombrado.iloc[14]["CF"],
    porcentaje_DipNac_renombrado.iloc[14]["ULD"],
    0,
    porcentaje_DipNac_renombrado.iloc[14]["BLANCO"],
    porcentaje_DipNac_renombrado.iloc[14]["NULO"],
    porcentaje_DipNac_renombrado.iloc[14]["RECURRIDO"],
    porcentaje_DipNac_renombrado.iloc[14]["IMPUGNADO"],
    porcentaje_DipNac_renombrado.iloc[14]["OTROS"]
])

# %%

# Jefe de gobierno:

porcentaje_JefGob = pd.read_csv("data/jefe_gobierno/porcentajes_JefGob_comuna.csv")

porcentaje_JefGob_renombrado = porcentaje_JefGob.rename(columns={"NOMBRE_REGION": "Comuna",
                                                                 "VOTOS_TOTALES_JEFGOB": "TOTALES",
                                                                 "PORCENTAJE_FIT_JEFGOB": "FIT",
                                                                 "PORCENTAJE_CF_JEFGOB": "CF",
                                                                 "PORCENTAJE_FDT_JEFGOB": "FDT",
                                                                 "PORCENTAJE_JXC_JEFGOB": "JXC",
                                                                 "PORCENTAJE_NOS_JEFGOB": "NOS",
                                                                 "PORCENTAJE_ULD_JEFGOB": "ULD",
                                                                 "PORCENTAJE_NULO_JEFGOB": "NULO",
                                                                 "PORCENTAJE_RECURRIDO_JEFGOB": "RECURRIDO",
                                                                 "PORCENTAJE_IMPUGNADO_JEFGOB": "IMPUGNADO",
                                                                 "PORCENTAJE_BLANCO_JEFGOB": "BLANCO",
                                                                 "PORCENTAJE_OTROS_JEFGOB": "OTROS"},
                                                        inplace=False)

Data_Frame_General = Data_Frame_General.assign(Porc_JefGob=
[
    porcentaje_JefGob_renombrado.iloc[0]["FIT"],
    porcentaje_JefGob_renombrado.iloc[0]["FDT"],
    porcentaje_JefGob_renombrado.iloc[0]["JXC"],
    porcentaje_JefGob_renombrado.iloc[0]["CF"],
    porcentaje_JefGob_renombrado.iloc[0]["ULD"],
    0,
    porcentaje_JefGob_renombrado.iloc[0]["BLANCO"],
    porcentaje_JefGob_renombrado.iloc[0]["NULO"],
    porcentaje_JefGob_renombrado.iloc[0]["RECURRIDO"],
    porcentaje_JefGob_renombrado.iloc[0]["IMPUGNADO"],
    porcentaje_JefGob_renombrado.iloc[0]["OTROS"],
    porcentaje_JefGob_renombrado.iloc[1]["FIT"],
    porcentaje_JefGob_renombrado.iloc[1]["FDT"],
    porcentaje_JefGob_renombrado.iloc[1]["JXC"],
    porcentaje_JefGob_renombrado.iloc[1]["CF"],
    porcentaje_JefGob_renombrado.iloc[1]["ULD"],
    0,
    porcentaje_JefGob_renombrado.iloc[1]["BLANCO"],
    porcentaje_JefGob_renombrado.iloc[1]["NULO"],
    porcentaje_JefGob_renombrado.iloc[1]["RECURRIDO"],
    porcentaje_JefGob_renombrado.iloc[1]["IMPUGNADO"],
    porcentaje_JefGob_renombrado.iloc[1]["OTROS"],
    porcentaje_JefGob_renombrado.iloc[2]["FIT"],
    porcentaje_JefGob_renombrado.iloc[2]["FDT"],
    porcentaje_JefGob_renombrado.iloc[2]["JXC"],
    porcentaje_JefGob_renombrado.iloc[2]["CF"],
    porcentaje_JefGob_renombrado.iloc[2]["ULD"],
    0,
    porcentaje_JefGob_renombrado.iloc[2]["BLANCO"],
    porcentaje_JefGob_renombrado.iloc[2]["NULO"],
    porcentaje_JefGob_renombrado.iloc[2]["RECURRIDO"],
    porcentaje_JefGob_renombrado.iloc[2]["IMPUGNADO"],
    porcentaje_JefGob_renombrado.iloc[2]["OTROS"],
    porcentaje_JefGob_renombrado.iloc[3]["FIT"],
    porcentaje_JefGob_renombrado.iloc[3]["FDT"],
    porcentaje_JefGob_renombrado.iloc[3]["JXC"],
    porcentaje_JefGob_renombrado.iloc[3]["CF"],
    porcentaje_JefGob_renombrado.iloc[3]["ULD"],
    0,
    porcentaje_JefGob_renombrado.iloc[3]["BLANCO"],
    porcentaje_JefGob_renombrado.iloc[3]["NULO"],
    porcentaje_JefGob_renombrado.iloc[3]["RECURRIDO"],
    porcentaje_JefGob_renombrado.iloc[3]["IMPUGNADO"],
    porcentaje_JefGob_renombrado.iloc[3]["OTROS"],
    porcentaje_JefGob_renombrado.iloc[4]["FIT"],
    porcentaje_JefGob_renombrado.iloc[4]["FDT"],
    porcentaje_JefGob_renombrado.iloc[4]["JXC"],
    porcentaje_JefGob_renombrado.iloc[4]["CF"],
    porcentaje_JefGob_renombrado.iloc[4]["ULD"],
    0,
    porcentaje_JefGob_renombrado.iloc[4]["BLANCO"],
    porcentaje_JefGob_renombrado.iloc[4]["NULO"],
    porcentaje_JefGob_renombrado.iloc[4]["RECURRIDO"],
    porcentaje_JefGob_renombrado.iloc[4]["IMPUGNADO"],
    porcentaje_JefGob_renombrado.iloc[4]["OTROS"],
    porcentaje_JefGob_renombrado.iloc[5]["FIT"],
    porcentaje_JefGob_renombrado.iloc[5]["FDT"],
    porcentaje_JefGob_renombrado.iloc[5]["JXC"],
    porcentaje_JefGob_renombrado.iloc[5]["CF"],
    porcentaje_JefGob_renombrado.iloc[5]["ULD"],
    0,
    porcentaje_JefGob_renombrado.iloc[5]["BLANCO"],
    porcentaje_JefGob_renombrado.iloc[5]["NULO"],
    porcentaje_JefGob_renombrado.iloc[5]["RECURRIDO"],
    porcentaje_JefGob_renombrado.iloc[5]["IMPUGNADO"],
    porcentaje_JefGob_renombrado.iloc[5]["OTROS"],
    porcentaje_JefGob_renombrado.iloc[6]["FIT"],
    porcentaje_JefGob_renombrado.iloc[6]["FDT"],
    porcentaje_JefGob_renombrado.iloc[6]["JXC"],
    porcentaje_JefGob_renombrado.iloc[6]["CF"],
    porcentaje_JefGob_renombrado.iloc[6]["ULD"],
    0,
    porcentaje_JefGob_renombrado.iloc[6]["BLANCO"],
    porcentaje_JefGob_renombrado.iloc[6]["NULO"],
    porcentaje_JefGob_renombrado.iloc[6]["RECURRIDO"],
    porcentaje_JefGob_renombrado.iloc[6]["IMPUGNADO"],
    porcentaje_JefGob_renombrado.iloc[6]["OTROS"],
    porcentaje_JefGob_renombrado.iloc[7]["FIT"],
    porcentaje_JefGob_renombrado.iloc[7]["FDT"],
    porcentaje_JefGob_renombrado.iloc[7]["JXC"],
    porcentaje_JefGob_renombrado.iloc[7]["CF"],
    porcentaje_JefGob_renombrado.iloc[7]["ULD"],
    0,
    porcentaje_JefGob_renombrado.iloc[7]["BLANCO"],
    porcentaje_JefGob_renombrado.iloc[7]["NULO"],
    porcentaje_JefGob_renombrado.iloc[7]["RECURRIDO"],
    porcentaje_JefGob_renombrado.iloc[7]["IMPUGNADO"],
    porcentaje_JefGob_renombrado.iloc[7]["OTROS"],
    porcentaje_JefGob_renombrado.iloc[8]["FIT"],
    porcentaje_JefGob_renombrado.iloc[8]["FDT"],
    porcentaje_JefGob_renombrado.iloc[8]["JXC"],
    porcentaje_JefGob_renombrado.iloc[8]["CF"],
    porcentaje_JefGob_renombrado.iloc[8]["ULD"],
    0,
    porcentaje_JefGob_renombrado.iloc[8]["BLANCO"],
    porcentaje_JefGob_renombrado.iloc[8]["NULO"],
    porcentaje_JefGob_renombrado.iloc[8]["RECURRIDO"],
    porcentaje_JefGob_renombrado.iloc[8]["IMPUGNADO"],
    porcentaje_JefGob_renombrado.iloc[8]["OTROS"],
    porcentaje_JefGob_renombrado.iloc[9]["FIT"],
    porcentaje_JefGob_renombrado.iloc[9]["FDT"],
    porcentaje_JefGob_renombrado.iloc[9]["JXC"],
    porcentaje_JefGob_renombrado.iloc[9]["CF"],
    porcentaje_JefGob_renombrado.iloc[9]["ULD"],
    0,
    porcentaje_JefGob_renombrado.iloc[9]["BLANCO"],
    porcentaje_JefGob_renombrado.iloc[9]["NULO"],
    porcentaje_JefGob_renombrado.iloc[9]["RECURRIDO"],
    porcentaje_JefGob_renombrado.iloc[9]["IMPUGNADO"],
    porcentaje_JefGob_renombrado.iloc[9]["OTROS"],
    porcentaje_JefGob_renombrado.iloc[10]["FIT"],
    porcentaje_JefGob_renombrado.iloc[10]["FDT"],
    porcentaje_JefGob_renombrado.iloc[10]["JXC"],
    porcentaje_JefGob_renombrado.iloc[10]["CF"],
    porcentaje_JefGob_renombrado.iloc[10]["ULD"],
    0,
    porcentaje_JefGob_renombrado.iloc[10]["BLANCO"],
    porcentaje_JefGob_renombrado.iloc[10]["NULO"],
    porcentaje_JefGob_renombrado.iloc[10]["RECURRIDO"],
    porcentaje_JefGob_renombrado.iloc[10]["IMPUGNADO"],
    porcentaje_JefGob_renombrado.iloc[10]["OTROS"],
    porcentaje_JefGob_renombrado.iloc[11]["FIT"],
    porcentaje_JefGob_renombrado.iloc[11]["FDT"],
    porcentaje_JefGob_renombrado.iloc[11]["JXC"],
    porcentaje_JefGob_renombrado.iloc[11]["CF"],
    porcentaje_JefGob_renombrado.iloc[11]["ULD"],
    0,
    porcentaje_JefGob_renombrado.iloc[11]["BLANCO"],
    porcentaje_JefGob_renombrado.iloc[11]["NULO"],
    porcentaje_JefGob_renombrado.iloc[11]["RECURRIDO"],
    porcentaje_JefGob_renombrado.iloc[11]["IMPUGNADO"],
    porcentaje_JefGob_renombrado.iloc[11]["OTROS"],
    porcentaje_JefGob_renombrado.iloc[12]["FIT"],
    porcentaje_JefGob_renombrado.iloc[12]["FDT"],
    porcentaje_JefGob_renombrado.iloc[12]["JXC"],
    porcentaje_JefGob_renombrado.iloc[12]["CF"],
    porcentaje_JefGob_renombrado.iloc[12]["ULD"],
    0,
    porcentaje_JefGob_renombrado.iloc[12]["BLANCO"],
    porcentaje_JefGob_renombrado.iloc[12]["NULO"],
    porcentaje_JefGob_renombrado.iloc[12]["RECURRIDO"],
    porcentaje_JefGob_renombrado.iloc[12]["IMPUGNADO"],
    porcentaje_JefGob_renombrado.iloc[12]["OTROS"],
    porcentaje_JefGob_renombrado.iloc[13]["FIT"],
    porcentaje_JefGob_renombrado.iloc[13]["FDT"],
    porcentaje_JefGob_renombrado.iloc[13]["JXC"],
    porcentaje_JefGob_renombrado.iloc[13]["CF"],
    porcentaje_JefGob_renombrado.iloc[13]["ULD"],
    0,
    porcentaje_JefGob_renombrado.iloc[13]["BLANCO"],
    porcentaje_JefGob_renombrado.iloc[13]["NULO"],
    porcentaje_JefGob_renombrado.iloc[13]["RECURRIDO"],
    porcentaje_JefGob_renombrado.iloc[13]["IMPUGNADO"],
    porcentaje_JefGob_renombrado.iloc[13]["OTROS"],
    porcentaje_JefGob_renombrado.iloc[14]["FIT"],
    porcentaje_JefGob_renombrado.iloc[14]["FDT"],
    porcentaje_JefGob_renombrado.iloc[14]["JXC"],
    porcentaje_JefGob_renombrado.iloc[14]["CF"],
    porcentaje_JefGob_renombrado.iloc[14]["ULD"],
    0,
    porcentaje_JefGob_renombrado.iloc[14]["BLANCO"],
    porcentaje_JefGob_renombrado.iloc[14]["NULO"],
    porcentaje_JefGob_renombrado.iloc[14]["RECURRIDO"],
    porcentaje_JefGob_renombrado.iloc[14]["IMPUGNADO"],
    porcentaje_JefGob_renombrado.iloc[14]["OTROS"]
])

# %%

# Junta Comunal 1:

porcentaje_Com1 = pd.read_csv("data/comuna_1/Com1_comuna_completo.csv")

porcentaje_Com1_renombrado = porcentaje_Com1.rename(columns={"NOMBRE_REGION": "Comuna",
                                                             "VOTOS_TOTALES_COM1": "TOTALES",
                                                             "PORCENTAJE_FIT_COM1": "FIT",
                                                             "PORCENTAJE_CF_COM1": "CF",
                                                             "PORCENTAJE_FDT_COM1": "FDT",
                                                             "PORCENTAJE_JXC_COM1": "JXC",
                                                             "PORCENTAJE_NOS_COM1": "NOS",
                                                             "PORCENTAJE_ULD_COM1": "ULD",
                                                             "PORCENTAJE_NULO_COM1": "NULO",
                                                             "PORCENTAJE_RECURRIDO_COM1": "RECURRIDO",
                                                             "PORCENTAJE_IMPUGNADO_COM1": "IMPUGNADO",
                                                             "PORCENTAJE_BLANCO_COM1": "BLANCO",
                                                             "PORCENTAJE_OTROS_COM1": "OTROS"},
                                                    inplace=False)

Porc_Com1 = pd.Series([
    porcentaje_Com1_renombrado.iloc[0]["FIT"],
    porcentaje_Com1_renombrado.iloc[0]["FDT"],
    porcentaje_Com1_renombrado.iloc[0]["JXC"],
    porcentaje_Com1_renombrado.iloc[0]["CF"],
    0,
    0,
    porcentaje_Com1_renombrado.iloc[0]["BLANCO"],
    porcentaje_Com1_renombrado.iloc[0]["NULO"],
    porcentaje_Com1_renombrado.iloc[0]["RECURRIDO"],
    porcentaje_Com1_renombrado.iloc[0]["IMPUGNADO"],
    porcentaje_Com1_renombrado.iloc[0]["OTROS"],
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
])

Data_Frame_General = pd.concat([Data_Frame_General, Porc_Com1], axis=1)

Data_Frame_General = Data_Frame_General.rename(columns={0: "Porc_Com1"})

# %%

# Junta Comunal 2:

porcentaje_Com2 = pd.read_csv("data/comuna_2/Com2_comuna_completo.csv")

porcentaje_Com2_renombrado = porcentaje_Com2.rename(columns={"NOMBRE_REGION": "Comuna",
                                                             "VOTOS_TOTALES_COM2": "TOTALES",
                                                             "PORCENTAJE_FIT_COM2": "FIT",
                                                             "PORCENTAJE_CF_COM2": "CF",
                                                             "PORCENTAJE_FDT_COM2": "FDT",
                                                             "PORCENTAJE_JXC_COM2": "JXC",
                                                             "PORCENTAJE_NOS_COM2": "NOS",
                                                             "PORCENTAJE_ULD_COM2": "ULD",
                                                             "PORCENTAJE_NULO_COM2": "NULO",
                                                             "PORCENTAJE_RECURRIDO_COM2": "RECURRIDO",
                                                             "PORCENTAJE_IMPUGNADO_COM2": "IMPUGNADO",
                                                             "PORCENTAJE_BLANCO_COM2": "BLANCO",
                                                             "PORCENTAJE_OTROS_COM2": "OTROS"},
                                                    inplace=False)

Porc_Com2 = pd.Series([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       porcentaje_Com2_renombrado.iloc[0]["FIT"],
                       porcentaje_Com2_renombrado.iloc[0]["FDT"],
                       porcentaje_Com2_renombrado.iloc[0]["JXC"],
                       porcentaje_Com2_renombrado.iloc[0]["CF"],
                       0,
                       0,
                       porcentaje_Com2_renombrado.iloc[0]["BLANCO"],
                       porcentaje_Com2_renombrado.iloc[0]["NULO"],
                       porcentaje_Com2_renombrado.iloc[0]["RECURRIDO"],
                       porcentaje_Com2_renombrado.iloc[0]["IMPUGNADO"],
                       porcentaje_Com2_renombrado.iloc[0]["OTROS"],
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       ])

Data_Frame_General = pd.concat([Data_Frame_General, Porc_Com2], axis=1)

Data_Frame_General = Data_Frame_General.rename(columns={0: "Porc_Com2"})


# %%

# Junta Comunal 3:

porcentaje_Com3 = pd.read_csv("data/comuna_3/Com3_comuna_completo.csv")

porcentaje_Com3_renombrado = porcentaje_Com3.rename(columns={"NOMBRE_REGION": "Comuna",
                                                             "VOTOS_TOTALES_COM3": "TOTALES",
                                                             "PORCENTAJE_FIT_COM3": "FIT",
                                                             "PORCENTAJE_CF_COM3": "CF",
                                                             "PORCENTAJE_FDT_COM3": "FDT",
                                                             "PORCENTAJE_JXC_COM3": "JXC",
                                                             "PORCENTAJE_NOS_COM3": "NOS",
                                                             "PORCENTAJE_ULD_COM3": "ULD",
                                                             "PORCENTAJE_NULO_COM3": "NULO",
                                                             "PORCENTAJE_RECURRIDO_COM3": "RECURRIDO",
                                                             "PORCENTAJE_IMPUGNADO_COM3": "IMPUGNADO",
                                                             "PORCENTAJE_BLANCO_COM3": "BLANCO",
                                                             "PORCENTAJE_OTROS_COM3": "OTROS"},
                                                    inplace=False)

Porc_Com3 = pd.Series([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       porcentaje_Com3_renombrado.iloc[0]["FIT"],
                       porcentaje_Com3_renombrado.iloc[0]["FDT"],
                       porcentaje_Com3_renombrado.iloc[0]["JXC"],
                       porcentaje_Com3_renombrado.iloc[0]["CF"],
                       0,
                       0,
                       porcentaje_Com3_renombrado.iloc[0]["BLANCO"],
                       porcentaje_Com3_renombrado.iloc[0]["NULO"],
                       porcentaje_Com3_renombrado.iloc[0]["RECURRIDO"],
                       porcentaje_Com3_renombrado.iloc[0]["IMPUGNADO"],
                       porcentaje_Com3_renombrado.iloc[0]["OTROS"],
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       ])

Data_Frame_General = pd.concat([Data_Frame_General, Porc_Com3], axis=1)

Data_Frame_General = Data_Frame_General.rename(columns={0: "Porc_Com3"})


# %%

# Junta Comunal 4:

porcentaje_Com4 = pd.read_csv("data/comuna_4/Com4_comuna_completo.csv")

porcentaje_Com4_renombrado = porcentaje_Com4.rename(columns={"NOMBRE_REGION": "Comuna",
                                                             "VOTOS_TOTALES_COM4": "TOTALES",
                                                             "PORCENTAJE_FIT_COM4": "FIT",
                                                             "PORCENTAJE_CF_COM4": "CF",
                                                             "PORCENTAJE_FDT_COM4": "FDT",
                                                             "PORCENTAJE_JXC_COM4": "JXC",
                                                             "PORCENTAJE_NOS_COM4": "NOS",
                                                             "PORCENTAJE_ULD_COM4": "ULD",
                                                             "PORCENTAJE_NULO_COM4": "NULO",
                                                             "PORCENTAJE_RECURRIDO_COM4": "RECURRIDO",
                                                             "PORCENTAJE_IMPUGNADO_COM4": "IMPUGNADO",
                                                             "PORCENTAJE_BLANCO_COM4": "BLANCO",
                                                             "PORCENTAJE_OTROS_COM4": "OTROS"},
                                                    inplace=False)

Porc_Com4 = pd.Series([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       porcentaje_Com4_renombrado.iloc[0]["FIT"],
                       porcentaje_Com4_renombrado.iloc[0]["FDT"],
                       porcentaje_Com4_renombrado.iloc[0]["JXC"],
                       porcentaje_Com4_renombrado.iloc[0]["CF"],
                       0,
                       0,
                       porcentaje_Com4_renombrado.iloc[0]["BLANCO"],
                       porcentaje_Com4_renombrado.iloc[0]["NULO"],
                       porcentaje_Com4_renombrado.iloc[0]["RECURRIDO"],
                       porcentaje_Com4_renombrado.iloc[0]["IMPUGNADO"],
                       porcentaje_Com4_renombrado.iloc[0]["OTROS"],
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       ])

Data_Frame_General = pd.concat([Data_Frame_General, Porc_Com4], axis=1)

Data_Frame_General = Data_Frame_General.rename(columns={0: "Porc_Com4"})


# %%

# Junta Comunal 5:

porcentaje_Com5 = pd.read_csv("data/comuna_5/Com5_comuna_completo.csv")

porcentaje_Com5_renombrado = porcentaje_Com5.rename(columns={"NOMBRE_REGION": "Comuna",
                                                             "VOTOS_TOTALES_COM5": "TOTALES",
                                                             "PORCENTAJE_FIT_COM5": "FIT",
                                                             "PORCENTAJE_CF_COM5": "CF",
                                                             "PORCENTAJE_FDT_COM5": "FDT",
                                                             "PORCENTAJE_JXC_COM5": "JXC",
                                                             "PORCENTAJE_NOS_COM5": "NOS",
                                                             "PORCENTAJE_ULD_COM5": "ULD",
                                                             "PORCENTAJE_NULO_COM5": "NULO",
                                                             "PORCENTAJE_RECURRIDO_COM5": "RECURRIDO",
                                                             "PORCENTAJE_IMPUGNADO_COM5": "IMPUGNADO",
                                                             "PORCENTAJE_BLANCO_COM5": "BLANCO",
                                                             "PORCENTAJE_OTROS_COM5": "OTROS"},
                                                    inplace=False)

Porc_Com5 = pd.Series([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       porcentaje_Com5_renombrado.iloc[0]["FIT"],
                       porcentaje_Com5_renombrado.iloc[0]["FDT"],
                       porcentaje_Com5_renombrado.iloc[0]["JXC"],
                       porcentaje_Com5_renombrado.iloc[0]["CF"],
                       0,
                       0,
                       porcentaje_Com5_renombrado.iloc[0]["BLANCO"],
                       porcentaje_Com5_renombrado.iloc[0]["NULO"],
                       porcentaje_Com5_renombrado.iloc[0]["RECURRIDO"],
                       porcentaje_Com5_renombrado.iloc[0]["IMPUGNADO"],
                       porcentaje_Com5_renombrado.iloc[0]["OTROS"],
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       ])

Data_Frame_General = pd.concat([Data_Frame_General, Porc_Com5], axis=1)

Data_Frame_General = Data_Frame_General.rename(columns={0: "Porc_Com5"})


# %%

# Junta Comunal 6:


porcentaje_Com6 = pd.read_csv("data/comuna_6/Com6_comuna_completo.csv")

porcentaje_Com6_renombrado = porcentaje_Com6.rename(columns={"NOMBRE_REGION": "Comuna",
                                                             "VOTOS_TOTALES_COM6": "TOTALES",
                                                             "PORCENTAJE_FIT_COM6": "FIT",
                                                             "PORCENTAJE_CF_COM6": "CF",
                                                             "PORCENTAJE_FDT_COM6": "FDT",
                                                             "PORCENTAJE_JXC_COM6": "JXC",
                                                             "PORCENTAJE_NOS_COM6": "NOS",
                                                             "PORCENTAJE_ULD_COM6": "ULD",
                                                             "PORCENTAJE_NULO_COM6": "NULO",
                                                             "PORCENTAJE_RECURRIDO_COM6": "RECURRIDO",
                                                             "PORCENTAJE_IMPUGNADO_COM6": "IMPUGNADO",
                                                             "PORCENTAJE_BLANCO_COM6": "BLANCO",
                                                             "PORCENTAJE_OTROS_COM6": "OTROS"},
                                                    inplace=False)

Porc_Com6 = pd.Series([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       porcentaje_Com6_renombrado.iloc[0]["FIT"],
                       porcentaje_Com6_renombrado.iloc[0]["FDT"],
                       porcentaje_Com6_renombrado.iloc[0]["JXC"],
                       porcentaje_Com6_renombrado.iloc[0]["CF"],
                       0,
                       0,
                       porcentaje_Com6_renombrado.iloc[0]["BLANCO"],
                       porcentaje_Com6_renombrado.iloc[0]["NULO"],
                       porcentaje_Com6_renombrado.iloc[0]["RECURRIDO"],
                       porcentaje_Com6_renombrado.iloc[0]["IMPUGNADO"],
                       porcentaje_Com6_renombrado.iloc[0]["OTROS"],
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       ])

Data_Frame_General = pd.concat([Data_Frame_General, Porc_Com6], axis=1)

Data_Frame_General = Data_Frame_General.rename(columns={0: "Porc_Com6"})


# %%

# Junta Comunal 7:

porcentaje_Com7 = pd.read_csv("data/comuna_7/Com7_comuna_completo.csv")

porcentaje_Com7_renombrado = porcentaje_Com7.rename(columns={"NOMBRE_REGION": "Comuna",
                                                             "VOTOS_TOTALES_COM7": "TOTALES",
                                                             "PORCENTAJE_FIT_COM7": "FIT",
                                                             "PORCENTAJE_CF_COM7": "CF",
                                                             "PORCENTAJE_FDT_COM7": "FDT",
                                                             "PORCENTAJE_JXC_COM7": "JXC",
                                                             "PORCENTAJE_NOS_COM7": "NOS",
                                                             "PORCENTAJE_ULD_COM7": "ULD",
                                                             "PORCENTAJE_NULO_COM7": "NULO",
                                                             "PORCENTAJE_RECURRIDO_COM7": "RECURRIDO",
                                                             "PORCENTAJE_IMPUGNADO_COM7": "IMPUGNADO",
                                                             "PORCENTAJE_BLANCO_COM7": "BLANCO",
                                                             "PORCENTAJE_OTROS_COM7": "OTROS"},
                                                    inplace=False)

Porc_Com7 = pd.Series([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       porcentaje_Com7_renombrado.iloc[0]["FIT"],
                       porcentaje_Com7_renombrado.iloc[0]["FDT"],
                       porcentaje_Com7_renombrado.iloc[0]["JXC"],
                       porcentaje_Com7_renombrado.iloc[0]["CF"],
                       0,
                       0,
                       porcentaje_Com7_renombrado.iloc[0]["BLANCO"],
                       porcentaje_Com7_renombrado.iloc[0]["NULO"],
                       porcentaje_Com7_renombrado.iloc[0]["RECURRIDO"],
                       porcentaje_Com7_renombrado.iloc[0]["IMPUGNADO"],
                       porcentaje_Com7_renombrado.iloc[0]["OTROS"],
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       ])

Data_Frame_General = pd.concat([Data_Frame_General, Porc_Com7], axis=1)

Data_Frame_General = Data_Frame_General.rename(columns={0: "Porc_Com7"})



# %%

# Junta Comunal 8:


porcentaje_Com8 = pd.read_csv("data/comuna_8/Com8_comuna_completo.csv")

porcentaje_Com8_renombrado = porcentaje_Com8.rename(columns={"NOMBRE_REGION": "Comuna",
                                                             "VOTOS_TOTALES_COM8": "TOTALES",
                                                             "PORCENTAJE_FIT_COM8": "FIT",
                                                             "PORCENTAJE_CF_COM8": "CF",
                                                             "PORCENTAJE_FDT_COM8": "FDT",
                                                             "PORCENTAJE_JXC_COM8": "JXC",
                                                             "PORCENTAJE_NOS_COM8": "NOS",
                                                             "PORCENTAJE_ULD_COM8": "ULD",
                                                             "PORCENTAJE_NULO_COM8": "NULO",
                                                             "PORCENTAJE_RECURRIDO_COM8": "RECURRIDO",
                                                             "PORCENTAJE_IMPUGNADO_COM8": "IMPUGNADO",
                                                             "PORCENTAJE_BLANCO_COM8": "BLANCO",
                                                             "PORCENTAJE_OTROS_COM8": "OTROS"},
                                                    inplace=False)

Porc_Com8 = pd.Series([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       porcentaje_Com8_renombrado.iloc[0]["FIT"],
                       porcentaje_Com8_renombrado.iloc[0]["FDT"],
                       porcentaje_Com8_renombrado.iloc[0]["JXC"],
                       porcentaje_Com8_renombrado.iloc[0]["CF"],
                       0,
                       0,
                       porcentaje_Com8_renombrado.iloc[0]["BLANCO"],
                       porcentaje_Com8_renombrado.iloc[0]["NULO"],
                       porcentaje_Com8_renombrado.iloc[0]["RECURRIDO"],
                       porcentaje_Com8_renombrado.iloc[0]["IMPUGNADO"],
                       porcentaje_Com8_renombrado.iloc[0]["OTROS"],
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       ])

Data_Frame_General = pd.concat([Data_Frame_General, Porc_Com8], axis=1)

Data_Frame_General = Data_Frame_General.rename(columns={0: "Porc_Com8"})



# %%

# Junta Comunal 9:

porcentaje_Com9 = pd.read_csv("data/comuna_9/Com9_comuna_completo.csv")

porcentaje_Com9_renombrado = porcentaje_Com9.rename(columns={"NOMBRE_REGION": "Comuna",
                                                             "VOTOS_TOTALES_COM9": "TOTALES",
                                                             "PORCENTAJE_FIT_COM9": "FIT",
                                                             "PORCENTAJE_CF_COM9": "CF",
                                                             "PORCENTAJE_FDT_COM9": "FDT",
                                                             "PORCENTAJE_JXC_COM9": "JXC",
                                                             "PORCENTAJE_NOS_COM9": "NOS",
                                                             "PORCENTAJE_ULD_COM9": "ULD",
                                                             "PORCENTAJE_NULO_COM9": "NULO",
                                                             "PORCENTAJE_RECURRIDO_COM9": "RECURRIDO",
                                                             "PORCENTAJE_IMPUGNADO_COM9": "IMPUGNADO",
                                                             "PORCENTAJE_BLANCO_COM9": "BLANCO",
                                                             "PORCENTAJE_OTROS_COM9": "OTROS"},
                                                    inplace=False)

Porc_Com9 = pd.Series([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       porcentaje_Com9_renombrado.iloc[0]["FIT"],
                       porcentaje_Com9_renombrado.iloc[0]["FDT"],
                       porcentaje_Com9_renombrado.iloc[0]["JXC"],
                       porcentaje_Com9_renombrado.iloc[0]["CF"],
                       0,
                       0,
                       porcentaje_Com9_renombrado.iloc[0]["BLANCO"],
                       porcentaje_Com9_renombrado.iloc[0]["NULO"],
                       porcentaje_Com9_renombrado.iloc[0]["RECURRIDO"],
                       porcentaje_Com9_renombrado.iloc[0]["IMPUGNADO"],
                       porcentaje_Com9_renombrado.iloc[0]["OTROS"],
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       ])

Data_Frame_General = pd.concat([Data_Frame_General, Porc_Com9], axis=1)

Data_Frame_General = Data_Frame_General.rename(columns={0: "Porc_Com9"})



# %%

# Junta Comunal 10:

porcentaje_Com10 = pd.read_csv("data/comuna_10/Com10_comuna_completo.csv")

porcentaje_Com10_renombrado = porcentaje_Com10.rename(columns={"NOMBRE_REGION": "Comuna",
                                                             "VOTOS_TOTALES_COM10": "TOTALES",
                                                             "PORCENTAJE_FIT_COM10": "FIT",
                                                             "PORCENTAJE_CF_COM10": "CF",
                                                             "PORCENTAJE_FDT_COM10": "FDT",
                                                             "PORCENTAJE_JXC_COM10": "JXC",
                                                             "PORCENTAJE_NOS_COM10": "NOS",
                                                             "PORCENTAJE_ULD_COM10": "ULD",
                                                             "PORCENTAJE_NULO_COM10": "NULO",
                                                             "PORCENTAJE_RECURRIDO_COM10": "RECURRIDO",
                                                             "PORCENTAJE_IMPUGNADO_COM10": "IMPUGNADO",
                                                             "PORCENTAJE_BLANCO_COM10": "BLANCO",
                                                             "PORCENTAJE_OTROS_COM10": "OTROS"},
                                                    inplace=False)

Porc_Com10 = pd.Series([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       porcentaje_Com10_renombrado.iloc[0]["FIT"],
                       porcentaje_Com10_renombrado.iloc[0]["FDT"],
                       porcentaje_Com10_renombrado.iloc[0]["JXC"],
                       porcentaje_Com10_renombrado.iloc[0]["CF"],
                       0,
                       0,
                       porcentaje_Com10_renombrado.iloc[0]["BLANCO"],
                       porcentaje_Com10_renombrado.iloc[0]["NULO"],
                       porcentaje_Com10_renombrado.iloc[0]["RECURRIDO"],
                       porcentaje_Com10_renombrado.iloc[0]["IMPUGNADO"],
                       porcentaje_Com10_renombrado.iloc[0]["OTROS"],
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       ])

Data_Frame_General = pd.concat([Data_Frame_General, Porc_Com10], axis=1)

Data_Frame_General = Data_Frame_General.rename(columns={0: "Porc_Com10"})



# %%

# Junta Comunal 11:

porcentaje_Com11 = pd.read_csv("data/comuna_11/Com11_comuna_completo.csv")

porcentaje_Com11_renombrado = porcentaje_Com11.rename(columns={"NOMBRE_REGION": "Comuna",
                                                             "VOTOS_TOTALES_COM11": "TOTALES",
                                                             "PORCENTAJE_FIT_COM11": "FIT",
                                                             "PORCENTAJE_CF_COM11": "CF",
                                                             "PORCENTAJE_FDT_COM11": "FDT",
                                                             "PORCENTAJE_JXC_COM11": "JXC",
                                                             "PORCENTAJE_NOS_COM11": "NOS",
                                                             "PORCENTAJE_ULD_COM11": "ULD",
                                                             "PORCENTAJE_NULO_COM11": "NULO",
                                                             "PORCENTAJE_RECURRIDO_COM11": "RECURRIDO",
                                                             "PORCENTAJE_IMPUGNADO_COM11": "IMPUGNADO",
                                                             "PORCENTAJE_BLANCO_COM11": "BLANCO",
                                                             "PORCENTAJE_OTROS_COM11": "OTROS"},
                                                    inplace=False)

Porc_Com11 = pd.Series([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       porcentaje_Com11_renombrado.iloc[0]["FIT"],
                       porcentaje_Com11_renombrado.iloc[0]["FDT"],
                       porcentaje_Com11_renombrado.iloc[0]["JXC"],
                       porcentaje_Com11_renombrado.iloc[0]["CF"],
                       0,
                       0,
                       porcentaje_Com11_renombrado.iloc[0]["BLANCO"],
                       porcentaje_Com11_renombrado.iloc[0]["NULO"],
                       porcentaje_Com11_renombrado.iloc[0]["RECURRIDO"],
                       porcentaje_Com11_renombrado.iloc[0]["IMPUGNADO"],
                       porcentaje_Com11_renombrado.iloc[0]["OTROS"],
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       ])

Data_Frame_General = pd.concat([Data_Frame_General, Porc_Com11], axis=1)

Data_Frame_General = Data_Frame_General.rename(columns={0: "Porc_Com11"})


# %%

# Junta Comunal 12:


porcentaje_Com12 = pd.read_csv("data/comuna_12/Com12_comuna_completo.csv")

porcentaje_Com12_renombrado = porcentaje_Com12.rename(columns={"NOMBRE_REGION": "Comuna",
                                                             "VOTOS_TOTALES_COM12": "TOTALES",
                                                             "PORCENTAJE_FIT_COM12": "FIT",
                                                             "PORCENTAJE_CF_COM12": "CF",
                                                             "PORCENTAJE_FDT_COM12": "FDT",
                                                             "PORCENTAJE_JXC_COM12": "JXC",
                                                             "PORCENTAJE_NOS_COM12": "NOS",
                                                             "PORCENTAJE_ULD_COM12": "ULD",
                                                             "PORCENTAJE_NULO_COM12": "NULO",
                                                             "PORCENTAJE_RECURRIDO_COM12": "RECURRIDO",
                                                             "PORCENTAJE_IMPUGNADO_COM12": "IMPUGNADO",
                                                             "PORCENTAJE_BLANCO_COM12": "BLANCO",
                                                             "PORCENTAJE_OTROS_COM12": "OTROS"},
                                                    inplace=False)

Porc_Com12 = pd.Series([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       porcentaje_Com12_renombrado.iloc[0]["FIT"],
                       porcentaje_Com12_renombrado.iloc[0]["FDT"],
                       porcentaje_Com12_renombrado.iloc[0]["JXC"],
                       porcentaje_Com12_renombrado.iloc[0]["CF"],
                       0,
                       0,
                       porcentaje_Com12_renombrado.iloc[0]["BLANCO"],
                       porcentaje_Com12_renombrado.iloc[0]["NULO"],
                       porcentaje_Com12_renombrado.iloc[0]["RECURRIDO"],
                       porcentaje_Com12_renombrado.iloc[0]["IMPUGNADO"],
                       porcentaje_Com12_renombrado.iloc[0]["OTROS"],
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       ])

Data_Frame_General = pd.concat([Data_Frame_General, Porc_Com12], axis=1)

Data_Frame_General = Data_Frame_General.rename(columns={0: "Porc_Com12"})


# %%

# Junta Comunal 13:

porcentaje_Com13 = pd.read_csv("data/comuna_13/Com13_comuna_completo.csv")

porcentaje_Com13_renombrado = porcentaje_Com13.rename(columns={"NOMBRE_REGION": "Comuna",
                                                             "VOTOS_TOTALES_COM13": "TOTALES",
                                                             "PORCENTAJE_FIT_COM13": "FIT",
                                                             "PORCENTAJE_CF_COM13": "CF",
                                                             "PORCENTAJE_FDT_COM13": "FDT",
                                                             "PORCENTAJE_JXC_COM13": "JXC",
                                                             "PORCENTAJE_NOS_COM13": "NOS",
                                                             "PORCENTAJE_ULD_COM13": "ULD",
                                                             "PORCENTAJE_NULO_COM13": "NULO",
                                                             "PORCENTAJE_RECURRIDO_COM13": "RECURRIDO",
                                                             "PORCENTAJE_IMPUGNADO_COM13": "IMPUGNADO",
                                                             "PORCENTAJE_BLANCO_COM13": "BLANCO",
                                                             "PORCENTAJE_OTROS_COM13": "OTROS"},
                                                    inplace=False)

Porc_Com13 = pd.Series([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       porcentaje_Com13_renombrado.iloc[0]["FIT"],
                       porcentaje_Com13_renombrado.iloc[0]["FDT"],
                       porcentaje_Com13_renombrado.iloc[0]["JXC"],
                       porcentaje_Com13_renombrado.iloc[0]["CF"],
                       0,
                       0,
                       porcentaje_Com13_renombrado.iloc[0]["BLANCO"],
                       porcentaje_Com13_renombrado.iloc[0]["NULO"],
                       porcentaje_Com13_renombrado.iloc[0]["RECURRIDO"],
                       porcentaje_Com13_renombrado.iloc[0]["IMPUGNADO"],
                       porcentaje_Com13_renombrado.iloc[0]["OTROS"],
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       ])

Data_Frame_General = pd.concat([Data_Frame_General, Porc_Com13], axis=1)

Data_Frame_General = Data_Frame_General.rename(columns={0: "Porc_Com13"})



# %%

# Junta Comunal 14:


porcentaje_Com14 = pd.read_csv("data/comuna_14/Com14_comuna_completo.csv")

porcentaje_Com14_renombrado = porcentaje_Com14.rename(columns={"NOMBRE_REGION": "Comuna",
                                                             "VOTOS_TOTALES_COM14": "TOTALES",
                                                             "PORCENTAJE_FIT_COM14": "FIT",
                                                             "PORCENTAJE_CF_COM14": "CF",
                                                             "PORCENTAJE_FDT_COM14": "FDT",
                                                             "PORCENTAJE_JXC_COM14": "JXC",
                                                             "PORCENTAJE_NOS_COM14": "NOS",
                                                             "PORCENTAJE_ULD_COM14": "ULD",
                                                             "PORCENTAJE_NULO_COM14": "NULO",
                                                             "PORCENTAJE_RECURRIDO_COM14": "RECURRIDO",
                                                             "PORCENTAJE_IMPUGNADO_COM14": "IMPUGNADO",
                                                             "PORCENTAJE_BLANCO_COM14": "BLANCO",
                                                             "PORCENTAJE_OTROS_COM14": "OTROS"},
                                                    inplace=False)

Porc_Com14 = pd.Series([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       porcentaje_Com14_renombrado.iloc[0]["FIT"],
                       porcentaje_Com14_renombrado.iloc[0]["FDT"],
                       porcentaje_Com14_renombrado.iloc[0]["JXC"],
                       porcentaje_Com14_renombrado.iloc[0]["CF"],
                       0,
                       0,
                       porcentaje_Com14_renombrado.iloc[0]["BLANCO"],
                       porcentaje_Com14_renombrado.iloc[0]["NULO"],
                       porcentaje_Com14_renombrado.iloc[0]["RECURRIDO"],
                       porcentaje_Com14_renombrado.iloc[0]["IMPUGNADO"],
                       porcentaje_Com14_renombrado.iloc[0]["OTROS"],
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       ])

Data_Frame_General = pd.concat([Data_Frame_General, Porc_Com14], axis=1)

Data_Frame_General = Data_Frame_General.rename(columns={0: "Porc_Com14"})


# %%

# Junta Comunal 15:

porcentaje_Com15 = pd.read_csv("data/comuna_15/Com15_comuna_completo.csv")

porcentaje_Com15_renombrado = porcentaje_Com15.rename(columns={"NOMBRE_REGION": "Comuna",
                                                             "VOTOS_TOTALES_COM15": "TOTALES",
                                                             "PORCENTAJE_FIT_COM15": "FIT",
                                                             "PORCENTAJE_CF_COM15": "CF",
                                                             "PORCENTAJE_FDT_COM15": "FDT",
                                                             "PORCENTAJE_JXC_COM15": "JXC",
                                                             "PORCENTAJE_NOS_COM15": "NOS",
                                                             "PORCENTAJE_ULD_COM15": "ULD",
                                                             "PORCENTAJE_NULO_COM15": "NULO",
                                                             "PORCENTAJE_RECURRIDO_COM15": "RECURRIDO",
                                                             "PORCENTAJE_IMPUGNADO_COM15": "IMPUGNADO",
                                                             "PORCENTAJE_BLANCO_COM15": "BLANCO",
                                                             "PORCENTAJE_OTROS_COM15": "OTROS"},
                                                    inplace=False)

Porc_Com15 = pd.Series([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       porcentaje_Com15_renombrado.iloc[0]["FIT"],
                       porcentaje_Com15_renombrado.iloc[0]["FDT"],
                       porcentaje_Com15_renombrado.iloc[0]["JXC"],
                       porcentaje_Com15_renombrado.iloc[0]["CF"],
                       0,
                       0,
                       porcentaje_Com15_renombrado.iloc[0]["BLANCO"],
                       porcentaje_Com15_renombrado.iloc[0]["NULO"],
                       porcentaje_Com15_renombrado.iloc[0]["RECURRIDO"],
                       porcentaje_Com15_renombrado.iloc[0]["IMPUGNADO"],
                       porcentaje_Com15_renombrado.iloc[0]["OTROS"],
                       ])

Data_Frame_General = pd.concat([Data_Frame_General, Porc_Com15], axis=1)

Data_Frame_General = Data_Frame_General.rename(columns={0: "Porc_Com15"})

Data_Frame_General.to_csv("Data_Frame_General.csv")
