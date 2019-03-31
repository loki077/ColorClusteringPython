# ColorClusteringPython
Description:
	This is a python code for finding color patches in an image or 		binary input

This is a Repository maintained and developed by Lokesh Ramina
===================================================================
About: 
 	The code is about color clusturing in 2D image.
 	Taking inputs as .bin file.

Prerequisit:
	python2.7 should be installed
	python-pip should be install in the system.
		To install you can the command as per below instruction.
		# cd ../ColorClusteringPython
		# sudo apt install python-pip
		once installed 
		# pip install -r requirements.tx

Instrution to execute file:
	Make sure the prerequisite is completed
	The main code is in ../ColorClusteringPython/main
	Save the .bin file in the main folder
	file name main.py
	To run the code:
		# cd .../ColorClusteringPython/main/dist/count-areas
		# ./count-areas <sub Location> --shape <Height>,<Width>
		>count-areas <sub Location> --shape <Height>,<Width> 	
		eg : count-areas data/sample.bin --shape 256,256
	if everything is perfect output will be generated or else code will exit.

-------------------------------------------------------------------
Allgorithm explained:
	The logic is developed by Lokesh Ramina
	Considering the below matrix.
	
	| 120  120  120  003  000|
	| 120  120	120  003  003|	
	| 003  120  120  120  003|
	| 003  003  003  003  003|
	| 003  003  003  003  003|
	
	> create a parallel similar matrix which will have assignment of group value
	> moving from 0,0 to w_,h_ it will check the position is assigned or not if not than will process the positon
	> In process it checks the color value of near 8 locations and if any has same value than both gets assigned into same group and so on.
	> output below of above image assign matrix

	| 1  1  1  2  3|
	| 1  1	1  2  2|	
	| 2  1  1  1  2|
	| 2  2  2  2  2|
	| 2  2  2  2  2|

	