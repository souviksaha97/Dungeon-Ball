import numpy as np
import pygame
pygame.init()
from pygame.locals import *
import os

FPS = 30
borderWidth = 5

powerUp = {'isPresent':False}

boxSize = (720, 480)

isMute = False

powerUpTimer = 0

wallCreator = np.random.rand(boxSize[0], boxSize[1]) < 0.9

colours = {'black':(0, 0, 0),
		   'red': (255, 0, 0),
		   'blue':(0, 0, 255),
		   'brown':(210, 105, 30),
		   'green':(0, 255, 0),
		   'white':(255, 255, 255),
		   'gold':(255, 215, 0),
		   'silver':(192, 192, 192),
		   'grey':(128, 128, 128)}

ball = {'position':{'x':boxSize[0]/2, 'y':boxSize[1]/3}, 'direction':np.random.randint(295, 325), 'speed':7, 'rad':5}

paddle = {'position':{'x':boxSize[0]/2, 'y':boxSize[1]-50}, 'length':100, 'speed':7, 'direction':'left'}

dimensions = {
			  'arena': pygame.Rect(0, 0, boxSize[0], boxSize[1]+10), 
			  'paddle': pygame.Rect(paddle['position']['x'], paddle['position']['y'], paddle['length'], 10)
			 }

gameStatus = {'points': 0, 'level': 1, 'random': 5, 'paddleHitsPerLevel':0, 'name': 'Dungeon Ball', 'powerUp': False, 'version': 'v1.0'}


fonts = {
		 'largeFont':pygame.font.Font(os.path.join(os.getcwd(),'fonts','Ancient_Modern_Tales_Regular.ttf'), 64),
		 'midFont':pygame.font.Font(os.path.join(os.getcwd(),'fonts', 'Old_School_Adventures_Regular.ttf'), 12),
		 'tinyFont': pygame.font.Font(os.path.join(os.getcwd(),'fonts', 'Old_School_Adventures_Regular.ttf'), 8)
		}

sounds = {
			'paddleHit': pygame.mixer.Sound(os.path.join(os.getcwd(), 'audio', 'paddle_hit.wav')), 
			'wallHit': pygame.mixer.Sound(os.path.join(os.getcwd(), 'audio', 'wall_hit.wav')), 
			'gameOver':pygame.mixer.Sound(os.path.join(os.getcwd(), 'audio', 'game_over.wav')),
			'levelUp': pygame.mixer.Sound(os.path.join(os.getcwd(), 'audio', 'level_up.wav'))
		}

images = {
			'powerUp': pygame.image.load(os.path.join(os.getcwd(), 'images', 'potion.png')),
			'tiles': pygame.image.load(os.path.join(os.getcwd(), 'images', 'wall_mid.png')),
			'tileHole_1': pygame.image.load(os.path.join(os.getcwd(), 'images', 'wall_hole_1.png')),
			'tileHole_2': pygame.image.load(os.path.join(os.getcwd(), 'images', 'wall_hole_2.png')),
			'left_wall': pygame.image.load(os.path.join(os.getcwd(), 'images', 'left wall.png')),
			'right_wall': pygame.image.load(os.path.join(os.getcwd(), 'images', 'right wall.png')),
			'top_wall': pygame.image.load(os.path.join(os.getcwd(), 'images', 'top wall.png')),
			'spikes': pygame.image.load(os.path.join(os.getcwd(), 'images', 'floor_spikes.png'))
		}