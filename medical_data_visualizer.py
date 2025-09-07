import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv') #estou usando o comando do pandas read_csv para atribuir a tabela medical_examination para a variável df 

# 2 

height_metros = df["height"] /100 # Convertendo de centimetros para metros 
df['overweight'] = (df["weight"] / (height_metros **2) > 25).astype(int)# Criei uma variável do df chamada "overweight" e atribuí um expressão que seleciona a coluna "weight" sendo dividida pela variável "height_metros",que criei para converter cm em metros, multiplicando pelo seu quadrado. Onde valores menores do que 25 representam false = 0(não estão acima do peso) ou 1, onde a expressão é true e recebe o inteiro 1.

# 3
df["cholesterol"] = (df["cholesterol"] > 1).astype(int) #Aqui eu criei uma variável onde se o valor presente for maior do que 1 ele recebe o valor true ou 1 (Ruim), e se for menor do que 1 recebe falso ou saudável(bom) 
df["gluc"] = (df['gluc'] > 1).astype(int)#Mesma coisa que fiz com a variável de cima só que para a coluna gluc

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]) # Precisei da ajuda da AI do google para lembrar da estrutura do pd.melt. Nessa linha nos usamos o pd.melt para "derreter" o dataframe para ter a coluna cardio como ID e as variaveis (value_vars) como linhas.


    # 6
    #esse codigo vai agrupar por cardio, variável e valor contando as ocorrências e renomear a contagem para 'total'
    df_cat = df_cat.value_counts(["cardio", "variable", "value"]).reset_index(name="total")# nessa linha usamos o metodo .value_counts para pegar todas as ocorrencias de cada variavel e agrupar em uma nova coluna total
    

    # 7 - Aqui preciso fazer um codigo para desenhar o gráfico categórico com barras por variável e painéis separados por cardio (precisei de ajuda da AI nesse, pois nao sabia de todos as funcoes do metodo catplot)
    g = sns.catplot(data=df_cat,x="variable",y="total",hue="value",col="cardio",kind="bar")

    # 8 - Atribuindo a figura gerada pelo comando g.fig a uma variavel figura 
    fig = g.fig

    # 9
    fig.savefig('catplot.png') #Salvei a imagem como catplot.png
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
