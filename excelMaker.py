import pathCreator
import os
import pandas as pd


'''
TODO:

Order dataframe

output to excel 

highlight important cells


'''

def makeDataFrame(myWorkDir, order):
	counterDict = {}
	with open(os.path.join(myWorkDir, 'D{}ResultsDict.txt'.format(order)), 'r') as f:
		counterDict = eval(f.read())
	return pd.DataFrame(counterDict)






def makeExcelSheet(myWorkDir, order):
	pass




if __name__ == '__main__':
	order = int(input('2n = ? '))
	myWorkDir = writeResults(order)

