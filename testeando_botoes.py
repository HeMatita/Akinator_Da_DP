# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 19:31:22 2017

@author: Matheus
"""
import pygame,sys, time
from pygame.locals import *

pygame.init()






gameDisplay = pygame.display.set_mode((800,600))

clock = pygame.time.Clock()
crashed = False

while not crashed:
    def game_intro():
    
        intro = True
    
        while intro:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            gameDisplay.fill(white)
            largeText = pygame.font.Font('freesansbold.ttf',115)
            TextSurf, TextRect = text_objects("A bit Racey", largeText)
            TextRect.center = ((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf, TextRect)
    
            pygame.draw.rect(gameDisplay, green,(150,450,100,50))
            pygame.draw.rect(gameDisplay, red,(550,450,100,50))
    
    
            pygame.display.update()
            clock.tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()
    clock.tick(60)



pygame.quit()
quit()