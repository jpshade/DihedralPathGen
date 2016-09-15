import pathCreator
import os
import pandas as pd


'''
TODO:

output to excel 

highlight important cells


'''

def makeDataFrame(myWorkDir, order):
	counterDict = {}
	with open(os.path.join(myWorkDir, 'D{}ResultsDict.txt'.format(order)), 'r') as f:
		counterDict = eval(f.read())
	return pd.DataFrame(counterDict)


def sortedDataFrame(myWorkDir, order):
	orderList = []

	with open(os.path.join(myWorkDir, 'D{}Group.txt'.format(order)), 'r') as f:
		orderList = eval(f.read())

	myFrame = makeDataFrame(myWorkDir, order).reindex_axis(orderList, axis=1)
	myFrame = myFrame.reindex_axis(orderList, axis=0)

	return myFrame





def makeExcelSheet(myWorkDir, order):
	pass




if __name__ == '__main__':
	order = int(input('2n = ? '))
	myWorkDir = writeResults(order)

