"""********************************************************************************************
Project Name    : Color Clusturing with input from .bin file and dimesion
Developer       : Lokesh Ramina
Platform        : Python 2.7 on Ubuntu 16.04
Date            : 22-03-2019
Purpose         : Task
Note			: Please go through the readme.txt file to understand the code and concept
********************************************************************************************"""

'''***************************Library Import***************************'''
import sys
import os
import atexit
import numpy as np
import matplotlib.pyplot as plt
import time


#*******MACROS*******# 
ERROR		= -1
SUCCESFULL	= 0


'''***************************Variable Initialization***************************'''
__author__          = "Lokesh Ramina"

debugPrintStatus = 0                    # **USER EDIT** debug_print()function for Debug print if 1 = enable  0 = disable

arrayWidth  = 10
arrayHeight = 10


'''***************************Class declaration***************************'''
# Class TimmerMonitor is used to track time for any execution
class TimmerMonitor:
	startValue = 0
	result = 0
	#Call start to start timmer
	def start(self):
		self.startValue = int(round(time.time() * 1000))
	
	#Call stop to stop timmer
	def stop(self):
		self.result = int(round(time.time() * 1000)) - self.startValue 

	#Call to get result timmer it has a return type of int
	def get_result(self):
		return self.result

# Class main for detecting patches of different color shade 
class ColorClusturing:	
	xIndex = 0
	yIndex = 0
	widthMatrix 	= 0
	heightMatrix 	= 0
	currentValue 	= 0
	currentAssigned = 0
	assignCounter 	= 0
	resultStringList 	= []
	resultColorList 	= []
	outputColorList		= [0]*256

	# inputMatrix = the matrix to operate on
	# widthTemp = width of matrix
	# heightTemp = height of matrix
	def create_file(self, inputMatrix, widthTemp, heightTemp):
		self.inputArray = np.zeros(shape=(widthTemp, heightTemp))
		self.assignArray = np.zeros(shape=(widthTemp, heightTemp))
		self.inputArray = inputMatrix
		self.widthMatrix = widthTemp
		self.heightMatrix = heightTemp

	# main algorithm to Scan the matrix and give result
	def scan_cluster(self):
		for self.yIndex in xrange(0,  self.heightMatrix):
			for self.xIndex in xrange(0, self.widthMatrix):
				if(self.assignArray[self.xIndex, self.yIndex] == 0):
					self.currentAssigned = 0
					self.currentValue = self.inputArray[self.xIndex, self.yIndex]

					# scan of location previously assigned
					self.processed_location((self.xIndex - 1), (self.yIndex   ))
					self.processed_location((self.xIndex - 1), (self.yIndex - 1))
					self.processed_location((self.xIndex    ), (self.yIndex - 1))
					self.processed_location((self.xIndex + 1), (self.yIndex - 1))

					# scan of location not assigned
					self.other_location((self.xIndex - 1), (self.yIndex + 1))
					self.other_location((self.xIndex    ), (self.yIndex + 1))
					self.other_location((self.xIndex + 1), (self.yIndex + 1))
					self.other_location((self.xIndex + 1), (self.yIndex    ))		

				if(self.currentAssigned == 0):
					self.assignCounter += 1
					self.assignArray[self.xIndex, self.yIndex] = self.assignCounter
					self.insert_new_match(self.assignCounter)

		self.generate_output_array(self.resultStringList)			
		# color_image_output(resultStringList, assignArray, self.widthMatrix, self.heightMatrix, assignCounter)
	
	# use this to print 255 array
	def print_output(self):
		for x in xrange(0, len(self.outputColorList)):
			print(self.outputColorList[x])

	# This generates the final output
	def generate_output_array(self, assignNewArray):
		tempList = []
		for t in xrange(0, len(assignNewArray)):		
			checkRepeat = 0
			for z in xrange(0, len(assignNewArray[t])):
				if assignNewArray[t][z] in tempList:
					checkRepeat = 1
					break
			for z in xrange(0,len(assignNewArray[t])):
				tempList.append(assignNewArray[t][z])

			if checkRepeat == 0:		
				index = int(self.resultColorList[t][0])
				self.outputColorList[index] += 1

	# This generates the digital view of it
	def color_image_output(self,assignNewArray, imageArray, imageW, imageH, counterMaxNo):
		finalResult = []
		tempList = []
			
		for t in xrange(0, len(self.assignNewArray)):		
			checkRepeat = 0

			for z in xrange(0,len(assignNewArray[t])):
				if assignNewArray[t][z] in tempList:
					checkRepeat = 1

			if checkRepeat == 0:		
				counter = 0 

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

	# Algorithm previous position checking code
	def processed_location(self, tempX, tempY):
		if(tempX >= 0) and (tempX < self.widthMatrix) and (tempY >= 0) and (tempY < self.heightMatrix):
			if(self.inputArray[tempX, tempY] == self.currentValue):
				if(self.assignArray[tempX, tempY] != 0):
					self.assignArray[self.xIndex, self.yIndex] = self.assignArray[tempX, tempY]
					self.currentAssigned = 1
					return 1
		return 0
					
	# Algorithm non allocated position checking code
	def other_location(self, tempX, tempY):
		if(tempX >= 0) and (tempX < self.widthMatrix) and (tempY >= 0) and (tempY < self.heightMatrix):
			if(self.inputArray[tempX, tempY] == self.currentValue):
				if(self.assignArray[self.xIndex, self.yIndex] == 0):
					if(self.assignArray[tempX, tempY] == 0):
						self.assignCounter += 1
						self.assignArray[tempX, tempY] 	 = self.assignCounter
						self.assignArray[self.xIndex, self.yIndex] = self.assignCounter
						self.currentAssigned = 1
						return 1	

					else:
						self.assignArray[self.xIndex, self.yIndex] = self.assignArray[tempX, tempY]
						self.currentAssigned = 1
						return 1		
				
				elif(self.assignArray[self.xIndex, self.yIndex] != self.assignArray[tempX, tempY]):
					if(self.assignArray[tempX, tempY] == 0):
						self.assignArray[tempX, tempY] = self.assignArray[self.xIndex, self.yIndex]
						self.currentAssigned = 1
						return 1	

					else:
						self.insert_match(self.assignArray[tempX, tempY], self.assignArray[self.xIndex, self.yIndex])
						self.currentAssigned = 1
						return 1
		return 0	

	# inserts and dataset with different assignment but same cluster
	def insert_match(self, value1, value2):
		valueStored = 0

		for x in xrange(0, len(self.resultStringList)):
			if value1 in self.resultStringList[x]:
				if value2 in self.resultStringList[x]:
					valueStored = 1

				else:
					self.resultStringList[x].append(value2)
					self.resultColorList[x].append(self.currentValue)					
					valueStored = 1
				
			elif value2 in self.resultStringList[x]:
				if value1 in self.resultStringList[x]:
					valueStored = 1
				
				else:
					self.resultStringList[x].append(value1)
					self.resultColorList[x].append(self.currentValue)					
					valueStored = 1

		if valueStored == 0:
			self.resultStringList.append([value1, value2])
			self.resultColorList.append([self.currentValue])					

	# inserts and dataset with new assignment
	def insert_new_match(self, value1):
		valueStored = 0

		for x in xrange(0, len(self.resultStringList)):
			if value1 in self.resultStringList[x]:
				valueStored = 1

		if valueStored == 0:
			self.resultStringList.append([value1])
			self.resultColorList.append([self.currentValue])					


