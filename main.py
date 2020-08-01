import pygame
from pygame.locals import *
import numpy as np 
import math

pygame.init()

FPS = 30
borderWidth = 5
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)

colours = {'black':(0,0,0), 'red': (255,0,0), 'blue':(0, 0, 255), 'brown':(210, 105, 30), 'green':(0, 255, 0), 'white':(255, 255, 255)}

ball = {'position':{'x':200, 'y':150}, 'direction':np.random.randint(295, 325), 'speed':5, 'rad':5}

paddle = {'position':{'x':200, 'y':350}, 'length':5, 'speed':5}

dimensions = {
			  'arena': pygame.Rect(0, 0, 500, 410), 
			  'paddle': pygame.Rect(paddle['position']['x'], paddle['position']['y'], paddle['length'], 10)
			 }

gameStatus = {'points':0, 'level':1, 'random': 1, 'name': 'Dungeon Ball', 'version': 'v1.0'}

pygame.display.set_caption(gameStatus['name'])

fonts = {'largeFont':pygame.font.Font(pygame.font.match_font('oldschooladventures'), 32),
		 'midFont':pygame.font.Font(pygame.font.match_font('oldschooladventures'), 12),
		'tinyFont': pygame.font.Font(pygame.font.match_font('oldschooladventures'), 8)}

sounds = {'paddleHit': pygame.mixer.Sound('paddle_hit.wav'), 
'wallHit': pygame.mixer.Sound('wall_hit.wav'), 
'gameOver':pygame.mixer.Sound('game_over.wav'),
'levelUp': pygame.mixer.Sound('level_up.wav')}

def gameOver():
	pygame.mixer.music.stop()
	sounds['gameOver'].play()
	keyStatus = True
	while keyStatus:
		pygame.draw.rect(DISPLAYSURF, colours['black'], dimensions['arena'])
		pygame.draw.rect(DISPLAYSURF, colours['brown'], dimensions['arena'], borderWidth)
		textSurfaceObj = fonts['largeFont'].render('GAME OVER!', True, colours['red'], colours['blue'])
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center = (250, 200)
		DISPLAYSURF.blit(textSurfaceObj, textRectObj)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					sounds['gameOver'].stop()
					keyStatus = False
				elif event.key == pygame.K_ESCAPE:
					pygame.quit()
					quit()

		pygame.display.update()
		fpsClock.tick(FPS)

		if keyStatus == False:
			break

	main()

def renderFunction():
	global gameStatus
	pygame.draw.rect(DISPLAYSURF, colours['black'], dimensions['arena'])
	pygame.draw.rect(DISPLAYSURF, colours['brown'], dimensions['arena'], borderWidth)
	pygame.draw.rect(DISPLAYSURF, colours['red'], dimensions['paddle'])
	pygame.draw.circle(DISPLAYSURF, colours['blue'], (ball['position']['x'], ball['position']['y']), ball['rad'] , 0)
	pointSurface = fonts['tinyFont'].render('Points : ' + str(gameStatus['points']), True, colours['white'])
	pointSurfaceRect = pointSurface.get_rect()
	pointSurfaceRect.center = (40, 390)
	DISPLAYSURF.blit(pointSurface, pointSurfaceRect)

	levelSurface = fonts['tinyFont'].render('Level : ' + str(gameStatus['level']), True, colours['white'])
	levelSurfaceRect = levelSurface.get_rect()
	levelSurfaceRect.center = (460, 390)
	DISPLAYSURF.blit(levelSurface, levelSurfaceRect)

def introScreen():
	keyStatus = True
	blinkerCount = 0
	blinkerState = True
	blinkTime = 15
	pygame.mixer.music.load('startScreenMusic.wav')
	pygame.mixer.music.play(-1, 0.0)
	while keyStatus:
		pygame.draw.rect(DISPLAYSURF, colours['black'], dimensions['arena'])
		# pygame.draw.rect(DISPLAYSURF, colours['brown'], dimensions['arena'], borderWidth)
		textSurfaceObj = fonts['largeFont'].render(gameStatus['name'], True, colours['red'], colours['blue'])
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center = (250, 200)
		DISPLAYSURF.blit(textSurfaceObj, textRectObj)

		if blinkerState:
			spaceSurfaceObj = fonts['midFont'].render('Press Enter to Continue', True, colours['white'])
			spaceRectObj = spaceSurfaceObj.get_rect()
			spaceRectObj.center = (250, 250)
			DISPLAYSURF.blit(spaceSurfaceObj, spaceRectObj)

		versionSurface = fonts['tinyFont'].render(gameStatus['version'], True, colours['white'])
		versionSurfaceRect = versionSurface.get_rect()
		versionSurfaceRect.center = (480, 390)
		DISPLAYSURF.blit(versionSurface, versionSurfaceRect)
		blinkerCount += 1

		if blinkerCount % blinkTime == 0:
			blinkerCount = 0
			blinkerState = not blinkerState

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					keyStatus = False
		pygame.display.update()
		fpsClock.tick(FPS)

	keyStatus=True
	pygame.mixer.music.stop()		

