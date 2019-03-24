class colorClusturing:
	
	xIndex = 0
	yIndex = 0
	widthMatrix 	= 0
	heightMatrix 	= 0
	currentValue 	= 0
	currentAssigned = 0
	resultStringList 	= []
	resultColorList 	= []
	outputColorList		= []

    def create_file(self, inputMatrix, widthTemp, heightTemp):
    	self.inputArray = np.zeros(shape=(widthTemp, heightTemp))
		self.assignArray = np.zeros(shape=(widthTemp, heightTemp))
    	self.widthMatrix = widthTemp
    	self.heightMatrix = heightTemp

    def scan_cluster(self):
    	for self.yIndex in xrange(0, yMax):
			for self.xIndex in xrange(0, xMax):
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

		self.generate_output_array()
		print(outputColorList)
		# color_image_output(resultStringList, assignArray, xMax,yMax, assignCounter)

	def generate_output_array(self):
		tempList = []
		for t in xrange(0, len(self.assignNewArray)):		
			checkRepeat = 0
			for z in xrange(0, len(assignNewArray[t])):
				if assignNewArray[t][z] in tempList:
					checkRepeat = 1

			if checkRepeat == 0:		
				outputColorList[resultColorList[t][0]] += 1

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

		print finalResult
		plt.imshow(outputArray)
		plt.show()
		# img = PIL.Image.fromarray(outputArray, 'L')
		# img.save('myOutput.png')
		# img.show()

    def processed_location(self, tempX, tempY):
    	if(tempX >= 0) and (tempX < self.widthMatrix) and (tempY >= 0) and (tempY < self.heightMatrix):
			if(self.inputArray[tempX, tempY] == self.currentValue):
				if(self.assignArray[tempX, tempY] != 0):
					self.assignArray[xIndex, yIndex] = self.assignArray[tempX, tempY]
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
						self.assignArray[xIndex, yIndex] = self.assignCounter
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
