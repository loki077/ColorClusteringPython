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
# import atexit
import numpy as np
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
		self.inputArray = np.zeros(shape=(heightTemp, widthTemp))
		self.assignArray = np.zeros(shape=(heightTemp, widthTemp))
		self.inputArray = inputMatrix
		self.widthMatrix = widthTemp
		self.heightMatrix = heightTemp

	# main algorithm to Scan the matrix and give result
	def scan_cluster(self):
		for self.yIndex in range(0,  self.heightMatrix):
			for self.xIndex in range(0, self.widthMatrix):
				if(self.assignArray[self.yIndex, self.xIndex] == 0):
					self.currentAssigned = 0
					self.currentValue = self.inputArray[self.yIndex, self.xIndex]

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
					self.assignArray[self.yIndex, self.xIndex] = self.assignCounter
					self.insert_new_match(self.assignCounter)

		self.generate_output_array(self.resultStringList)			
		# color_image_output(resultStringList, assignArray, self.widthMatrix, self.heightMatrix, assignCounter)
	
	# use this to print 255 array
	def print_output(self):
		for x in range(0, len(self.outputColorList)):
			print(self.outputColorList[x])

	# This generates the final output
	def generate_output_array(self, assignNewArray):
		tempList = []
		for t in range(0, len(assignNewArray)):		
			checkRepeat = 0
			for z in range(0, len(assignNewArray[t])):
				if assignNewArray[t][z] in tempList:
					checkRepeat = 1
					break
			for z in range(0,len(assignNewArray[t])):
				tempList.append(assignNewArray[t][z])

			if checkRepeat == 0:		
				index = int(self.resultColorList[t][0])
				self.outputColorList[index] += 1

	# This generates the digital view of it
	def color_image_output(self,assignNewArray, imageArray, imageW, imageH, counterMaxNo):
		finalResult = []
		tempList = []
			
		for t in range(0, len(self.assignNewArray)):		
			checkRepeat = 0

			for z in range(0,len(assignNewArray[t])):
				if assignNewArray[t][z] in tempList:
					checkRepeat = 1

			if checkRepeat == 0:		
				counter = 0 

				for y in range(0,imageH):
					for x in range(0,imageW):
						for z in range(0,len(assignNewArray[t])):			
							if (imageArray[y, x] == assignNewArray[t][z]):
								outputArray[y,x] = [rColor, gColor, bColor]
								x_ = x
								y_ = y
								counter += 1

				for z in range(0,len(assignNewArray[t])):
					tempList.append(assignNewArray[t][z])

				finalResult.append([inputArray[y_,x_], counter])

	# Algorithm previous position checking code
	def processed_location(self, tempX, tempY):
		if(tempX >= 0) and (tempX < self.widthMatrix) and (tempY >= 0) and (tempY < self.heightMatrix):
			if(self.inputArray[tempY, tempX] == self.currentValue):
				if(self.assignArray[tempY, tempX] != 0):
					self.assignArray[self.yIndex, self.xIndex] = self.assignArray[tempY, tempX]
					self.currentAssigned = 1
					return 1
		return 0
					
	# Algorithm non allocated position checking code
	def other_location(self, tempX, tempY):
		if(tempX >= 0) and (tempX < self.widthMatrix) and (tempY >= 0) and (tempY < self.heightMatrix):
			if(self.inputArray[tempY, tempX] == self.currentValue):
				if(self.assignArray[self.yIndex, self.xIndex] == 0):
					if(self.assignArray[tempY, tempX] == 0):
						self.assignCounter += 1
						self.assignArray[tempY, tempX] 	 = self.assignCounter
						self.assignArray[self.yIndex, self.xIndex] = self.assignCounter
						self.currentAssigned = 1
						return 1	

					else:
						self.assignArray[self.yIndex, self.xIndex] = self.assignArray[tempY, tempX]
						self.currentAssigned = 1
						return 1		
				
				elif(self.assignArray[self.yIndex, self.xIndex] != self.assignArray[tempY, tempX]):
					if(self.assignArray[tempY, tempX] == 0):
						self.assignArray[tempY, tempX] = self.assignArray[self.yIndex, self.xIndex]
						self.currentAssigned = 1
						return 1	

					else:
						self.insert_match(self.assignArray[tempY, tempX], self.assignArray[self.yIndex, self.xIndex])
						self.currentAssigned = 1
						return 1
		return 0	

	# inserts and dataset with different assignment but same cluster
	def insert_match(self, value1, value2):
		valueStored = 0

		for x in range(0, len(self.resultStringList)):
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

		for x in range(0, len(self.resultStringList)):
			if value1 in self.resultStringList[x]:
				valueStored = 1

		if valueStored == 0:
			self.resultStringList.append([value1])
			self.resultColorList.append([self.currentValue])					


'''***************************Function declaration***************************'''

#To load file and extract output 
def file_load():
	global inputArray
	global arrayWidth, arrayHeight
	#count-areas <input-filename> --shape <height>,<width>"
	#count-areas data/sample.bin --shape 256,256
	# rawData = raw_input("") 	
	# rawDataList  = rawData.split()
	# fileLocation = rawDataList[1]
	# arrayList    = rawDataList[3].split(',') 
	# arrayHeight = int(arrayList[0])
	# arrayWidth  = int(arrayList[1])
	
	if (len(sys.argv) != 4):
		print ("argument error")
		# exit()

	fileLocation = sys.argv[1]
	arrayList    = sys.argv[3].split(',') 
	arrayHeight  = int(arrayList[0])
	arrayWidth   = int(arrayList[1])
	
	inputArray  = np.zeros(shape=(arrayHeight, arrayWidth))
	
	# exists = os.path.isfile(fileLocation)
	exists = os.path.isfile(fileLocation)
	# exists = True 				#only for test
	if exists == False:
		print ("File Error")
		# exit()
	
	else:
		with open(fileLocation, "rb") as f:
			for y in range(0, arrayHeight):	
				for x in range(0, arrayWidth):
					byte = f.read(1)
					inputArray[y, x] = ord(byte)
		return inputArray	

scan1 = ColorClusturing()
scan1.create_file(file_load(), arrayWidth, arrayHeight)
scan1.scan_cluster()
scan1.print_output()

