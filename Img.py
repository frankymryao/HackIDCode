#!/usr/bin/python

import Image
import numpy
import urllib2
import time

class Img(object):
    
    def __init__(self,img_path):
        self.__img_url = urllib2.urlopen(img_path)
        self.__file_name = time.strftime("%Y%m%d%H%M%S")+".jpg"
        o = open(self.__file_name,"aw")
        o.writelines(self.__img_url.readlines())
        o.close()
        self.__img = Image.open(self.__file_name)
    
    def getMatrix(self):
		return numpy.asarray(self.__img)

if __name__ == "__main__":
    img = Img("http://hub.hust.edu.cn/randomImage.action")
    print img.getMatrix()
