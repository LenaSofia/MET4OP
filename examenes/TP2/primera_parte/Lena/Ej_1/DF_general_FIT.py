import pandas as pd

DF_general_FIT = pd.read_csv('Data_Frame_General.csv')

DF_general_FIT = DF_general_FIT.drop([])

DF_GENERAL_FIT_idx=DF_general_FIT[DF_general_FIT["Partido"]!="FIT"].index
DF_general_FIT=DF_general_FIT.drop(DF_GENERAL_FIT_idx)

DF_general_FIT.to_csv('DF_general_FIT.csv')