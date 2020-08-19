import numpy as np
import pygame
pygame.init()
from pygame.locals import *
import os

FPS = 30
borderWidth = 5

powerUp = {'isPresent':False}

# boxSize = (720, 480)

width = 720
height = 480

isMute = False

powerUpTimer = 0

LEFT_ANGLE = 225
RIGHT_ANGLE = 315

wallCreator = np.random.rand(width, height) < 0.9

colours = {'black':(0, 0, 0),
		   'red': (255, 0, 0),
		   'blue':(0, 0, 255),
		   'brown':(210, 105, 30),
		   'green':(0, 255, 0),
		   'white':(255, 255, 255),
		   'gold':(255, 215, 0),
		   'silver':(192, 192, 192),
		   'grey':(128, 128, 128)}

ball = {'position':{'x':width/2, 'y':height/3}, 'direction':np.random.randint(LEFT_ANGLE, RIGHT_ANGLE), 'speed':7, 'radius':5}

paddle = {'position':{'x':width/2, 'y':height-50}, 'length':100, 'speed':7, 'direction':'left'}

dimensions = {
			  'arena': pygame.Rect(0, 0, width, height+10), 
			  'paddle': pygame.Rect(paddle['position']['x'], paddle['position']['y'], paddle['length'], 10)
			 }

gameStatus = {'points': 0, 'level': 1, 'random': 5, 'paddleHitsPerLevel':0, 'name': 'Dungeon Ball', 'powerUp': False, 'version': 'v1.0'}


def get_sound(filename):
    return pygame.mixer.Sound(os.path.join(os.getcwd(), 'audio', filename))

def get_font(filename, fontSize):
	return pygame.font.Font(os.path.join(os.getcwd(),'fonts',filename), fontSize)

def get_image(filename):
	return pygame.image.load(os.path.join(os.getcwd(), 'images', filename))


fonts = {
		 'largeFont': get_font('Ancient_Modern_Tales_Regular.ttf', 64),
		 'midFont': get_font('Old_School_Adventures_Regular.ttf', 16),
		 'tinyFont': get_font('Old_School_Adventures_Regular.ttf', 10)
		}

sounds = {
			'paddleHit': get_sound('paddle_hit.wav'), 
			'wallHit': get_sound('wall_hit.wav'), 
			'gameOver': get_sound('game_over.wav'),
			'levelUp': get_sound('level_up.wav'),
			'powerUp': get_sound('power_up.wav'),
			'powerDown': get_sound('power_down.wav'),
			'explosion': get_sound('explosion.wav')
		}

images = {
			'powerUp': get_image('potion.png'),
			'tiles': get_image('wall_mid.png'),
			'tileHole_1': get_image('wall_hole_1.png'),
			'tileHole_2': get_image('wall_hole_2.png'),
			'left_wall': get_image('left wall.png'),
			'right_wall': get_image('right wall.png'),
			'top_wall': get_image('top wall.png'),
			'spikes': get_image('floor_spikes.png')
		}