import pandas as pd
import matplotlib.pyplot as plt

DF = pd.read_csv("Data_Frame_General.csv")

print(DF)
DF.drop(DF.columns[[0, 1]], axis=1, inplace=True)
DF.set_index('Partido', inplace=True)
print(DF)

DF = DF.transpose()
print(DF)

for y in range(1,18):
    for x in range(0,165):
        if DF.iloc[y][x] == 0.0:
            DF.iloc[y][x] = 1.0

print(DF)

corr_DF = DF.corr(method='pearson')

plt.matshow(corr_DF)
plt.show()
print(corr_DF)

corr_DF.to_csv("corralcion.csv")