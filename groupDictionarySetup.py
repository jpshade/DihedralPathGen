import re

#myGroup = ['e', 'r1', 'r2', 'r3', 's', 'r1s', 'r2s', 'r3s']

myGroup = ['e']
groupDict = {}

order = int(input("2n = ? "))


n = int(order/2)

def groupGenerate():
	for i in range(1,n):
		myGroup.append('r'+ str(i))

	myGroup.append('s')

	for i in range(1,n):
		myGroup.append('r'+str(i)+'s')


def rrChange(matchedSubstring):
	numLengthCheck = re.compile('[0-9]+')

	exponents = numLengthCheck.findall(matchedSubstring)
	newExponent = 0

	for num in exponents:
		newExponent = newExponent + int(num)

	return newExponent


def srChange(matchedSubstring):
	numLengthCheck = re.compile('[0-9]+')

	exponent = numLengthCheck.findall(matchedSubstring)

	return int(exponent[0])*(n-1)


def rNChange(matchedSubstring):
	numLengthCheck = re.compile('[0-9]+')

	exponent = numLengthCheck.findall(matchedSubstring)

	return int(exponent[0])-n


def multiply(firstElement, secondElement):

	#Regex for determining if two r values next to each other

	rrCheck = re.compile('r[0-9]+r[0-9]+')

	#regex for determining if r comes after s

	srCheck = re.compile('sr[0-9]+')

	#regex for checking if an r exponent is greater than n

	rNCheck = re.compile('[0-9]+')

	totalString = firstElement + secondElement

	if 'e' in totalString:
		totalString = totalString.replace('e','')

	#Loop to make replacements. If element is in D8 or is empty, exit loop

	while True:

		changesMade = False

		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		#replace sr with r(n-1)

		srMatch = srCheck.search(totalString)

		while srMatch:
			totalString = totalString[:srMatch.start()] + 'r' + str(srChange(totalString[srMatch.start():srMatch.end()])) + 's' + totalString[srMatch.end():]
			changesMade = True
			srMatch = srCheck.search(totalString)

		#~~~~~~~~~~~~~~~~~~~~~~~

		#if r values side by side, add exponents

		rrMatch = rrCheck.search(totalString)

		while rrMatch:
			newExponent = rrChange(totalString[rrMatch.start():rrMatch.end()])
			totalString = totalString[:rrMatch.start()] + 'r' + str(newExponent) + totalString[rrMatch.end():]
			changesMade = True
			rrMatch = rrCheck.search(totalString)

		#~~~~~~~~~~~~~~~~~~~~~~~~`
		#Check r4

		rNMatch = rNCheck.findall(totalString)

		for exponent in rNMatch:
			if int(exponent) >= n:
				newExponent = int(exponent) % n
				totalString = totalString.replace(exponent, str(newExponent))

		'''
		while rNMatch:


			newExponent = rNChange(totalString[rNMatch.start():rNMatch.end()])
			totalString = totalString[:rNMatch.start() + 1] + str(newExponent) + totalString[rNMatch.end():]
			changesMade = True
			rNMatch = rNCheck.search(totalString)
		'''

		if ('ss' in totalString) or ('r0' in totalString):
			totalString = totalString.replace('ss', '').replace('r0', '')
			changesMade = True

		#Check exit condition
		
		if not changesMade:
			break

	if totalString == '':
		totalString = 'e'

	return totalString






def initialize():

	groupGenerate()

	with open('D' + str(order) + 'multiply.txt', 'w') as f:
		f.write("Group: [ ")

		for element in myGroup:
			f.write(element + ' ')
		f.write(']\n')

		f.write("groupDict = {")
		for firstElement in myGroup:
			for secondElement in myGroup:
				newElement = multiply(firstElement,secondElement)
				f.write('\t(\'' + firstElement + '\',\'' + secondElement + '\') : \''+ newElement + '\'\n' )
				groupDict[(firstElement, secondElement)] = newElement

		f.write("}")


