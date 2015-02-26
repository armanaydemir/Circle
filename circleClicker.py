#!/usr/bin/env python2.7
# file that main game is played off of
# Arman Aydemir
# April 28, 2014
#http://stackoverflow.com/questions/3964681/find-all-files-in-directory-with-extension-txt-with-python
#http://stackoverflow.com/questions/180606/how-do-i-convert-a-list-of-ascii-values-to-a-string-in-python

#Constants
#==================
beta = []
for i in range(97,124):
	beta.append(i)
for i in range(65,92):
	beta.append(i)
import pygame
import sys
import circle
import random
from pygame import *
from circle import Circle
from scorer import Scorer
from pyButton import PyButton
from scoreManager import ScoreManager
app = ScoreManager('scores.txt')
import time
WIDTH = 800
HEIGHT = 800
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.update()
circles = []
###### circle factory here #######
ranPos = (0,0)
ranRadius = 0
ranR = 0
ranG = 0
ranB = 0
ranSpd = (0,0)
blocks = []

#adds circle to screen
#====================
def addition():
	ranPos = (random.randrange(100, WIDTH-100), random.randrange(100, HEIGHT-100))
	ranRadius = random.randrange(50,101)
	ranR = random.randrange(0,256)
	ranG = random.randrange(0,256)
	ranB = random.randrange(0,256)
	ranSpd = (random.randrange(-4, 5), random.randrange(-4, 5))
	circles.append(Circle(ranPos, ranRadius, (ranR,ranG,ranB), ranSpd))
	
#initiates the two point circle system
#======================
def cut(p,t):
	ranR = random.randrange(0,256)
	ranG = random.randrange(0,256)
	ranB = random.randrange(0,256)
	ranSpd = ((p[0]-t[0])/-10, (p[1]-t[1])/-10)
	hst = Circle(p, 10, (ranR,ranG,ranB), ranSpd)
	circles.append(hst)
	return hst	
	
#gives player menu options
#==============
def menu():
	
	#updates high scores
	app.rewrite()
	
	blocks = []
	screen.fill((0,0,0))
	blocks.append(PyButton((255,255,255), Rect(200,160,400,160)))
	blocks.append(PyButton((0,150,255), Rect(200,480,400,160)))
	for btn in blocks:
		pygame.draw.rect(btn.screen, btn.color, btn.shape)
	screen.blit(pygame.font.Font(None, 80).render('Play',1,(0,0,0)), (350, 220))
	screen.blit(pygame.font.Font(None, 80).render('High Scores',1,(255,255,255)), (252, 540))
	pygame.display.flip()
	free = False
	contin = False
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				#updates high scores
				app.rewrite()
				
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONDOWN:
				if blocks[0].contains_click(pygame.mouse.get_pos()):
					free = True
					break
				elif blocks[1].contains_click(pygame.mouse.get_pos()):
					contin = True
					break
		if free or contin:
			break
	if free:
		namer()
	elif contin:
		high()

#displays the high scores
#====================	
def high():
	blocks = []
	wait = True
	while wait:
		for event in pygame.event.get():
			if event.type == QUIT:
				#updates high scores
				app.rewrite()
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONDOWN:
				if blocks[0].contains_click(pygame.mouse.get_pos()):
					wait = False
					break
		screen.fill((0,0,0))
		blocks.append(PyButton((255,255,255), Rect(200,100,400,50)))
		for btn in blocks:
			pygame.draw.rect(btn.screen, btn.color, btn.shape)
		t = 0
		for i in app.printList():
			screen.blit(pygame.font.Font(None, 80).render(str(i.name) + ' ' + str(i.score),1,(255,255,255)), (155, 220+100*t))
			t += 1
		screen.blit(pygame.font.Font(None, 80).render('Main Menu',1,(0,0,0)), (250, 100))
		pygame.display.flip()
	menu()

