'''
################################################################################
This module provides routines that read in image recognition data sets
consisting of images and their associated ground truth.  Image recognition data
sets come in different formats so there are routines for reading each format
that has been used with nupic.vision.
################################################################################
'''

from PIL import Image
from xml.dom import minidom

DEBUG = 0



'''
################################################################################
This routine reads the XML files that contain the paths to the images and the
tags which indicate what is in the image (i.e. "ground truth").
################################################################################
'''
def getImagesAndTags(xmlFilename):
  xmldoc = minidom.parse(xmlFilename)
  # Find the path to the XML file so it can be used to find the image files.
  directoryPath = xmlFilename.replace(xmlFilename.split("/")[-1],"")
  # Read the image list from the XML file and populate images and tags.
  imageList = xmldoc.getElementsByTagName('image')
  images = []
  tags = []
  for image in imageList:
    tags.append(image.attributes['tag'].value)
    filename = image.attributes['file'].value
    images.append(Image.open(directoryPath + filename))
    #imagePatches[-1].show()
  return images, tags



