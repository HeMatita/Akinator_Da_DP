# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:13:49 2017

@author: Matheus
"""

import pygame
import time
import random
 
pygame.init()

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt 
from random import randint

xl = pd.ExcelFile("EP3_dados.xlsx")
xl.sheet_names
['Planilha1']
df = xl.parse()

print("Olá, e bem vindo(a) ao Gênio de DeSoft!!\nPeço para que pense em alguma pessoa que fez a matéria de DeSoft nesse semestre.\nJá pensou?\nÓtimo, agora vou adivinhar quem é essa pessoa que você está pensando!!\nBom jogo!!\n")

dic_salas = {1 : "A", 2 : "B", 3 : "C"}
dic_engenharias = {1 : "Engenharia Mecânica", 2 : "Engenharia Mecatrônica", 3 : "Engenharia de Computação", 4 : "Arquitetura"}
dic_times = {1 : "o Santos", 2 : "o Corinthians", 3 : "o Palmeiras", 4 : "o São Paulo", 5 : "o Flamengo", 6 : "time nenhum"}
dic_idade = {1 : 17, 2 : 18, 3 : 19, 4 : 20, 5 : 21, 6 : 22, 7 : 23, 8 : 43}
dic_olhos = {1 : "verde", 2 : "azul", 3 : "castanho"}
dic_cabelo = {1 : "castanho", 2 : "preto", 3 : "loiro"}
dic_musica = {1 : "Pop", 2 : "Rock", 3 : "Rap", 4 : "Gospel", 5 : "Metal", 6 : "Sertanejo", 7 : "Funk", 8 : "Eletro", 9 : "Samba", 10 : "Tecno"}
dic_cor = {1 : "roxo", 2 : "azul", 3 : "verde", 4 : "vermelho", 5 : "cinza", 6 : "preto", 7 : "rosa"}
dic_desc = {1 : "portuguesa", 2 : "italiana", 3 : "húngara", 4 : "libanesa", 5 : "espanhola", 6 : "árabe", 7 : "africana", 8 : "austríaca", 9 : "polonesa", 10 : "alemã", 11 : "nórdica"}

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
            26 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            27 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            28 : "1 - Bolacha\n2 - Biscoito\n3 - Não sei\n",
            29 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            30 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            31 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            32 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            33 : "1 - Destra\n2 - Canhota\n3 - Não sei\n",
            34 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            35 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            36 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            37 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            38 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            39 : "1 - Sim\n2 - Não\n3 - Não sei\n",
            40 : "1 - Sim\n2 - Não\n3 - Não sei\n"}

while len(df) > 2:
    p = random.sample(range(1,41), 40)
    for i in range(len(p)):
        perguntas = {1 : "Essa pessoa é da sala {} ?".format(dic_salas[randint(1,3)]), 
             2 : "Essa pessoa é de {} ?".format(dic_engenharias[randint(1,4)]),
             3 : "Essa pessoa torce para {} ?".format(dic_times[randint(1,6)]),
             4 : "Essa pessoa têm {} anos?".format(dic_idade[randint(1,8)]),
             5 : "Essa pessoa usa óculos ?",
             6 : "Essa pessoa nasceu na cidade de SP ?",
             7 : "Essa pessoa faz academia ?",
             8 : "Essa pessoa dirige ?",
             9 : "Qual tipo de celular que ela prefere ?",
             10 : "Essa pessoa namora ?",
             11 : "Essa pessoa já viajou para fora do Brasil ?",
             12 : "Essa pessoa têm os olhos de cor {} ?".format(dic_olhos[randint(1,3)]),
             13 : "O cabelo dessa pessoa é {} ?".format(dic_cabelo[randint(1,3)]),
             14 : "O tipo de música favorita dessa pessoa é {} ?".format(dic_musica[randint(1,10)]),
             15 : "Onde que essa pessoa gostaria de morar ?",
             16 : "Essa pessoa têm irmãos ou irmãs ?",
             17 : "Essa pessoa prefere salgado ou doce ?",
             18 : "A cor favorita dessa pessoa é {} ?".format(dic_cor[randint(1,7)]),
             19 : "Essa pessoa prefere carro ou avião ?",
             20 : "Essa pessoa prefere frio ou calor ?",
             21 : "Essa pessoa gosta de esportes ?",
             22 : "Essa pessoa foi para o Econo 2017 ?",
             23 : "Essa pessoa já trabalhou ?",
             24 : "Essa pessoa prefere chá ou café ?",
             25 : "Essa pessoa prefere filmes ou séries ?",
             26 : "Essa pessoa já viu neve ?",
             27 : "Essa pessoa têm algum animal de estimação ?",
             28 : "Essa pessoa fala bolacha ou biscoito ? ",
             29 : "Essa pessoa têm descendência {} ?".format(dic_desc[randint(1,5)]),
             30 : "Essa pessoa têm medo de aranhas ?",
             31 : "Essa pessoa gosta de videogames ?",
             32 : "Essa pessoa têm casa na praia ?",
             33 : "Essa pessoa é destra ou canhota ?",
             34 : "Essa pessoa gosta de cozinhar ?",
             35 : "Essa pessoa fala três línguas ou mais ?",
             36 : "Essa pessoa sabe surfar ?",
             37 : "Essa pessoa já acampou alguma vez ?",
             38 : "Essa pessoa têm medo de injeção ?",
             39 : "Essa pessoa já quebrou algum osso ?",
             40 : "Essa pessoa já foi picada por uma abelha ?"}
        print(perguntas[p[i]])
        x = int(input((respostas[p[i]])))
        if p[i] == 1 or p[i] == 2 or p[i] == 3 or p[i] == 12 or p[i] == 13 or p[i] == 14 or p[i] == 18 or p[i] == 29:
            if x == 1:
                df = df[(df.iloc[:, p[i]-1] == perguntas[p[i]].split()[-2])]
            if x == 2:
                df = df[(df.iloc[:, p[i]-1] != perguntas[p[i]].split()[-2])]
        if p[i] == 4:
            if x == 1:
                df = df[(df.iloc[:, p[i]-1] == int(perguntas[p[i]].split()[-2]))]
            if x == 2:
                df = df[(df.iloc[:, p[i]-1] != int(perguntas[p[i]].split()[-2]))]
        if p[i] == 5 or p[i] == 6 or p[i] == 7 or p[i] == 8 or p[i] == 10 or p[i] == 11 or p[i] == 16 or p[i] == 21 or p[i] == 22 or p[i] == 23 or p[i] == 26 or p[i] == 27 or p[i] == 29 or p[i] == 30 or p[i] == 31 or p[i] == 32 or p[i] == 34 or p[i] == 35 or p[i] == 36 or p[i] == 37 or p[i] == 38 or p[i] == 39 or p[i] == 40:
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
        if p[i] == 28:
            if x == 1:
                df = df[(df.iloc[:, p[i]-1] == "Bolacha")]
            if x == 2:
                df = df[(df.iloc[:, p[i]-1] == "Biscoito")]
        if p[i] == 33:
            if x == 1:
                df = df[(df.iloc[:, p[i]-1] == "Destra")]
            if x == 2:
                df = df[(df.iloc[:, p[i]-1] == "Canhota")]
        if len(df) == 0:
            xl = pd.ExcelFile("EP3_dados.xlsx")
            xl.sheet_names
            ['Planilha1']
            df = xl.parse()
            p = random.sample(range(1,41), 40)
            break
        if len(df) == 1:
            print("Com certeza a pessoa que você está pensando é {}!!\n".format(list(df.index)[0]))
            t = int(input("Acertei?\n1 - Sim\n2 - Não\n"))
            if t == 1:
                print("Acertei de primeira!!! Valeu pelo jogo, venha mais vezes!!")
                break
            if t == 2:
                print("Hmmm, devo ter me confundido em alguma pergunta....vamos tentar novamente")
                xl = pd.ExcelFile("EP3_dados.xlsx")
                xl.sheet_names
                ['Planilha1']
                df = xl.parse()
                p = random.sample(range(1,41), 40)
                break
        if len(df) == 2:
            w = randint(0,1)
            print("Já sei!!\nA pessoa que você está pensando deve ser {}!!\n".format(list(df.index)[w]))
            y = int(input("Estou certo?\n1 - Sim\n2 - Não\n"))
            if y == 1:
                print("Aeee, acertei mais um!! Adorei jogar com você, volte mais vezes!!\n")
                break
            if y == 2:
                print("Então com certeza a pessoa que você está pensando deve der {}!!".format(list(df.index)[w- 1]))
                z = int(input("Agora acertei, certo?\n1 - Sim\n2 - Não\n"))
                if z == 1:
                    print("Opaaa, errei uma vez mas consegui!! Obrigado por jogar, venha mais vezes!!\n")
                    break
                if z == 2:
                    print("Poxa, alguma coisa deve ter acontecido de errado, deix-me tentar novamente...\n")
                    xl = pd.ExcelFile("EP3_dados.xlsx")
                    xl.sheet_names
                    ['Planilha1']
                    df = xl.parse()
                    p = random.sample(range(1,41), 40)
                    break
        if x == 3:
            df = df
        if x == 4:
            break
    if x ==4:
        break

 
display_width = 1000
display_height = 680
 
white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
 
block_color = (53,115,255)

cor_sim = (46, 184, 46)
cor_não = (0, 107, 179)
cor_não_sei = (191, 0, 255)
cor_sair = (255, 0, 0)

cor_sim_escolha = (132, 225, 132)
cor_não_escolha = (26, 163, 255)
cor_não_sei_escolha = (210, 77, 255)
cor_sair_escolha = (255, 75, 75)
 
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Akinator')
clock = pygame.time.Clock()
 

 
 
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))
 
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
 
 
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
 
    time.sleep(2)
 
    game_loop()
    
    

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        smallText = pygame.font.Font('freesansbold.ttf',40)
        TextSurf, TextRect = text_objects(perguntas[p[i]], smallText)
        TextRect.center = ((display_width/2),(display_height/10))
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        #print(mouse)

        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, cor_sim_escolha,(150,450,100,50))
        else:
            pygame.draw.rect(gameDisplay, cor_sim,(150,450,100,50))
        if 450+100 > mouse[0] > 450 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, cor_não_escolha,(450,450,100,50))
        else:
            pygame.draw.rect(gameDisplay, cor_não,(450,450,100,50))
        if 750+100 > mouse[0] > 750 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, cor_não_sei_escolha,(750,450,100,50))
        else:
            pygame.draw.rect(gameDisplay, cor_não_sei,(750,450,100,50))
        if 450+100 > mouse[0] > 450 and 600+50 > mouse[1] >600:
            pygame.draw.rect(gameDisplay, cor_sair_escolha,(450,600,100,50))
        else:
            pygame.draw.rect(gameDisplay, cor_sair, (450,600,100,50))
            
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("Não sei", smallText)
        textRect.center = ( (750+(100/2)), (450+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("Sair", smallText)
        textRect.center = ( (450+(100/2)), (600+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        
        if p[i] == 1 or p[i] == 2 or p[i] == 3 or p[i] == 12 or p[i] == 13 or p[i] == 14 or p[i] == 18 or p[i] == 29 or p[i] == 5 or p[i] == 6 or p[i] == 7 or p[i] == 8 or p[i] == 10 or p[i] == 11 or p[i] == 16 or p[i] == 21 or p[i] == 22 or p[i] == 23 or p[i] == 26 or p[i] == 27 or p[i] == 29 or p[i] == 30 or p[i] == 31 or p[i] == 32 or p[i] == 34 or p[i] == 35 or p[i] == 36 or p[i] == 37 or p[i] == 38 or p[i] == 39 or p[i] == 40:
            smallText = pygame.font.Font("freesansbold.ttf",20)
            textSurf, textRect = text_objects("Sim", smallText)
            textRect.center = ( (150+(100/2)), (450+(50/2)) )
            gameDisplay.blit(textSurf, textRect)
            textSurf, textRect = text_objects("Não", smallText)
            textRect.center = ( (450+(100/2)), (450+(50/2)) )
            gameDisplay.blit(textSurf, textRect)
        if p[i] == 9:
            smallText = pygame.font.Font("freesansbold.ttf",20)
            textSurf, textRect = text_objects("Android", smallText)
            textRect.center = ( (150+(100/2)), (450+(50/2)) )
            gameDisplay.blit(textSurf, textRect)
            textSurf, textRect = text_objects("iPhone", smallText)
            textRect.center = ( (450+(100/2)), (450+(50/2)) )
            gameDisplay.blit(textSurf, textRect)
        if p[i] == 15:
            smallText = pygame.font.Font("freesansbold.ttf",20)
            textSurf, textRect = text_objects("Casa", smallText)
            textRect.center = ( (150+(100/2)), (450+(50/2)) )
            gameDisplay.blit(textSurf, textRect)
            textSurf, textRect = text_objects("Apartamento", smallText)
            textRect.center = ( (450+(100/2)), (450+(50/2)) )
            gameDisplay.blit(textSurf, textRect)
        if p[i] == 17:
            smallText = pygame.font.Font("freesansbold.ttf",20)
            textSurf, textRect = text_objects("Salgado", smallText)
            textRect.center = ( (150+(100/2)), (450+(50/2)) )
            gameDisplay.blit(textSurf, textRect)
            textSurf, textRect = text_objects("Doce", smallText)
            textRect.center = ( (450+(100/2)), (450+(50/2)) )
            gameDisplay.blit(textSurf, textRect)
        if p[i] == 19:
            smallText = pygame.font.Font("freesansbold.ttf",20)
            textSurf, textRect = text_objects("Carro", smallText)
            textRect.center = ( (150+(100/2)), (450+(50/2)) )
            gameDisplay.blit(textSurf, textRect)
            textSurf, textRect = text_objects("Avião", smallText)
            textRect.center = ( (450+(100/2)), (450+(50/2)) )
            gameDisplay.blit(textSurf, textRect)
        if p[i] == 20:
            smallText = pygame.font.Font("freesansbold.ttf",20)
            textSurf, textRect = text_objects("Frio", smallText)
            textRect.center = ( (150+(100/2)), (450+(50/2)) )
            gameDisplay.blit(textSurf, textRect)
            textSurf, textRect = text_objects("Calor", smallText)
            textRect.center = ( (450+(100/2)), (450+(50/2)) )
            gameDisplay.blit(textSurf, textRect)
        if p[i] == 24:
            smallText = pygame.font.Font("freesansbold.ttf",20)
            textSurf, textRect = text_objects("Chá", smallText)
            textRect.center = ( (150+(100/2)), (450+(50/2)) )
            gameDisplay.blit(textSurf, textRect)
            textSurf, textRect = text_objects("Café", smallText)
            textRect.center = ( (450+(100/2)), (450+(50/2)) )
            gameDisplay.blit(textSurf, textRect)
        if p[i] == 25:
            smallText = pygame.font.Font("freesansbold.ttf",20)
            textSurf, textRect = text_objects("Filme", smallText)
            textRect.center = ( (150+(100/2)), (450+(50/2)) )
            gameDisplay.blit(textSurf, textRect)
            textSurf, textRect = text_objects("Série", smallText)
            textRect.center = ( (450+(100/2)), (450+(50/2)) )
            gameDisplay.blit(textSurf, textRect)
        if p[i] == 28:
            smallText = pygame.font.Font("freesansbold.ttf",20)
            textSurf, textRect = text_objects("Bolacha", smallText)
            textRect.center = ( (150+(100/2)), (450+(50/2)) )
            gameDisplay.blit(textSurf, textRect)
            textSurf, textRect = text_objects("Biscoito", smallText)
            textRect.center = ( (450+(100/2)), (450+(50/2)) )
            gameDisplay.blit(textSurf, textRect)
        if p[i] == 33:
            smallText = pygame.font.Font("freesansbold.ttf",20)
            textSurf, textRect = text_objects("Destra", smallText)
            textRect.center = ( (150+(100/2)), (450+(50/2)) )
            gameDisplay.blit(textSurf, textRect)
            textSurf, textRect = text_objects("Canhota", smallText)
            textRect.center = ( (450+(100/2)), (450+(50/2)) )
            gameDisplay.blit(textSurf, textRect)
        
        
        pygame.display.update()
        clock.tick(15)
        
        
    
    

    
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
 
    x_change = 0
 
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100
 
    thingCount = 1
 
    dodged = 0
 
    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
 
        x += x_change
        gameDisplay.fill(white)
 
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
 
 
        
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
 
        if x > display_width - car_width or x < 0:
            crash()
 
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)
 
        if y < thing_starty+thing_height:
            print('y crossover')
 
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()
        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()