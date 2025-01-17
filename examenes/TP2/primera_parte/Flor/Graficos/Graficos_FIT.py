# %%
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

# %%
#Grafico votos diputados nacionales por comuna partido FIT
votos_dipnac_grafico_1 = pd.read_csv("DipNac_FIT_comuna.csv")
sns.set(style = 'darkgrid')
sns.relplot(x = 'VOTOS_FIT_DIPNAC', y = 'NOMBRE_REGION', data= votos_dipnac_grafico_1)

#Grafico votos presidenciales por comuna partido FIT
votos_pres_grafico_1 = pd.read_csv("pres_FIT_comuna.csv")
sns.set(style = 'darkgrid')
sns.relplot(x = 'VOTOS_AGRUPACION', y = 'NOMBRE_REGION', data= votos_pres_grafico_1, row="Votos Agrupación", col= "Comunas", )

# %%
#Grafico votos presidenciales por comuna partido FIT
votos_pres_grafico_1 = pd.read_csv("pres_FIT_comuna.csv",)
sns.set(style = 'darkgrid')
sns.relplot(x = 'VOTOS_AGRUPACION', y = 'NOMBRE_REGION', data= votos_pres_grafico_1)

# %%
#Grafico Pie Chart. Porcentajes de votos presidenciales por comunas de partido FIT
#df =  pd.read_csv('pres_FIT_comuna.csv')
#nombre_region = df["NOMBRE_REGION"]
#porcentaje_agrupacion = df["PORCENTAJE_AGRUPACION"]
#colors = ["#C0C0C0", "pink", "#FF0000", "#800000", "#FFFF00", "#808000", "#00FF00", "#008000", "#00FFFF", "#008080","#0000FF", "#000080", "#FF00FF", "#800080", "#FFFFFF"] 
#plt.pie(porcentaje_agrupacion, labels=nombre_region, colors=colors,
#autopct='%1.1f%%', shadow=True, startangle=140)
#plt.title("Porcentajes de voto presidenciales por comunas de partido FIT")
#plt.show()

