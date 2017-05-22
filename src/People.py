import numpy as np
import random


class People(object):

	def __init__(self, mom=None, dad=None):
		if mom is None or dad is None:
			self.generateDefaults()
			#TODO separate male and female defaults
		else:
			self.getGenetics(mom, dad)

	def generateDefaults(self):
		'''
		sets the default value according world average
		weight and height defaults is according to CDC paper
		https://www.cdc.gov/nchs/data/ad/ad347.pdf
		'''
		self.geneder = self.randomGender()
		self.age = 0
		self.height = np.random.normal(170, 8.5) # average, stdev
		self.weight = np.random.normal(72, 13)
		self.lifeSpan = np.random.normal(79, 15)

	def randomGender(self):
		gender = None
		sex = random.randint(0, 1)
		if sex == 0:
			gender = 'MALE'
		else:
			gender = 'FEMALE'
		return gender

	def getGenetics(self, mom, dad):
		momGene = self.getMomGenes(mom)
		dataGene = self.getDadGenes(dad)
		myGene = self.mixGenes(momGene, dataGene)
		return myGene

	def getMomGenes(self, mom):
		return mom

	def getDadGenes(self, dad):
		return dad

	def mixGenes(self, mom, dad):
		mixedGenes = People()

		return mixedGenes

	def sleep():
		pass

	def eat():
		pass

	def drink():
		pass

	def breath():
		pass

	def grow():
		pass

	def die():
		pass

	def poop():
		pass

	def urinate():
		pass

	def play():
		pass
