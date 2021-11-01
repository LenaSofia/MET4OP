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

Data_Frame_General.to_csv("Data_Frame_General_Sin_Comuneros.csv")

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
         porcentaje_Com1_renombrado.iloc[0]["OTROS"]
        ])

Data_Frame_General = pd.concat([Data_Frame_General, Porc_Com1], axis=1)

Data_Frame_General = Data_Frame_General.rename(columns={0:"Porc_Com1"})


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

Porc_Com2 = pd.Series([
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
         porcentaje_Com2_renombrado.iloc[0]["OTROS"]
        ])

Data_Frame_General = pd.concat([Data_Frame_General, Porc_Com2], axis=1)

Data_Frame_General = Data_Frame_General.rename(columns={0:"Porc_Com2"})

print(Data_Frame_General)


# %%

# Junta Comunal 3:

# FIT

# FDT

# JXC

# CS

# ULD

# NOS

# NULO

# BLANCO

# RECURRIDO

# IMPUGNADO

# OTROS


# %%

# Junta Comunal 4:

# FIT

# FDT

# JXC

# CS

# ULD

# NOS

# NULO

# BLANCO

# RECURRIDO

# IMPUGNADO

# OTROS


# %%

# Junta Comunal 5:

# FIT

# FDT

# JXC

# CS

# ULD

# NOS

# NULO

# BLANCO

# RECURRIDO

# IMPUGNADO

# OTROS


# %%

# Junta Comunal 6:

# FIT

# FDT

# JXC

# CS

# ULD

# NOS

# NULO

# BLANCO

# RECURRIDO

# IMPUGNADO

# OTROS


# %%

# Junta Comunal 7:

# FIT

# FDT

# JXC

# CS

# ULD

# NOS

# NULO

# BLANCO

# RECURRIDO

# IMPUGNADO

# OTROS


# %%

# Junta Comunal 8:

# FIT

# FDT

# JXC

# CS

# ULD

# NOS

# NULO

# BLANCO

# RECURRIDO

# IMPUGNADO

# OTROS


# %%

# Junta Comunal 9:

# FIT

# FDT

# JXC

# CS

# ULD

# NOS

# NULO

# BLANCO

# RECURRIDO

# IMPUGNADO

# OTROS


# %%

# Junta Comunal 10:

# FIT

# FDT

# JXC

# CS

# ULD

# NOS

# NULO

# BLANCO

# RECURRIDO

# IMPUGNADO

# OTROS


# %%

# Junta Comunal 11:

# FIT

# FDT

# JXC

# CS

# ULD

# NOS

# NULO

# BLANCO

# RECURRIDO

# IMPUGNADO

# OTROS


# %%

# Junta Comunal 12:

# FIT

# FDT

# JXC

# CS

# ULD

# NOS

# NULO

# BLANCO

# RECURRIDO

# IMPUGNADO

# OTROS


# %%

# Junta Comunal 13:

# FIT

# FDT

# JXC

# CS

# ULD

# NOS

# NULO

# BLANCO

# RECURRIDO

# IMPUGNADO

# OTROS


# %%

# Junta Comunal 14:

# FIT

# FDT

# JXC

# CS

# ULD

# NOS

# NULO

# BLANCO

# RECURRIDO

# IMPUGNADO

# OTROS


# %%

# Junta Comunal 15:

# FIT

# FDT

# JXC

# CS

# ULD

# NOS

# NULO

# BLANCO

# RECURRIDO

# IMPUGNADO

# OTROS
