"""********************************************************************************************
Project Name    : Color Clusturing with input from .bin file and dimesion
Developer       : Lokesh Ramina
Platform        : Python 3.6 on Ubuntu 16.04
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


#*******MACROS#*******# 
ERROR		= -1
SUCCESFULL	= 0


'''***************************Variable Initialization***************************'''
__author__          = "Lokesh Ramina"

debugPrintStatus = 0                    # **USER EDIT** debug_print()function for Debug print if 1 = enable  0 = disable

arrayWidth  = 256
arrayHeight = 256
inputArray  = np.zeros(shape=(arrayWidth, arrayHeight))

'''***************************Function declaration***************************'''
class timmerMonitor:
	startValue = 0
	result = 0
	def start(self):
		self.startValue = int(round(time.time() * 1000))
	
	def stop(self):
		self.result = int(round(time.time() * 1000)) - self.startValue 

	def get_result(self):
		return self.result

class colorClusturing:	
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

	def create_file(self, inputMatrix, widthTemp, heightTemp):
		self.inputArray = np.zeros(shape=(widthTemp, heightTemp))
		self.assignArray = np.zeros(shape=(widthTemp, heightTemp))
		self.inputArray = inputMatrix
		self.widthMatrix = widthTemp
		self.heightMatrix = heightTemp

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
	
	def print_output(self):
		for x in xrange(0, len(self.outputColorList)):
			print(self.outputColorList[x])

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

	def processed_location(self, tempX, tempY):
		if(tempX >= 0) and (tempX < self.widthMatrix) and (tempY >= 0) and (tempY < self.heightMatrix):
			if(self.inputArray[tempX, tempY] == self.currentValue):
				if(self.assignArray[tempX, tempY] != 0):
					self.assignArray[self.xIndex, self.yIndex] = self.assignArray[tempX, tempY]
					self.currentAssigned = 1
					return 1
		return 0
					
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

	def insert_new_match(self, value1):
		valueStored = 0

		for x in xrange(0, len(self.resultStringList)):
			if value1 in self.resultStringList[x]:
				valueStored = 1

		if valueStored == 0:
			self.resultStringList.append([value1])
			self.resultColorList.append([self.currentValue])					

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

def file_load(imageW, imageH):
	global inputArray

	fileLocation = raw_input("Count Areas File Name : ") 	
	exists = os.path.isfile(fileLocation)
	exists = True 				#only for test
	if exists == False:
		return ERROR
	
	else:
		with open("/home/lokesh/Desktop/Projects/ColorGrouping/data/sample.bin", "rb") as f:
			for y in xrange(0, imageW):	
				for x in xrange(0, imageW):
					byte = f.read(1)
					inputArray[x, y] = ord(byte)
		return SUCCESFULL	

def print_section_from_matrix(matrix, startX, startY, w_, h_):
	tempMatrix = np.zeros(shape=(w_, h_))
	for y in xrange(0, h_):
		for x in xrange(0, w_):
			tempMatrix[x, y] = matrix[(startX+x), (startY+y)]
	print ("SUB-MATRIX")
	print (tempMatrix)

def main():
	algoTime = timmerMonitor()

	scan1 = colorClusturing()	

	if(file_load(arrayWidth, arrayHeight) == ERROR):
		print ("********FILE READING FAIL*********")
		exit()
	scan1.create_file(inputArray, arrayWidth, arrayHeight)
	algoTime.start()
	scan1.scan_cluster()
	algoTime.stop()
	scan1.print_output()
	print("algoTime = ", algoTime.get_result())

'''*************************** Main initialization ***************************'''
codeTime = timmerMonitor() 
codeTime.start()
debug_print("Author : Lokesh Ramina")
debug_print("DEBUG PRINT IS ON")

atexit.register(exit_handler)

# plt.imshow(inputArray, cmap="gray")
# plt.show()


if __name__ == "__main__":
    main()

codeTime.stop()
print("codeTime = ", codeTime.get_result())
exit()

	
