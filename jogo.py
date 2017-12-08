import pygame
from pygame.locals import *
import time,sys



def principal():
    pygame.init()

    tela=pygame.display.set_mode((1200,720),0,32) #inicia a tela
    pygame.display.set_caption('Akinator da DP')
    fundo_tela=pygame.image.load('background.png')
    genio = ["genio0.png","genio1.png","genio2.png","genio3.png","genio4.png","genio5.png","genio6.png"] #sprite da arma
    
    d=0

    lampada=[0,0]
    
    while True:
	
        if (d==6):
            d=0

        tela.fill([0,0,0]) #a tela fica preta no fundo	
        tela.blit(fundo_tela, [0,0]) #a logo1 é	 posicionada nas coordenadas em 0,0
        tela.blit(pygame.image.load(genio[d]), lampada)
        
        events=pygame.event.get()
        for event in events:
            if event.type==pygame.KEYDOWN:
                if event.type==K_ESCAPE:
                    sys.exit()
                
        d=d+1
    pygame.display.update()

