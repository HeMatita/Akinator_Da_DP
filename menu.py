# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 16:32:34 2017

@author: mathe
"""
#Imports
import pygame,sys, time
from pygame.locals import *

#Função que chama o menu
def menu():
	pygame.init()
	pygame.mixer.init()
	tela=pygame.display.set_mode((1200,720),0,32)
	pygame.display.set_caption('Akinator da DP')
    
    #Fundo do programa
	fundo=pygame.image.load('background.png')
    
	fonte=pygame.font.Font("anirb.ttf", 40)
    
    #Opções
	iniciar=fonte.render("Iniciar",1,(205,25,205)) #texto 1
	lista=fonte.render("Lista de Pessoas",1,(205,25,205))
	quitar=fonte.render("Sair",1,(205,25,205))
    
	iniciar_NEW=fonte.render("Iniciar",1,(64,77,205))
	lista_NEW=fonte.render("Lista de Pessoas",1,(64,77,205))
	quitar_NEW=fonte.render("Sair",1,(64,77,205))
    
	
	xp=iniciar_NEW
	yp=lista
	zp=quitar
    
    #Música do programa
	soundtrack_1="tema.mp3"
	pygame.mixer.music.load(soundtrack_1) #Música
	pygame.mixer.music.play(-1)
    
	egito=[350,305]
	d=0
	while True:
    	
		if (d==6):
				d=0
    
				tela.fill([0,0,0]) #a tela fica preta no fundo
    
				tela.blit(fundo, [0,0]) #a logo1 é	 posicionada nas coordenadas em 0,0
				tela.blit(xp, [420,300])
				tela.blit(yp, [410,400])
				tela.blit(zp, [410,500])
				
				
				events=pygame.event.get();
				for event in events:
					if event.type==pygame.KEYDOWN:
						if event.key==K_ESCAPE:
							pygame.mixer.music.fadeout(2)
							sys.exit()
						elif xp==iniciar_NEW and event.key==K_DOWN:
							xp=iniciar
							yp=lista_NEW
							zp=quitar
							markerp=2
						
						elif xp==iniciar_NEW and event.key==K_UP:
							xp=inciar
							yp=lista
							zp=quitar_NEW
							markerp=3
					
						elif yp==lista_NEW and event.key==K_DOWN:
							xp=iniciar
							yp=lista
							zp=quitar_NEW
							markerp=3
					
						elif yp==lista_NEW and event.key==K_UP:
							xp=iniciar_NEW
							yp=lista
							zp=quitar
							markerp=1
				
						elif zp==quitar_NEW and event.key==K_DOWN:
							xp=iniciar_NEW
							yp=lista
							zp=quitar
							markerp=1
					
						elif zp==quitar_NEW and event.key==K_UP:
							xp=iniciar
							yp=lista_NEW
							zp=quitar
							markerp=2
					
						#elif markerp==1 and event.key==pygame.K_RETURN:
						#	historinha.HISTORIONA()
						#elif markerp==2 and event.key==pygame.K_RETURN:
						#	opt.opcoes()
						elif markerp==3 and event.key==pygame.K_RETURN:
							pygame.mixer.music.fadeout(2)
							sys.exit()
                            
                            
		d=d+1
		pygame.display.update()
            
menu()
