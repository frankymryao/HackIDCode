#!/usr/bin/python

import Image
import numpy

class Img(object):
	def __init__(self,file_path):
		self.__img = Image.open(file_path)
	
	def getMatrix(self):
		return numpy.asarray(self.__img)
