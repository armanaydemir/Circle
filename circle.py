#!/usr/bin/env python2.7
# circle.py is a data representation of a circle
# Arman Aydemir
# April 28th, 2014

import random
import math
import time

NORTH = 1
SOUTH = 2
EAST = 3
WEST = 4

class Circle:
	center = None
	radius = 0
	color = None
	speed = None
	
	def __init__(self, cen, rad, col, spd):
		self.center = cen
		self.radius = rad
		self.color = col
		self.speed = spd
		
	def move_ip(self):
		self.center = (self.center[0] + self.speed[0], self.center[1] + self.speed[1])
		
	def bounce(self, width, height):
		# check all four dimensions using if
		# WEST -- left wall
		if self.center[0]-self.radius < 1:
			self.center = ((self.radius+1), self.center[1])
			self.change_direction(WEST)
		# EAST -- right wall
		if self.center[0]+self.radius > width-1:
			self.center = (width-(1+self.radius), self.center[1])
			self.change_direction(EAST)
		# NORTH -- top wall
		if self.center[1]-self.radius < 1:
			self.center = (self.center[0], (self.radius+1))
			self.change_direction(NORTH)
		# South -- bottom wall
		if self.center[1]+self.radius > height-1:
			self.center = (self.center[0], height-(1+self.radius))
			self.change_direction(SOUTH)
	
	def change_direction(self, dir):
		if dir == EAST or dir == WEST:
			self.speed = (self.speed[0]*-1, self.speed[1])
		elif dir == NORTH or dir == SOUTH:
			self.speed = (self.speed[0], self.speed[1]*-1)
			
	def contains_point(self, p):
		return math.sqrt(((p[1]-self.center[1])**2) + ((p[0]-self.center[0])**2)) < self.radius
		
	def disappear(self):
		R = self.color[0]
		B = self.color[1]
		G = self.color[2]
		if R > 2:
			R -= 2
		if G > 2:
			G -= 2
		if B > 2:
			B -= 2
		self.color = (R, G, B)
		#extract color values R, G, B
		#subtract a factor from each value* - use if statements
		#color = (R, G, B) --> supplying new values
	
	def isInvisible(self):
		return color[0]<5 and color[1]<5 and color[2]<5
		
	def colliding(self, p):
		return math.sqrt(((p.center[1]-self.center[1])**2) + ((p.center[0]-self.center[0])**2)) < p.radius + self.radius
		
	#def collided(self):
		#self.speed = (self.speed[0]*-1, self.speed[1]*-1)