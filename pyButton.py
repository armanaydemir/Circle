#!/usr/bin/env python2.7
# pyButton.py
# makes the buttons of py
# Arman Aydemir
# March, 30 2014


import pygame
from pygame import *

#color constants
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

#class for constructing buttons
class PyButton:
	color = None
	shape = None
	screen = None
	
	#initializes variables
	def __init__(self, color, shape):
		pygame.init()
		self.color = color
		self.shape = shape
		self.screen = pygame.display.set_mode((800, 800), 0, 0)
	
	def contains_click(self, point):
		return self.shape.collidepoint(point)
		
		
	