def eventHandler():
	global dimensions
	keys=pygame.key.get_pressed()
	if keys[K_LEFT] and not (dimensions['paddle'].left <= (dimensions['arena'].left+borderWidth)):
		direction = -1*paddle['speed']
		# print('hi left')
		paddle['position']['x'] += direction
	elif keys[K_RIGHT] and not (dimensions['paddle'].right >= (dimensions['arena'].right-borderWidth)):
		direction = paddle['speed']
		# print('hi right')
		paddle['position']['x'] += direction
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()

	dimensions['paddle'] = pygame.Rect(paddle['position']['x'], paddle['position']['y'], 100, paddle['length'])


def ballEngine():
	global gameStatus
	if (ball['position']['x'] <= (dimensions['arena'].left+borderWidth+ball['rad'])):
		# print('LeftSideBounce')
		ball['direction'] = 180 - ball['direction'] + pow(-1, np.random.randint(2))*np.random.randint(gameStatus['random'])
		sounds['wallHit'].play()
	elif (ball['position']['x'] >= (dimensions['arena'].right-borderWidth-ball['rad'])):
		# print('RightSideBounce')
		ball['direction'] = 180 - ball['direction'] + pow(-1, np.random.randint(2))*np.random.randint(gameStatus['random'])
		sounds['wallHit'].play()
	elif ball['position']['y'] <= (dimensions['arena'].top+borderWidth+ball['rad']):
		# print('TopBounce')
		ball['direction'] = 360 - ball['direction'] + pow(-1, np.random.randint(2))*np.random.randint(gameStatus['random'])
		sounds['wallHit'].play()
	elif ball['position']['y'] >= (dimensions['arena'].bottom - borderWidth - ball['rad']):
		# print('BottomBounce')
		# ball['speed'] = 0
		# gameStatus = True
		gameOver()
	# print(ball['direction'])
	ball['position']['x'] += int(ball['speed']*math.cos(ball['direction']*math.pi/180))
	ball['position']['y'] += int(ball['speed']*math.sin(ball['direction']*math.pi/180))


	if (ball['position']['y'] >= (paddle['position']['y']-ball['rad']) and ball['position']['y'] <= paddle['position']['y']+5-ball['rad']) and ball['position']['x'] >= dimensions['paddle'].left and ball['position']['x'] <= dimensions['paddle'].right:
		# print('Paddle hit')
		ball['direction'] = 360 - ball['direction'] + pow(-1, np.random.randint(2))*np.random.randint(gameStatus['random'])
		gameStatus['points'] = gameStatus['points'] + 1

		sounds['paddleHit'].play()

		if gameStatus['points'] % 5 == 0 and not gameStatus['points']  == 0:
			ball['speed'] += 2
			gameStatus['level'] += 1
			gameStatus['random'] += 1
			sounds['levelUp'].play()

		if gameStatus['points'] % 10 == 0 and not gameStatus['points']  == 0:
			paddle['speed'] += 1

def init():
	global ball, paddle, gameStatus
	ball['position']['x']=200
	ball['position']['y']=150
	ball['direction']=np.random.randint(295, 325)
	ball['speed']=5
	ball['rad']=5

	paddle['position']['x']=200
	paddle['position']['y']=350
	paddle['length']=5
	paddle['speed']=5

	gameStatus['points']=0
	gameStatus['level']=1
	gameStatus['random']=1


def main():
	introScreen()
	init()
	pygame.mixer.music.load('gamePlayMusic.wav')
	pygame.mixer.music.play(-1, 0.0)
	while True:
		# print(paddle['position'][0])
		eventHandler()
		ballEngine()
		renderFunction()
		pygame.display.update()
		fpsClock.tick(FPS)

if __name__ == '__main__':
	main()
