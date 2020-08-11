import pygame
from pygame.locals import *
import numpy as np 
import math
from sys import exit
pygame.init()

from variables import *

def gameOver():
	global isMute, wallCreator
	pygame.mixer.music.stop()
	if not isMute:
		sounds['gameOver'].play()
	keyStatus = True
	blinkerCount = 0
	blinkerState = True
	blinkTime = 15
	
	while keyStatus:
		renderWall(wallCreator)
		# pygame.draw.rect(DISPLAYSURF, colours['grey'], dimensions['arena'])
		# pygame.draw.rect(DISPLAYSURF, colours['brown'], dimensions['arena'], borderWidth)
		if blinkerState:
			textSurfaceObj = fonts['largeFont'].render('GAME OVER!', True, colours['red'])
			textRectObj = textSurfaceObj.get_rect()
			textRectObj.center = (boxSize[0]/2, boxSize[1]/2)
			DISPLAYSURF.blit(textSurfaceObj, textRectObj)

		scoreSurface = fonts['midFont'].render('Score : {}'.format(gameStatus['points']), True, colours['white'])
		scoreSurfaceRect = scoreSurface.get_rect()
		scoreSurfaceRect.center = (boxSize[0]/2, boxSize[1]/2 + 50)
		DISPLAYSURF.blit(scoreSurface, scoreSurfaceRect)

		blinkerCount += 1

		if blinkerCount % blinkTime == 0:
			blinkerCount = 0
			blinkerState = not blinkerState

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					sounds['gameOver'].stop()
					keyStatus = False
				elif event.key == pygame.K_ESCAPE:
					pygame.quit()
					exit()
				elif event.key == pygame.K_m:
					isMute = not isMute

		pygame.display.update()
		fpsClock.tick(FPS)

		if keyStatus == False:
			break

	main()

def renderWall(wall):
	for i in np.arange(0, boxSize[0], 16):
		for j in np.arange(0, boxSize[1], 16):
			if wall[i][j] == True:
				DISPLAYSURF.blit(images['tiles'], (i, j))
			else:
				DISPLAYSURF.blit(images['tileHole_1'], (i, j))

			if i == 0:
				DISPLAYSURF.blit(images['left_wall'], (i, j))

			if i == boxSize[0]-16:
				DISPLAYSURF.blit(images['right_wall'], (i, j))

			if j == 0:
				DISPLAYSURF.blit(images['top_wall'], (i, j))

			if j == boxSize[1] - 16 and i > 80 and i < boxSize[0]-80:
				DISPLAYSURF.blit(images['spikes'], (i, j))


def renderFunction(wall):
	global gameStatus

	renderWall(wall)
	# pygame.draw.rect(DISPLAYSURF, colours['brown'], dimensions['arena'], borderWidth)
	pygame.draw.rect(DISPLAYSURF, colours['red'], dimensions['paddle'])
	pygame.draw.circle(DISPLAYSURF, colours['blue'], (ball['position']['x'], ball['position']['y']), ball['rad'] , 0)
	pointSurface = fonts['tinyFont'].render('Points : ' + str(gameStatus['points']), True, colours['white'])
	pointSurfaceRect = pointSurface.get_rect()
	pointSurfaceRect.center = (40, boxSize[1]-10)
	DISPLAYSURF.blit(pointSurface, pointSurfaceRect)

	levelSurface = fonts['tinyFont'].render('Level : ' + str(gameStatus['level']), True, colours['white'])
	levelSurfaceRect = levelSurface.get_rect()
	levelSurfaceRect.center = (boxSize[0]-40, boxSize[1]-10)
	DISPLAYSURF.blit(levelSurface, levelSurfaceRect)

	if powerUp['isPresent']:
		DISPLAYSURF.blit(images['powerUp'], powerUp['location'])

