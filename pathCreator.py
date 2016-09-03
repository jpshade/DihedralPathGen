import os
from groupDictionarySetup import *

if not os.path.exists('D' + str(order)):
    os.makedirs('D' + str(order))

os.chdir('.\\D' + str(order))

initialize()

paths = []

completePaths = []

lengthAnomalies = []

prematurePaths = []

def isPowerOfTwo(num):
	return bin(num).count('1') == 1

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

	fullString =  '{:<15}: {:<10}: {}'.format('(' + firstElement + ' , ' + secondElement + ')', str(counter) + ' steps', pathString)

	pathDict = {'elements' : (firstElement, secondElement), 'pathList' : pathList, 'counter' : counter, 'fullString': fullString}

	if pathDict['counter'] == order:
		completePaths.append(pathDict)

	if (not isPowerOfTwo(pathDict['counter']) and (order % pathDict['counter'])):
		lengthAnomalies.append(pathDict)

	if (firstElement != 'e') and (secondElement != 'e') and (pathDict['pathList'][-1] != 'e'):
		prematurePaths.append(pathDict)

	return pathDict






with open('D' + str(order) + 'Results.txt', 'w') as f:
	f.write('Results:\n\n')

	for firstElement in myGroup:
		for secondElement in myGroup:
			f.write(generatePath(firstElement,secondElement)['fullString'] + '\n')

with open('D' + str(order) + 'SignificantPaths.txt', 'w') as f:
	f.write("Complete Paths: Total {}\n\n".format(str(len(completePaths))))

	for path in completePaths:
		f.write(path['fullString']+'\n')

	f.write('\n\nLength Anomalies: Total {}\n\n'.format(str(len(lengthAnomalies))))

	for path in lengthAnomalies:
		f.write(path['fullString'] + '\n')

	f.write('\n\nPremature Paths: Total {}\n\n'.format(str(len(prematurePaths))))

	for path in prematurePaths:
		f.write(path['fullString']+'\n')