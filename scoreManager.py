#!/usr/bin/env python2.7
# manages the highscores list and scores.txt
# Arman Aydemir
# April 28th, 2014
from scorer import Scorer

class ScoreManager:
	highScores = []
	file = None
	maxHighScores = 6
	
	def __init__(self, filename):
		self.file = open(filename, 'r')
		self.maxHighScores = 10
		for line in self.file:
			temp = line.split()
			name = temp[0]
			score = temp[1]		
			score = int(score)	# gets rid of \n and converts to int
			self.highScores.append(Scorer(name, score))
		# for loop ended, so close the file stream
		self.file.close()
		self.sortScorers()
			
	def sortScorers(self):
		self.highScores = sorted(self.highScores, reverse = True)
	
	def printList(self):
		t = []
		for i in self.highScores:
			t.append(i)
		return t
	
	def isNewHighScore(self, score):
		if len(self.highScores) < self.maxHighScores:
			return True
		lastIndex = len(self.highScores) - 1
		if len(self.highScores) == 0:
			lastIndex = 0
		return self.highScores[lastIndex].score < score
	
	def addNewHighScore(self, person):
		if len(self.highScores) < self.maxHighScores:
			self.highScores.append(person)
		else:
			lastIndex = len(self.highScores) - 1
			self.highScores[lastIndex] = person
			
	#what to do when a new score is introduced, checks if it is supposed to be in high scores and if so adds it to high scores then sorts the file
	#===========================
	def main(self, p, score):
		person = Scorer(p, score)
		if self.isNewHighScore(score):
			self.addNewHighScore(person)
			self.sortScorers()
	
	def rewrite(self):
		self.fi = open('scores.txt', 'w')
		self.sortScorers()
		for i in self.highScores:
			self.fi.write(str(i.name) + ' ' + str(i.score) + '\n')
		self.fi.close()