def introScreen():
	global isMute, wallCreator
	keyStatus = True
	blinkerCount = 0
	blinkerState = True
	blinkTime = 15
	if not isMute:
		pygame.mixer.music.load(os.path.join(os.getcwd(), 'audio', 'startScreenMusic.wav'))
		pygame.mixer.music.play(-1, 0.0)

	while keyStatus:
		renderWall(wallCreator)
		# pygame.draw.rect(DISPLAYSURF, colours['grey'], dimensions['arena'])
		# pygame.draw.rect(DISPLAYSURF, colours['brown'], dimensions['arena'], borderWidth)
		textSurfaceObj = fonts['largeFont'].render(gameStatus['name'], True, colours['gold'])
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center = (boxSize[0]/2, boxSize[1]/2)
		DISPLAYSURF.blit(textSurfaceObj, textRectObj)

		if blinkerState:
			spaceSurfaceObj = fonts['midFont'].render('Press Enter to Continue', True, colours['white'])
			spaceRectObj = spaceSurfaceObj.get_rect()
			spaceRectObj.center = (boxSize[0]/2, boxSize[1]/2+50)
			DISPLAYSURF.blit(spaceSurfaceObj, spaceRectObj)

		versionSurface = fonts['tinyFont'].render(gameStatus['version'], True, colours['white'])
		versionSurfaceRect = versionSurface.get_rect()
		versionSurfaceRect.center = (boxSize[0]-20, boxSize[1]-10)
		DISPLAYSURF.blit(versionSurface, versionSurfaceRect)
		blinkerCount += 1

		if blinkerCount % blinkTime == 0:
			blinkerCount = 0
			blinkerState = not blinkerState

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					keyStatus = False
				elif event.key == pygame.K_ESCAPE:
					pygame.quit()
					exit()
				elif event.key == pygame.K_m:
					isMute = not isMute
					if isMute:
						pygame.mixer.music.stop()
					else:
						pygame.mixer.music.load(os.path.join(os.getcwd(), 'audio', 'startScreenMusic.wav'))
						pygame.mixer.music.play(-1, 0.0)

		pygame.display.update()
		fpsClock.tick(FPS)

	keyStatus=True
	pygame.mixer.music.stop()		

def eventHandler():
	global dimensions, isMute
	keys=pygame.key.get_pressed()

	if keys[K_LEFT] and not (dimensions['paddle'].left <= (dimensions['arena'].left+borderWidth)):
		direction = -1*paddle['speed']
		paddle['direction'] = 'left'
		paddle['position']['x'] += direction
		# print('hi left')
	elif keys[K_RIGHT] and not (dimensions['paddle'].right >= (dimensions['arena'].right-borderWidth)):
		direction = paddle['speed']
		paddle['direction'] = 'right'
		paddle['position']['x'] += direction
	else:
		paddle['direction'] = 'none'
		# print('hi right')
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_m:
				isMute = not isMute
				if isMute:
						pygame.mixer.music.stop()
				else:
					pygame.mixer.music.load(os.path.join(os.getcwd(), 'audio', 'gamePlayMusic.wav'))
					pygame.mixer.music.play(-1, 0.0)
				

	dimensions['paddle'] = pygame.Rect(paddle['position']['x'], paddle['position']['y'], paddle['length'], 10)

def createPowerup():
	return np.random.randint(1, 100) % 17 == 0

