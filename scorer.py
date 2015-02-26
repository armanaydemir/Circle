#!/usr/bin/env python2.7
# manages individual scores
# Arman Aydemir
# April 28th, 2014
class Scorer:
	name = None
	score = 0
	
	def __init__(self, n, score):
		self.name = n
		self.score = score
		
	def __cmp__(self, other):
		diff = self.score - other.score
		if diff == 0:
			diff = self.name < other.name
		#print diff
		return diff
	
	def __str__(self):
		return (self.name + ' ' + str(self.score))
		
		
		
		
		
		