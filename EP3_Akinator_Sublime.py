import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt 
import random
from random import randint

xl = pd.ExcelFile("EP3_dados.xlsx")
xl.sheet_names
['Planilha1']
df = xl.parse()

print("Olá, e bem vindo(a) ao Gênio de DeSoft!!\nPeço para que pense em alguma pessoa que fez a matéria de DeSoft nesse semestre.\nJá pensou?\nÓtimo, agora vou adivinhar quem é essa pessoa que você está pensando!!\nBom jogo!!\n")

dic_salas = {1 : "A", 2 : "B", 3 : "C"}
dic_engenharias = {1 : "Mecânica", 2 : "Mecatrônica", 3 : "de Computação"}
dic_times = {1 : "o Santos", 2 : "o Corinthians", 3 : "o Palmeiras", 4 : "o São Paulo", 5 : "o Flamengo", 6 : "time nenhum"}
dic_idade = {1 : 17, 2 : 18, 3 : 19, 4 : 20, 5 : 21, 6 : 23, 7 : 43}
dic_olhos = {1 : "verde", 2 : "azul", 3 : "castanho"}
dic_cabelo = {1 : "castanho", 2 : "preto", 3 : "loiro"}
dic_musica = {1 : "Pop", 2 : "Rock", 3 : "Rap", 4 : "Gospel", 5 : "Metal", 6 : "Sertanejo", 7 : "Funk", 8 : "Eletro", 9 : "Samba", 10 : "Tecno"}
dic_cor = {1 : "roxo", 2 : "azul", 3 : "verde", 4 : "vermelho", 5 : "cinza", 6 : "preto"}
perguntas = {1 : "Essa pessoa é da sala {} ?".format(dic_salas[randint(1,3)]), 
             2 : "Essa pessoa é de Engenharia {} ?".format(dic_engenharias[randint(1,3)]),
             3 : "Essa pessoa torce para {} ?".format(dic_times[randint(1,6)]),
             4 : "Essa pessoa têm {} anos?".format(dic_idade[randint(1,7)]),
             5 : "Ela usa óculos ?",
             6 : "Ela nasceu na cidade de SP ?",
             7 : "Ela faz academia ?",
             8 : "Ela dirige ?",
             9 : "Qual tipo de celular ela prefere ?",
             10 : "Ela namora ?",
             11 : "Ela já viajou para fora do Brasil ?",
             12 : "Essa pessoa têm os olhos de cor {} ?".format(dic_olhos[randint(1,3)]),
             13 : "O cabelo dessa pessoa é {} ?".format(dic_cabelo[randint(1,3)]),
             14 : "O tipo de música favorita dessa pessoa é {} ?".format(dic_musica[randint(1,10)]),
             15 : "Onde ela gostaria de morar ?",
             16 : "Ela têm irmãos ou irmãs ?",
             17 : "Ela prefere salgado ou doce ?",
             18 : "A cor favorita dessa pessoa é {} ?".format(dic_cor[randint(1,6)]),
             19 : "Ela prefere carro ou avião ?",
             20 : "Ela prefere frio ou calor ?",
             21 : "Ela gosta de esportes ?",
             22 : "Ela foi para o Econo 2017 ?",
             23 : "Ela já trabalhou ?",
             24 : "Ela prefere chá ou café ?",
             25 : "Ela prefere filmes ou séries ?",
             26 : "Ela já viu neve ?"}

respostas = {1 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            2 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            3 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            4 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            5 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            6 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            7 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            8 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            9 : "1 - Android\n2 - iPhone\n3 - Não sei\n",
            10 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            11 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            12 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            13 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            14 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            15 : "1 - Casa\n2 - Apartamento\n3 - Não sei\n",
            16 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            17 : "1 - Salgado\n2 - Doce\n3 - Não sei\n",
            18 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            19 : "1 - Carro\n2 - Avião\n3 - Não sei\n",
            20 : "1 - Frio\n2 - Calor\n3 - Não sei\n",
            21 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            22 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            23 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            24 : "1 - Chá\n2 - Café\n3 - Não sei\n",
            25 : "1 - Filmes\n2 - Séries\n3 - Não sei\n",
            26 : "1 - Sim\n2 - Não\n3 - Não sei\n"}

p = random.sample(range(1,27), 26)
for i in range(len(p)):
    print(perguntas[p[i]])
    x = int(input((respostas[p[i]])))
    if x == 3:
        break
    if p[i] == 1 or p[i] == 2 or p[i] == 3 or p[i] == 12 or p[i] == 13 or p[i] == 14 or p[i] == 18:
        if x == 1:
            df = df[(df.iloc[:, p[i]-1] == perguntas[p[i]].split()[-2])]
        if x == 2:
            df = df[(df.iloc[:, p[i]-1] != perguntas[p[i]].split()[-2])]
    if p[i] == 4:
        if x == 1:
            df = df[(df.iloc[:, p[i]-1] == int(perguntas[p[i]].split()[-2]))]
        if x == 2:
            df = df[(df.iloc[:, p[i]-1] != int(perguntas[p[i]].split()[-2]))]
    if p[i] == 5 or p[i] == 6 or p[i] == 7 or p[i] == 8 or p[i] == 10 or p[i] == 11 or p[i] == 16 or p[i] == 21 or p[i] == 22 or p[i] == 23 or p[i] == 26:
        if x == 1:
            df = df[(df.iloc[:, p[i]-1] == "Sim")]
        if x == 2:
            df = df[(df.iloc[:, p[i]-1] == "Não")]
    if p[i] == 9:
        if x == 1:
            df = df[(df.iloc[:, p[i]-1] == "Android")]
        if x == 2:
            df = df[(df.iloc[:, p[i]-1] == "iPhone")]
    if p[i] == 15:
        if x == 1:
            df = df[(df.iloc[:, p[i]-1] == "Casa")]
        if x == 2:
            df = df[(df.iloc[:, p[i]-1] == "Apartamento")]
    if p[i] == 17:
        if x == 1:
            df = df[(df.iloc[:, p[i]-1] == "Salgado")]
        if x == 2:
            df = df[(df.iloc[:, p[i]-1] == "Doce")]
    if p[i] == 19:
        if x == 1:
            df = df[(df.iloc[:, p[i]-1] == "Carro")]
        if x == 2:
            df = df[(df.iloc[:, p[i]-1] == "Avião")]
    if p[i] == 20:
        if x == 1:
            df = df[(df.iloc[:, p[i]-1] == "Frio")]
        if x == 2:
            df = df[(df.iloc[:, p[i]-1] == "Calor")]
    if p[i] == 24:
        if x == 1:
            df = df[(df.iloc[:, p[i]-1] == "Chá")]
        if x == 2:
            df = df[(df.iloc[:, p[i]-1] == "Café")]
    if p[i] == 25:
        if x == 1:
            df = df[(df.iloc[:, p[i]-1] == "Filme")]
        if x == 2:
            df = df[(df.iloc[:, p[i]-1] == "Série")]
    if len(df) == 1:
        break
print("A pessoa que você está pensando deve ser o {}!!".format(list(df.index)[0]))
