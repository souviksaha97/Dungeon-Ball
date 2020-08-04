import numpy as np
import pygame
pygame.init()
from pygame.locals import *
import os

FPS = 30
borderWidth = 5

boxSize = (700, 400)

colours = {'black':(0, 0, 0),
		   'red': (255, 0, 0),
		   'blue':(0, 0, 255),
		   'brown':(210, 105, 30),
		   'green':(0, 255, 0),
		   'white':(255, 255, 255),
		   'gold':(255, 215, 0),
		   'silver':(192, 192, 192),
		   'grey':(128, 128, 128)}

ball = {'position':{'x':boxSize[0]/2, 'y':boxSize[1]/3}, 'direction':np.random.randint(295, 325), 'speed':5, 'rad':5}

paddle = {'position':{'x':boxSize[0]/2, 'y':boxSize[1]-50}, 'length':100, 'speed':5}

dimensions = {
			  'arena': pygame.Rect(0, 0, boxSize[0], boxSize[1]+10), 
			  'paddle': pygame.Rect(paddle['position']['x'], paddle['position']['y'], paddle['length'], 10)
			 }

gameStatus = {'points': 0, 'level': 1, 'random': 5, 'paddleHitsPerLevel':0, 'name': 'Dungeon Ball', 'version': 'v1.0'}


fonts = {
		 'largeFont':pygame.font.Font(os.getcwd()+'\\fonts\\Ancient_Modern_Tales_Regular.ttf', 64),
		 'midFont':pygame.font.Font(os.getcwd()+'\\fonts\\Old_School_Adventures_Regular.ttf', 12),
		 'tinyFont': pygame.font.Font(os.getcwd()+'\\fonts\\Old_School_Adventures_Regular.ttf', 8)
		}

sounds = {'paddleHit': pygame.mixer.Sound(os.getcwd()+'\\audio\\paddle_hit.wav'), 
'wallHit': pygame.mixer.Sound(os.getcwd()+'\\audio\\wall_hit.wav'), 
'gameOver':pygame.mixer.Sound(os.getcwd()+'\\audio\\game_over.wav'),
'levelUp': pygame.mixer.Sound(os.getcwd()+'\\audio\\level_up.wav')}