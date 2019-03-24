"""**************************************************
Project Name    : PACMAN Game with input from .txt file
Developer       : Lokesh Ramina
Platform        : Python 3.6 on Jessie- Debian
Date            : 26-02-2019
Purpose         : Practise
*****************************************************"""

import sys
import numpy as np
import os
import atexit
import PIL 
from random import randint
import matplotlib.pyplot as plt

debugPrintStatus = 1                    # **USER EDIT** debug_print()function for Debug print if 1 = enable  0 = disable

ERROR		= -1
SUCCESFULL	= 0

xIndex = 0
yIndex = 0
xMax = 256
yMax = 256

currentValue = 0
assignCounter = 0

resultString = []
newList = []

inputArray = np.zeros(shape=(xMax,yMax))
assignArray = np.zeros(shape=(xMax,yMax))

def debug_print(textToPrint):
    if debugPrintStatus:
        print(textToPrint)

def exit_handler():
    debug_print("***************Color Clusturing EXIT***************")

def load_value_mattrix(imageW, imageH):
	global inputArray
	for y in xrange(0, imageW):	
		for x in xrange(0, imageW):
			inputArray[x, y] = 125



def file_existance_check(imageW, imageH):
	global inputArray

	fileLocation = raw_input("File Name : ") 	
	exists = os.path.isfile(fileLocation)
	exists = True
	if exists == False:
		return ERROR
	
	else:
		inputArrayTemp = np.zeros(shape=(xMax,yMax),dtype = int)
		with open("/home/lokesh/Desktop/Projects/ColorGrouping/docs/sample.bin", "rb") as f:
			for y in xrange(0, imageW):	
				for x in xrange(0, imageW):
					byte = f.read(1)
					inputArray[x, y] = ord(byte)
		print inputArray
		return SUCCESFULL		

# def final_count(tempInputArray):
# 	finalResult = []
# 	tempList = []

# 	for t in xrange(0, len(assignNewArray)):		
# 		checkRepeat = 0
# 		for z in xrange(0,len(assignNewArray[t])):
# 			if assignNewArray[t][z] in tempList:
# 				checkRepeat = 1
# 		if checkRepeat == 0:		
# 			for y in xrange(0,imageH):
# 				for x in xrange(0,imageW):
# 					for z in xrange(0,len(assignNewArray[t])):			
# 						if (imageArray[x,y] == assignNewArray[t][z]):
# 							outputArray[x,y] = [rColor, gColor, bColor]
# 							x_ = x
# 							y_ = y
# 							counter += 1

# 			for z in xrange(0,len(assignNewArray[t])):
# 				tempList.append(assignNewArray[t][z])

# 			finalResult.append([inputArray[x_,y_], counter])

# 	print finalResult
# 	plt.imshow(outputArray)
# 	plt.show()

def color_image_output(assignNewArray, imageArray, imageW, imageH, counterMaxNo):
	global inputArray
	finalResult = []
	tempList = []
	outputArray = np.zeros((imageW,imageH, 3))
	
	print len(assignNewArray)
	for t in xrange(0, len(assignNewArray)):		
		checkRepeat = 0
		for z in xrange(0,len(assignNewArray[t])):
			if assignNewArray[t][z] in tempList:
				checkRepeat = 1
		if checkRepeat == 0:		
			counter = 0 
			rColor = randint(0,255)
			gColor = randint(0,255)
			bColor = randint(0,255)
			print (rColor," ", gColor, " ", bColor)
			for y in xrange(0,imageH):
				for x in xrange(0,imageW):
					for z in xrange(0,len(assignNewArray[t])):			
						if (imageArray[x,y] == assignNewArray[t][z]):
							outputArray[x,y] = [rColor, gColor, bColor]
							x_ = x
							y_ = y
							counter += 1

			for z in xrange(0,len(assignNewArray[t])):
				tempList.append(assignNewArray[t][z])

			finalResult.append([inputArray[x_,y_], counter])

	print finalResult
	plt.imshow(outputArray)
	plt.show()
	# img = PIL.Image.fromarray(outputArray, 'L')
	# img.save('myOutput.png')
	# img.show()

def print_section_from_matrix(matrix, startX, startY, w_, h_):
	tempMatrix = np.zeros(shape=(w_, h_))
	for y in xrange(0, h_):
		for x in xrange(0, w_):
			tempMatrix[x, y] = matrix[(startX+x), (startY+y)]
	print "SUB-MATRIX"
	print tempMatrix

