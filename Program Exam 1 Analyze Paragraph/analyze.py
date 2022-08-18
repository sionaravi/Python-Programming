# Siona Ravi
# CSCI 236
# Sep 25, 2020
# analyze.py
# 30 mins
# A version
# It was a bit tricky
# Status: It compiles very well

def analyze_paragraphs(test1):
	'''
This Function Returns the max number of lines present in a paragraphs
and displays the number of lines for each paragraph.

Parameters:
fileName (string): input file name

Returns:
maxValue (int): returns the maximum lines count for a paragraph
from the given input file(fileName).
'''
	maxValue = 0
	lineCount = 0
	try:
	  	with open(test1, "r") as test1:
			test1 = test1
			lines - test1.readlines()
			for line in lines:
				temp = line.split()
				if temp[0] == "<p>":
					print("%d-line paragraph" %lineCount)
					if maxValue < lineCount:
						maxValue = lineCount
						lineCount = 0
				else:
					lineCount += 1
			return maxValue

	except IOError:
		print("Unable to open the inout file.")
		return maxValue

def main():
	max = analyze_paragraphs("test1.txt")

	print("Maximum value for the input file: %d" %(max))


if __name__ == '__main__':
	main()
