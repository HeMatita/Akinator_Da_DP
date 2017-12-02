import pygame

screen = pygame.display.set_mode((1300, 680))
running = 1

pygame.display.set_caption('Tutorial 1')

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	screen.fill((120, 0, 85))
	pygame.draw.line(screen, (0, 0, 255), (0, 0), (1300, 680))
	pygame.draw.aaline(screen, (0, 0, 255), (1300, 0), (0, 680))
	pygame.display.flip()