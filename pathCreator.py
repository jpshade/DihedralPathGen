import os
import groupDictionarySetup

workingDir = os.getcwd()

myGroup = ['e']
groupDict = {}

paths = []
completePaths = []
lengthAnomalies = []
prematurePaths = []

def resetGroup():
	for elementIndex in range(1,len(myGroup)):
		myGroup.pop()
	for i in list(groupDict):
		groupDict.pop(i)

	for elementIndex in range(1,len(paths)+1):
		paths.pop()
	for elementIndex in range(1,len(completePaths)+1):
		completePaths.pop()
	for elementIndex in range(1,len(lengthAnomalies)+1):
		lengthAnomalies.pop()
	for elementIndex in range(1,len(prematurePaths)+1):
		prematurePaths.pop()


def isPowerOfTwo(num):
	return bin(num).count('1') == 1

def generatePath(firstElement, secondElement, order):
	
	pathList = ['e']
	counter = 0
	newElement = ''

	while newElement not in pathList[:-1]:
		if counter%2 == 0:
			newElement = groupDict[(firstElement, pathList[-1])]
		else:
			newElement = groupDict[(secondElement, pathList[-1])]
		pathList.append(newElement)
		counter = counter + 1

	pathString = ''

	for element in pathList:
		pathString = pathString + element + ' -> '


	pathString = pathString[:-4]

	fullString =  '{:<15}: {:<10}: {}'.format('(' + firstElement + ' , ' + secondElement + ')', str(counter) + ' steps', pathString)

	pathDict = {'elements' : (firstElement, secondElement), 'pathList' : pathList, 'counter' : counter, 'fullString': fullString}

	if pathDict['counter'] == order:
		completePaths.append(pathDict)

	if (not isPowerOfTwo(pathDict['counter']) and (order % pathDict['counter'])):
		lengthAnomalies.append(pathDict)

	if (firstElement != 'e') and (secondElement != 'e') and (pathDict['pathList'][-1] != 'e'):
		prematurePaths.append(pathDict)

	return pathDict





def writeResults(order):
	
	initializeGroup(order)

	with open('D' + str(order) + 'Results.txt', 'w') as f:
		f.write('Results:\n\n')

		for firstElement in myGroup:
			for secondElement in myGroup:
				f.write(generatePath(firstElement,secondElement,order)['fullString'] + '\n')

	with open('D' + str(order) + 'SignificantPaths.txt', 'w') as f:
		f.write("Complete Paths: {}\nLength Anomalies: {}\nPremature Paths: {}\n\n".format(str(len(completePaths)),
			str(len(lengthAnomalies)), str(len(prematurePaths))))

		f.write("Complete Paths: Total {}\n\n".format(str(len(completePaths))))

		for path in completePaths:
			f.write(path['fullString']+'\n')

		f.write('\n\nLength Anomalies: Total {}\n\n'.format(str(len(lengthAnomalies))))

		for path in lengthAnomalies:
			f.write(path['fullString'] + '\n')

		f.write('\n\nPremature Paths: Total {}\n\n'.format(str(len(prematurePaths))))

		for path in prematurePaths:
			f.write(path['fullString']+'\n')


def makeMultiplicationTable(n):
	with open('D{}MultiplicationTable.py'.format(str(2*n)), 'w') as f:
		f.write('D{}: ['.format(str(2*n)))
		for element in myGroup:
			f.write(element + ' ')
		f.write(']\n')
		f.write("D{}Dict = {{\n".format(str(2*n)))
		for firstElement in myGroup:
			for secondElement in myGroup:
				newElement = groupDictionarySetup.multiply(firstElement,secondElement,n)
				f.write('\t(\'' + firstElement + '\',\'' + secondElement + '\') : \''+ newElement + '\'\n' )
				groupDict[(firstElement, secondElement)] = newElement
		f.write("}")


def initializeGroup(order):
	resetGroup()
	
	n = int(order/2)
	if not os.path.exists(workingDir + '\\D' + str(order)):
	    os.makedirs(workingDir + '\\D' + str(order))

	os.chdir(workingDir + '\\D' + str(order))

	#initialize(n, myGroup, groupDict)
	groupDictionarySetup.groupGenerate(n, myGroup)

	makeMultiplicationTable(n)

if __name__ == "__main__":
	order = int(input('2n = ? '))
	writeResults(order)