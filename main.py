import pygame
from pygame.locals import *
import numpy as np 

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)

colours = {'black':(0,0,0), 'red': (255,0,0), 'blue':(0, 0, 255), 'brown':(210, 105, 30)}

ball = {'position':(100, 100), 'direction':0, 'speed':5, 'rad':5}

paddle = {'position':(200, 350), 'length':10}


pygame.display.set_caption('Drawing')

pygame.display.update()

# fpsClock.tick(FPS)
# ball = 

while True:
	# DISPLAYSURF.fill(colours['brown'])
	pygame.draw.rect(DISPLAYSURF, colours['brown'], (0, 0, 500, 400), 5)
	pygame.draw.rect(DISPLAYSURF, colours['red'], (paddle['position'][0], paddle['position'][1], 100, 10))
	pygame.draw.circle(DISPLAYSURF, colours['blue'], ball['position'], ball['rad'] , 0)
	# pygame.draw.rect(DISPLAYSURF, colours['brown'], (0, 0))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
	pygame.display.update()



