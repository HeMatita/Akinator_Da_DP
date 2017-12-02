import pygame
pygame.init()

(width, height) = (800, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
while True:
	pass


pygame.display.set_caption('Tutorial 1')

background_colour = (255,255,255)
screen.fill(background_colour)

background_colour = (255,255,255)
(width, height) = (300, 200)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
 
pygame.display.flip()
 
running = True
while running:
	pygame.event.get()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