def ballEngine():
	global gameStatus, powerUp, powerUpTimer
	if (ball['position']['x'] <= (dimensions['arena'].left+borderWidth+ball['rad'])):
		# print('LeftSideBounce')
		ball['direction'] = 180 - ball['direction'] + np.random.randint(-1*gameStatus['random'],gameStatus['random'])
		sounds['wallHit'].play()

	elif (ball['position']['x'] >= (dimensions['arena'].right-borderWidth-ball['rad'])):
		# print('RightSideBounce')
		ball['direction'] = 180 - ball['direction'] + np.random.randint(-1*gameStatus['random'],gameStatus['random'])
		sounds['wallHit'].play()

	elif ball['position']['y'] <= (dimensions['arena'].top+borderWidth+ball['rad']):
		# print('TopBounce')
		ball['direction'] = 360 - ball['direction'] + np.random.randint(-1*gameStatus['random'],gameStatus['random'])

		if ball['direction'] >= 250 and ball['direction'] <= 290:
			ball['direction'] += np.random.randint(-2*gameStatus['random'],2*gameStatus['random'])

		sounds['wallHit'].play()
	elif ball['position']['y'] >= (dimensions['arena'].bottom - borderWidth - ball['rad']):
		# print('BottomBounce')
		# ball['speed'] = 0
		# gameStatus = True
		gameOver()
	# print(ball['direction'])
	if (ball['position']['y'] >= (paddle['position']['y']-ball['rad']) and ball['position']['y'] <= paddle['position']['y']+dimensions['paddle'].height+ball['rad']) and ball['position']['x'] >= dimensions['paddle'].left and ball['position']['x'] <= dimensions['paddle'].right:
		# print('Paddle hit')
		ball['direction'] = 360 - ball['direction'] #+ np.random.randint(-1*gameStatus['random'],gameStatus['random'])

		if paddle['direction'] == 'left':
			ball['direction'] += np.random.randint(-2*gameStatus['random'], 0)
		elif paddle['direction'] == 'right':
			ball['direction'] += np.random.randint(0, 2*gameStatus['random'])

		gameStatus['points'] = gameStatus['points'] + 1

		if not powerUp['isPresent'] and gameStatus['level'] > 2:
			powerUp['isPresent'] = createPowerup()
			if powerUp['isPresent']:
				powerUp['location'] = (np.random.randint(borderWidth*10, boxSize[0]-borderWidth*10), 
										np.random.randint(borderWidth*10, boxSize[1]-borderWidth*10))

		sounds['paddleHit'].play()
		# print(ball['position'], paddle['position'], ball['direction'])
		# print(gameStatus)

		gameStatus['paddleHitsPerLevel'] += 1

		if ball['position']['y'] >= dimensions['paddle'].top and ball['position']['y'] <= dimensions['paddle'].bottom:
			ball['position']['y'] = dimensions['paddle'].top - ball['rad']

		if gameStatus['paddleHitsPerLevel'] == (gameStatus['level']*5) and not gameStatus['points']  == 0:
			ball['speed'] += 2
			gameStatus['level'] += 1
			gameStatus['random'] += 2
			gameStatus['paddleHitsPerLevel'] = 0
			sounds['levelUp'].play()

		if gameStatus['points'] % 10 == 0 and not gameStatus['points']  == 0:
			paddle['speed'] += 1

	if (ball['direction']>360 or ball['direction'] < 0):
		ball['direction'] %= 360

	if ball['direction'] % 90 >= 80 and ball['direction'] % 90 <=89 or ball['direction'] % 90 >= 0 and ball['direction'] % 90 <= 10:
		ball['direction'] += np.random.randint(-5*gameStatus['random'],5*gameStatus['random'])


	if ball['position']['y'] < borderWidth+ball['rad']:
		ball['position']['y'] = borderWidth+ball['rad']
	elif ball['position']['x'] < borderWidth+ball['rad']:
		ball['position']['x'] = borderWidth+ball['rad']
	elif ball['position']['x'] > dimensions['arena'].right-borderWidth-ball['rad']:
		ball['position']['x'] = dimensions['arena'].right-borderWidth-ball['rad']


	if powerUp['isPresent']:
		if abs(ball['position']['x']-powerUp['location'][0]) < 10 and abs(ball['position']['y']-powerUp['location'][1]) < 10:
			paddle['length'] += 50
			powerUp['isPresent'] = False
			powerUp.pop('location')
			powerUpTimer = 0
			gameStatus['powerUp'] = True

		powerUpTimer += 1

		if powerUpTimer/FPS == 10:
			powerUp['isPresent'] = False
			powerUp.pop('location')
			powerUpTimer = 0

	if gameStatus['powerUp']:
		powerUpTimer += 1
		if powerUpTimer/FPS == 15:
			gameStatus['powerUp'] = False
			paddle['length'] -= 50
			powerUpTimer = 0


	ball['position']['x'] += int(ball['speed']*math.cos(ball['direction']*math.pi/180))
	ball['position']['y'] += int(ball['speed']*math.sin(ball['direction']*math.pi/180))

def init():
	global ball, paddle, gameStatus, powerUpisPresent
	ball['position']['x']=boxSize[0]/2
	ball['position']['y']=int(boxSize[1]/3)
	ball['direction']=np.random.randint(225, 315)
	ball['speed']=7
	ball['rad']=5

	paddle['position']['x']=boxSize[0]/2
	paddle['position']['y']=boxSize[1]-50
	paddle['length']=100
	paddle['speed']=7

	gameStatus['points']=0
	gameStatus['level']=1
	gameStatus['random']=5
	gameStatus['powerUp']=False

	powerUp = {'isPresent':False}

def main():
	global wallCreator
	introScreen()
	init()
	pygame.mixer.music.load(os.path.join(os.getcwd(),'audio', 'gamePlayMusic.wav'))
	if not isMute:
		pygame.mixer.music.play(-1, 0.0)


	while True:
		eventHandler()
		ballEngine()
		renderFunction(wallCreator)
		pygame.display.update()
		fpsClock.tick(FPS)

if __name__ == '__main__':
	fpsClock = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode(boxSize, 0, 32)
	pygame.display.set_caption(gameStatus['name'])
	main()