def insert_new_match(value1, value2):
	global resultString

	valueStored = 0

	for x in xrange(0,len(resultString)):
		if value1 in resultString[x]:
			if value2 in resultString[x]:
				valueStored = 1

			else:
				resultString[x].append(value2)
				valueStored = 1
			# break

		elif value2 in resultString[x]:
			if value1 in resultString[x]:
				valueStored = 1
				b
			
			else:
				resultString[x].append(value1)
				valueStored = 1
			# break

	if valueStored == 0:
		resultString.append([value1, value2])

def insert_new_match_1(value1):
	global resultString
	
	valueStored = 0

	for x in xrange(0,len(resultString)):
		if value1 in resultString[x]:
			valueStored = 1

	if valueStored == 0:
		resultString.append([value1])

'''*************************** Main initialization ***************************'''

debug_print("Author : Lokesh Ramina")
atexit.register(exit_handler)

debug_print("READ FILE")

if(file_existance_check(xMax, yMax) == ERROR):
	print "********FILE READING FAIL*********"
	exit()


print_section_from_matrix(inputArray, 75, 110 ,50, 12)	
plt.imshow(inputArray, cmap="gray")
plt.show()
exit()

while 1:
	for yIndex in xrange(0,yMax):
		for xIndex in xrange(0,xMax):
			# print xIndex , "  ", yIndex
			if(assignArray[xIndex, yIndex] == 0):
				currentAssigned = 0
				currentValue = inputArray[xIndex, yIndex]

				tempX = xIndex - 1
				tempY = yIndex
				if(tempX >= 0) and (tempX < xMax) and (tempY >= 0) and (tempY < yMax):
					if(inputArray[tempX, tempY] == currentValue):
						if(assignArray[tempX, tempY] == 0):
							# print "error 1"
						else:
							assignArray[xIndex,yIndex] = assignArray[tempX,tempY]
							currentAssigned = 1

				tempX = xIndex - 1
				tempY = yIndex - 1
				if(tempX >= 0) and (tempX < xMax) and (tempY >= 0) and (tempY < yMax):
					if(inputArray[tempX, tempY] == currentValue):
						if(assignArray[tempX, tempY] == 0):
							# print "error 2" 
						else:
							assignArray[xIndex,yIndex] = assignArray[tempX,tempY]
							currentAssigned = 1	

				tempX = xIndex 
				tempY = yIndex - 1
				if(tempX >= 0) and (tempX < xMax) and (tempY >= 0) and (tempY < yMax):
					if(inputArray[tempX, tempY] == currentValue):
						if(assignArray[tempX, tempY] == 0):
							# print "error 3"
						else:
							assignArray[xIndex,yIndex] = assignArray[tempX,tempY]
							currentAssigned = 1			

				tempX = xIndex + 1
				tempY = yIndex - 1
				if(tempX >= 0) and (tempX < xMax) and (tempY >= 0) and (tempY < yMax):
					if(inputArray[tempX, tempY] == currentValue):
						if(assignArray[tempX, tempY] == 0):
							# print "error 4"
						else:
							assignArray[xIndex,yIndex] = assignArray[tempX,tempY]
							currentAssigned = 1		

				# NOT ASSIGN POSITION

				tempX = xIndex - 1
				tempY = yIndex + 1
				if(tempX >= 0) and (tempX < xMax) and (tempY >= 0) and (tempY < yMax):
					if(inputArray[tempX, tempY] == currentValue):

						if(assignArray[xIndex,yIndex] == 0):
							if(assignArray[tempX, tempY] == 0):
								assignCounter += 1
								assignArray[tempX,tempY] = assignCounter
								assignArray[xIndex,yIndex] = assignCounter
								currentAssigned = 1		
							else:
								assignArray[xIndex,yIndex] = assignArray[tempX,tempY]
								currentAssigned = 1		
						
						elif(assignArray[xIndex,yIndex] != assignArray[tempX, tempY]):
							if(assignArray[tempX, tempY] == 0):
								assignArray[tempX,tempY] = assignArray[xIndex,yIndex]
								currentAssigned = 1	
							else:
								# print "BOTH ARE SAME 1 : ",assignArray[tempX,tempY], "   ", assignArray[xIndex,yIndex]
								# resultString.append([assignArray[tempX,tempY], assignArray[xIndex,yIndex]])
								insert_new_match(assignArray[tempX,tempY], assignArray[xIndex,yIndex])
								currentAssigned = 1	

				tempX = xIndex
				tempY = yIndex + 1
				if(tempX >= 0) and (tempX < xMax) and (tempY >= 0) and (tempY < yMax):
					if(inputArray[tempX, tempY] == currentValue):
						if(assignArray[xIndex,yIndex] == 0):
							if(assignArray[tempX, tempY] == 0):
								assignCounter += 1
								assignArray[tempX,tempY] = assignCounter
								assignArray[xIndex,yIndex] = assignCounter
								currentAssigned = 1		
							else:
								assignArray[xIndex,yIndex] = assignArray[tempX,tempY]
								currentAssigned = 1		
						elif(assignArray[xIndex,yIndex] != assignArray[tempX, tempY]):
							if(assignArray[tempX, tempY] == 0):
								assignArray[tempX,tempY] = assignArray[xIndex,yIndex]
								currentAssigned = 1	
							else:
								# print "BOTH ARE SAME 2 : ",assignArray[tempX,tempY], "   ", assignArray[xIndex,yIndex]
								insert_new_match(assignArray[tempX,tempY], assignArray[xIndex,yIndex])
								# resultString.append([assignArray[tempX,tempY], assignArray[xIndex,yIndex]])
								currentAssigned = 1	

				tempX = xIndex + 1
				tempY = yIndex + 1
				if(tempX >= 0) and (tempX < xMax) and (tempY >= 0) and (tempY < yMax):
					if(inputArray[tempX, tempY] == currentValue):
						if(assignArray[xIndex,yIndex] == 0):
							if(assignArray[tempX, tempY] == 0):
								assignCounter += 1
								assignArray[tempX,tempY] = assignCounter
								assignArray[xIndex,yIndex] = assignCounter
								currentAssigned = 1		
							else:
								assignArray[xIndex,yIndex] = assignArray[tempX,tempY]
								currentAssigned = 1		
						elif(assignArray[xIndex,yIndex] != assignArray[tempX, tempY]):
							if(assignArray[tempX, tempY] == 0):
								assignArray[tempX,tempY] = assignArray[xIndex,yIndex]
								currentAssigned = 1	
							else:
								# print "BOTH ARE SAME 3 : ",assignArray[tempX,tempY], "   ", assignArray[xIndex,yIndex]
								insert_new_match(assignArray[tempX,tempY], assignArray[xIndex,yIndex])
								# resultString.append([assignArray[tempX,tempY], assignArray[xIndex,yIndex]])
								currentAssigned = 1	

				tempX = xIndex + 1
				tempY = yIndex
				if(tempX >= 0) and (tempX < xMax) and (tempY >= 0) and (tempY < yMax):
					if(inputArray[tempX, tempY] == currentValue):
						if(assignArray[xIndex,yIndex] == 0):
							if(assignArray[tempX, tempY] == 0):
								assignCounter += 1
								assignArray[tempX,tempY] = assignCounter
								assignArray[xIndex,yIndex] = assignCounter
								currentAssigned = 1		
							else:
								assignArray[xIndex,yIndex] = assignArray[tempX,tempY]
								currentAssigned = 1		
						elif(assignArray[xIndex,yIndex] != assignArray[tempX, tempY]):
							if(assignArray[tempX, tempY] == 0):
								assignArray[tempX,tempY] = assignArray[xIndex,yIndex]
								currentAssigned = 1	
							else:
								# print "BOTH ARE SAME 4 : ",assignArray[tempX,tempY], "   ", assignArray[xIndex,yIndex]
								insert_new_match(assignArray[tempX,tempY], assignArray[xIndex,yIndex])
								# resultString.append([assignArray[tempX,tempY], assignArray[xIndex,yIndex]])
								currentAssigned = 1

				if(currentAssigned == 0):
					assignCounter += 1
					assignArray[xIndex,yIndex] = assignCounter
					insert_new_match_1(assignCounter)
					# print "NO MATCH FOUND"
	# print "OUTPUT ARRAY : " 
	# print assignArray
	
	for x in xrange(0, len(resultString)):
		print resultString[x]


	color_image_output(resultString, assignArray, xMax,yMax, assignCounter)

	exit()

	