'''***************************Function declaration***************************'''

#debug purpose print 
def debug_print(textToPrint):
    if debugPrintStatus:
        print(textToPrint)

#whenever code exits will compile here once 
def exit_handler():
    debug_print("***************Color Clusturing EXIT***************")

#load a fixed value to matrix 
def load_value_mattrix(imageW, imageH, value):
	global inputArray
	for y in xrange(0, imageW):	
		for x in xrange(0, imageW):
			inputArray[x, y] = value

#To load file and extract output 
def file_load():
	global inputArray
	global arrayWidth, arrayHeight

	fileLocation = raw_input("count-areas ") 	
	print '\033[{}C\033[1A'.format(12 + len(fileLocation)),
	arrayHeightTemp = raw_input("--shape ") 	
	print '\033[{}C\033[1A'.format(12 + len(fileLocation)+ 8 + len(str(arrayHeight))+ 1),
	arrayWidthTemp = raw_input(",") 	

	arrayHeight = int(arrayHeightTemp)
	arrayWidth = int(arrayWidthTemp)
	inputArray = np.zeros(shape=(arrayWidth, arrayHeight))
	
	exists = os.path.isfile(fileLocation)
	# exists = True 				#only for test
	if exists == False:
		exit()
	
	else:
		with open(fileLocation, "rb") as f:
			for y in xrange(0, arrayHeight):	
				for x in xrange(0, arrayWidth):
					byte = f.read(1)
					inputArray[x, y] = ord(byte)
		return inputArray	

#To view a block of matrix
def print_section_from_matrix(matrix, startX, startY, w_, h_):
	tempMatrix = np.zeros(shape=(w_, h_))
	for y in xrange(0, h_):
		for x in xrange(0, w_):
			tempMatrix[x, y] = matrix[(startX+x), (startY+y)]
	print ("SUB-MATRIX")
	print (tempMatrix)

# Main execution code
def main():
	algoTime = TimmerMonitor()

	scan1 = ColorClusturing()	

	scan1.create_file(file_load(), arrayWidth, arrayHeight)
	algoTime.start()
	scan1.scan_cluster()
	algoTime.stop()
	scan1.print_output()
	# print("algoTime = ", algoTime.get_result())

'''*************************** Main initialization ***************************'''
codeTime = TimmerMonitor() 
codeTime.start()
debug_print("Author : Lokesh Ramina")
debug_print("DEBUG PRINT IS ON")

atexit.register(exit_handler)

if __name__ == "__main__":
    main()

codeTime.stop()
exit()

	