# %%
g = sns.pairplot(futbol[['Pts_2014','inversion_abs','inversion_relativa','valor','Pos_Fecha_30','ascenso']], plot_kws={'color':'red'})
# %%
#Grafico pie chart. Porcentajes de voto diputados nacionales por comunas de partido FIT
df =  pd.read_csv("DipNac_FIT_comuna.csv")
nombre_region = df["NOMBRE_REGION"]
porcentaje_agrupacion = df["PORCENTAJE_FIT_DIPNAC"]
colors = ["#C0C0C0", "pink", "#FF0000", "#800000", "#FFFF00", "#808000", "#00FF00", "#008000", "#00FFFF", "#008080","#0000FF", "#000080", "#FF00FF", "#800080", "#FFFFFF"]
plt.pie(porcentaje_agrupacion, labels=nombre_region, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Porcentajes de voto a diputados por comunas de partido FIT")
plt.show()

# %%
#Gráfico de barras. Porcentaje de votos presidenciaeles por partido en cada comuna.
colors = ["#C0C0C0", "#000000", "#FF0000", "#800000", "#FFFF00", "#808000", "#00FF00", "#008000", "#00FFFF", "#008080","#0000FF", "#000080", "#FF00FF", "#800080", "#FFFFFF"]
df =  pd.read_csv('pres_FIT_comuna.csv')
eje_x = df["NOMBRE_REGION"]
eje_y = df["PORCENTAJE_AGRUPACION"]
plt.bar(eje_x, eje_y, color=colors)
plt.xticks(rotation=90)
plt.ylabel('Porcentajes a voto presidencial')
plt.xlabel('Comunas')
plt.title('Porcentaje de votos al FIT por comuna')
plt.show()

df =  pd.read_csv('pres_BLANCO_comuna.csv')
eje_x = df["NOMBRE_REGION"]
eje_y = df["PORCENTAJE_BLANCO_PRES"]
plt.bar(eje_x, eje_y, color=colors)
plt.xticks(rotation=90)
plt.ylabel('Porcentajes a voto presidencial')
plt.xlabel('Comunas')
plt.title('Porcentaje de votos blancos por comuna')
plt.show()

df =  pd.read_csv('pres_CF_comuna.csv')
eje_x = df["NOMBRE_REGION"]
eje_y = df["PORCENTAJE_CF_PRES"]
plt.bar(eje_x, eje_y, color=colors)
plt.xticks(rotation=90)
plt.ylabel('Porcentajes a voto presidencial')
plt.xlabel('Comunas')
plt.title('Porcentaje de votos a CF por comuna')
plt.show()

df =  pd.read_csv('pres_FDT_comuna.csv')
eje_x = df["NOMBRE_REGION"]
eje_y = df["PORCENTAJE_FDT_PRES"]
plt.bar(eje_x, eje_y, color=colors)
plt.xticks(rotation=90)
plt.ylabel('Porcentajes a voto presidencial')
plt.xlabel('Comunas')
plt.title('Porcentaje de votos a FDT por comuna')
plt.show()


df =  pd.read_csv('pres_IMPUGNADO_comuna.csv')
eje_x = df["NOMBRE_REGION"]
eje_y = df["PORCENTAJE_IMPUGNADO_PRES"]
plt.bar(eje_x, eje_y, color=colors)
plt.xticks(rotation=90)
plt.ylabel('Porcentajes a voto presidencial')
plt.xlabel('Comunas')
plt.title('Porcentaje de votos impugnados por comuna')
plt.show()

df =  pd.read_csv('pres_JXC_comuna.csv')
eje_x = df["NOMBRE_REGION"]
eje_y = df["PORCENTAJE_JXC_PRES"]
plt.bar(eje_x, eje_y, color=colors)
plt.xticks(rotation=90)
plt.ylabel('Porcentajes a voto presidencial')
plt.xlabel('Comunas')
plt.title('Porcentaje de votos a JXC por comuna')
plt.show()

df =  pd.read_csv('pres_NOS_comuna.csv')
eje_x = df["NOMBRE_REGION"]
eje_y = df["PORCENTAJE_NOS_PRES"]
plt.bar(eje_x, eje_y, color=colors)
plt.xticks(rotation=90)
plt.ylabel('Porcentajes a voto presidencial')
plt.xlabel('Comunas')
plt.title('Porcentaje de votos a NOS por comuna')
plt.show()

df =  pd.read_csv('pres_NULO_comuna.csv')
eje_x = df["NOMBRE_REGION"]
eje_y = df["PORCENTAJE_NULO_PRES"]
plt.bar(eje_x, eje_y, color=colors)
plt.xticks(rotation=90)
plt.ylabel('Porcentajes a voto presidencial')
plt.xlabel('Comunas')
plt.title('Porcentaje de votos nulos por comuna')
plt.show()

df =  pd.read_csv('pres_RECURRIDO_comuna.csv')
eje_x = df["NOMBRE_REGION"]
eje_y = df["PORCENTAJE_RECURRIDO_PRES"]
plt.bar(eje_x, eje_y, color=colors)
plt.xticks(rotation=90)
plt.ylabel('Porcentajes a voto presidencial')
plt.xlabel('Comunas')
plt.title('Porcentaje de votos recurridos por comuna')
plt.show()

df =  pd.read_csv('pres_ULD_comuna.csv')
eje_x = df["NOMBRE_REGION"]
eje_y = df["PORCENTAJE_ULD_PRES"]
plt.bar(eje_x, eje_y, color=colors)
plt.xticks(rotation=90)
plt.ylabel('Porcentajes a voto presidencial')
plt.xlabel('Comunas')
plt.title('Porcentaje de votos a ULD por comuna')
plt.show()

# %%
colors = ["#C0C0C0", "#000000", "#FF0000", "#800000", "#FFFF00", "#808000", "#00FF00", "#008000", "#00FFFF", "#008080","#0000FF", "#000080", "#FF00FF", "#800080", "#FFFFFF"]
df =  pd.read_csv('Data_Frame_General_Sin_Comuneros.csv')
eje_x = df["Partido"]
eje_y = df["Porc_Pres"]
plt.bar(eje_x, eje_y, color=colors)
plt.xticks(rotation=90)
plt.ylabel('Porcentajes a voto presidencial')
plt.xlabel('Comunas')
plt.title('Porcentaje de votos blancos por comuna')
plt.show()
# %%
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()
# %%



#Grafico comparacion de votos a diputados a FIT y FDT por comuna

# Fixing random state for reproducibility

df =  pd.read_csv('Data_Frame_General_Sin_Comuneros.csv')

plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()

# %%
colors = ["#C0C0C0", "#000000", "#FF0000", "#800000", "#FFFF00", "#808000", "#00FF00", "#008000", "#00FFFF", "#008080","#0000FF", "#000080", "#FF00FF", "#800080", "#FFFFFF"]
df =  pd.read_csv('distrib_DipNac_comuna')
eje_x = df["NOMBRE_REGION"]
eje_y = df["VOTOS_FDT_DIPNAC"]
plt.bar(eje_x, eje_y, color=colors)
plt.xticks(rotation=90)
plt.ylabel('Porcentajes a voto presidencial')
plt.xlabel('Comunas')
plt.title('Porcentaje de votos blancos por comuna')
plt.show()
# %%
