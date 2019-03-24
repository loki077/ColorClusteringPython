import sys
import numpy as np
import os
import atexit
from PIL import Image

tempList = []
inputArrayTemp = np.zeros(shape=(256,256),dtype = int)

def exit_handler():
    print "***************Color Clusturing EXIT***************"

atexit.register(exit_handler)

fileLocation = raw_input("File Name : ") 	
exists = os.path.isfile(fileLocation)
print exists
exists = True
if exists == False:
	exit()
	
else:
	# print "FILE READ COMPLETE"
	# with open("/home/lokesh/Desktop/Projects/ColorGrouping/docs/sample.bin", "rb") as f:
	# 	byte = f.read(1)
 #    	while byte != "":
	# 		byte = f.read(1)
			# tempList.append(byte)
	for y in xrange(0,255):
		for x in xrange(0,255):
			inputArrayTemp [x, y] = 125

img = Image.fromarray(inputArrayTemp, 'L')
img.save('myOutput.png')
img.show()

# print len(tempList)
				