#lets player put in their name
#========================		
def namer():
	nwait = True 
	L = []
	upper = False
	while nwait:
		screen.fill((0,0,0))
		screen.blit(pygame.font.Font(None, 80).render('Name:',1,(255,255,255)), (100, 220))
		for event in pygame.event.get():
			if event.type == QUIT:
				
				#updates high scores
				app.rewrite()
				
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				#print event.key
				if event.key == 303 or event.key == 304:
					upper = True
				elif event.key == 8:
					L = L[:len(L)-1:]
				elif (event.key in beta) and len(L) <= 8:
					if upper:
						L.append(chr(event.key-32))
						upper = False
					else:
						L.append(chr(event.key))
				elif event.key == 13 and len(L) > 0:
					nwait = False
					name = ''.join(L)
					break
		screen.blit(pygame.font.Font(None, 80).render(''.join(L),1,(255,255,255)), (100, 420))
		pygame.display.flip()
		
	#calls main game function with max clicks, num of circles, num of circles on screen, and name of player
	plugin(9,15,10, name)
	
#lets player play the game
#===========================================			
def plugin(numclick, numballs, onscreen, name):

	#define variables and adds circles to screen
	#======================
	caller = numclick
	blocks = []
	for i in range(0, onscreen):
		addition()
	i = 0
	t = 0
	click = False
	w = 0
	addex = 0
	max = 0
	fulltimer = time.clock()
	
	#main game loop
	#============
	while True:
		#print time.clock()
		for event in pygame.event.get():
			if event.type == QUIT:
				app.rewrite()
				pygame.quit()
				sys.exit()
			#collects two points for cut function
			#================================
			elif event.type == MOUSEBUTTONDOWN:
				if i == 0:
					cor1 = pygame.mouse.get_pos()
					i = 1
				else:
					let = True
					for i in circles:
						if i.radius == 10:
							let = False
					if let:
						hst = cut(cor1, pygame.mouse.get_pos())
						i = 0
						t = 0
						click = True
		screen.fill((0,0,0))
		
		#manages 'cutter' circle
		if t == 11 and click:
			numclick -= 1
			circles.remove(hst)
			click = False
			if w < numballs - onscreen:
				tel = 0
				while tel < addex:
					addition()
					w += 1
					tel += 1
				addex = 0
				
		#manages circles
		for c in circles:
			pygame.draw.circle(screen, c.color, c.center, c.radius, 0)
			c.move_ip()
			c.bounce(WIDTH, HEIGHT)
			popIndex = -1
			addIndex = -1
			for x in range(0, len(circles)):
				temp1 = circles[x]
				for y in range(x+1, len(circles)):
					temp2 = circles[y]
					if temp1.colliding(temp2):
						if temp1.radius <= 10:
							popIndex = y
							addIndex = x
							break
						elif 10 >= temp2.radius:
							popIndex = x
							addIndex = y
							break
			if popIndex != -1:
				circles.pop(popIndex)
				addex += 1
				
		t += 1
		pygame.display.flip()
		#if won or lost (no circles left or run out of clicks or runs out of time) ends the loop
		if len(circles) == 0 or numclick == 0 or time.clock()-fulltimer >= 200:
			break
			
	#builds blocks for screen
	screen.fill((0,0,0))
	blocks.append(PyButton((255,255,255), Rect(200,160,400,160)))
	blocks.append(PyButton((0,150,255), Rect(200,480,400,160)))
	#calculates score from time and number of clicks used
	fintime = int((str((4000-(numclick*50))/(time.clock()-fulltimer))[:3:]))
	for btn in blocks:
		pygame.draw.rect(btn.screen, btn.color, btn.shape)
	if len(circles) == 0:
		screen.blit(pygame.font.Font(None, 80).render('Score: ' + str(fintime),1,(255,255,255)), (265, 50))
		app.main(name, fintime)
	else:
		screen.blit(pygame.font.Font(None, 80).render('You Failed',1,(255,0,0)), (265, 50))
	screen.blit(pygame.font.Font(None, 80).render('Main Menu',1,(0,0,0)), (250, 220))
	screen.blit(pygame.font.Font(None, 80).render('Try Again',1,(255,255,255)), (265, 540))
	pygame.display.flip()
	free = False
	contin = False
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				#updates high scores
				app.rewrite()
				pygame.quit()
				sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if blocks[0].contains_click(pygame.mouse.get_pos()):
					free = True
					break
				elif blocks[1].contains_click(pygame.mouse.get_pos()):
					contin = True
					break
		if free or contin:
			break
	if free:
		menu()
	else:
		plugin(caller, numballs, onscreen, name)
menu()