import pygame
from pygame.locals import *
import numpy as np 
import math

pygame.init()

FPS = 30
borderWidth = 5
gameStatus = False
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)

colours = {'black':(0,0,0), 'red': (255,0,0), 'blue':(0, 0, 255), 'brown':(210, 105, 30), 'green':(0, 255, 0)}

ball = {'position':{'x':200, 'y':150}, 'direction':np.random.randint(200, 340), 'speed':5, 'rad':5}

paddle = {'position':{'x':200, 'y':350}, 'length':5}

dimensions = {
			  'arena': pygame.Rect(0, 0, 500, 410), 
			  'paddle': pygame.Rect(paddle['position']['x'], paddle['position']['y'], paddle['length'], 10)
			 }

pygame.display.set_caption('Brick Breaker')

pygame.display.update()

# fpsClock.tick(FPS)
# ball = 
direction = 0

fontObj = pygame.font.Font('freesansbold.ttf', 32)


def gameOver():
	while True:
		pygame.draw.rect(DISPLAYSURF, colours['black'], dimensions['arena'])
		pygame.draw.rect(DISPLAYSURF, colours['brown'], dimensions['arena'], borderWidth)
		textSurfaceObj = fontObj.render('GAME OVER!', True, colours['red'], colours['blue'])
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center = (250, 200)
		DISPLAYSURF.blit(textSurfaceObj, textRectObj)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
                
        #gameDisplay.fill(white)
        


		pygame.display.update()
		fpsClock.tick(FPS)

def renderFunction():
	pygame.draw.rect(DISPLAYSURF, colours['black'], dimensions['arena'])
	pygame.draw.rect(DISPLAYSURF, colours['brown'], dimensions['arena'], borderWidth)
	pygame.draw.rect(DISPLAYSURF, colours['red'], dimensions['paddle'])
	pygame.draw.circle(DISPLAYSURF, colours['blue'], (ball['position']['x'], ball['position']['y']), ball['rad'] , 0)


def eventHandler():
	keys=pygame.key.get_pressed()
	if keys[K_LEFT] and not (dimensions['paddle'].left == (dimensions['arena'].left+borderWidth)):
		direction = -5
		# print('hi left')
		paddle['position']['x'] += direction
	elif keys[K_RIGHT] and not (dimensions['paddle'].right == (dimensions['arena'].right-borderWidth)):
		direction = 5
		# print('hi right')
		paddle['position']['x'] += direction
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
		# elif event.type == pygame.KEYDOWN:
		# 	if event.key == pygame.K_LEFT:
		# 		direction = -10
		# 		print('hi left')
		# 	elif event.key == pygame.K_RIGHT:
		# 		direction = 10
		# 		print('hi right')
		# 	
		# 	print(paddle['position'][0])

def ballEngine():
	if (ball['position']['x'] <= (dimensions['arena'].left+borderWidth)):
		# print('LeftSideBounce')
		ball['direction'] = 180 - ball['direction']
	elif (ball['position']['x'] >= (dimensions['arena'].right-borderWidth)):
		# print('RightSideBounce')
		ball['direction'] = 180 - ball['direction']
	elif ball['position']['y'] <= (dimensions['arena'].top+borderWidth):
		# print('TopBounce')
		ball['direction'] = 360 - ball['direction']
	elif ball['position']['y'] >= (dimensions['arena'].bottom - borderWidth):
		# print('BottomBounce')
		ball['speed'] = 0
		# gameStatus = True
		gameOver()
	# print(ball['direction'])
	ball['position']['x'] += int(ball['speed']*math.cos(ball['direction']*math.pi/180))
	ball['position']['y'] += int(ball['speed']*math.sin(ball['direction']*math.pi/180))


	if (ball['position']['y'] >= (paddle['position']['y']-ball['rad'])) and ball['position']['x'] >= dimensions['paddle'].left and ball['position']['x'] <= dimensions['paddle'].right:
		print('Paddle hit')
		ball['direction'] = 360 - ball['direction']
while True:
	# print(paddle['position'][0])
	direction = 0
	dimensions['paddle'] = pygame.Rect(paddle['position']['x'], paddle['position']['y'], 100, paddle['length'])
	# if dimensions['paddle'].left == dimensions['arena'].left:
	# 	direction = 0
	# 	print('hi left')
	# if dimensions['paddle'].right == dimensions['arena'].right:
	# 	direction = 0
	# 	print('hi right')

	# paddle['position']['x'] += direction
	eventHandler()
	ballEngine()
	renderFunction()
	pygame.display.update()
	fpsClock.tick(FPS)

