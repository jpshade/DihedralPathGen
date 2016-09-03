from groupDictionarySetup import *

initialize()

paths = []

def generatePath(firstElement, secondElement):
	
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

	fullString =  '(' + firstElement + ' , ' + secondElement + ') : ' +  str(counter) + ' steps : ' + pathString

	return {'elements' : (firstElement, secondElement), 'pathList' : pathList, 'counter' : counter, 'fullString': fullString}

with open('D' + str(n) + 'Results.txt', 'w') as f:
	f.write('Results:\n\n')

	for firstElement in myGroup:
		for secondElement in myGroup:
			f.write(generatePath(firstElement,secondElement)['fullString'] + '\n')