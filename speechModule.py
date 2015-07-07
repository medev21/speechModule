

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):

    #replace this for solution
	numStr = str(number)	#convert number to a string
	numStrLength = len(numStr)	#store numStr length
	
	result = []		#empty result array
	firstTenArray = FIRST_TEN		#store FIRST_TEN array
	secondTenArray = SECOND_TEN	#store SECOND_TEN array
	otherTenArray = OTHER_TENS		#store OTHER_TENS array
	
	#check the number of digits(3 to 1)
	if numStrLength == 3:
		firstDig = int(numStr[0])	#store first digit(0 to 9)
		secondDig = int(numStr[1] + numStr[2])	#store second digit in the tens(e.g 11, 12)
		secondSingleDig = int(numStr[1])	#store  second digit above 2
		thirdDig = int(numStr[2])	#store third digit(0 to 9)
		count = 1
		#when appending, it call getWordNum function with 3 arguments)
		#it returns the word for the first digit
		result.append(getWordNum(count, firstDig, firstTenArray))
		result.append(HUNDRED)
		
		#check 2nd and 3rd digit if they are zero, return nothing
		if (numStr[1] == "0") and (numStr[2] == "0"):
			print(result)
		elif numStr[1] == "0":		#if 3rd dig is 0, then get word for 3rd digit
			result.append(getWordNum(count, thirdDig, firstTenArray))
			print(result)
		elif numStr[1] == "1":	#if 2nd dig is 1, then get word for 2nd digit TENS
			count = 10
			result.append(getWordNum(count, secondDig, secondTenArray))
			print(result)
		elif numStr[1] > "1" and numStr[2] == "0":	#if 2nd dig is  greater 1 and 3rd is 0, then get word for 2nd digit OTHER_TENS
			count = 2
			result.append(getWordNum(count, secondSingleDig, otherTenArray))
			print(result)
		else:
			count = 2
			result.append(getWordNum(count, secondSingleDig, otherTenArray))
			count = 1
			result.append(getWordNum(count, thirdDig, firstTenArray))
			print(result)
	elif numStrLength == 2:
		firstDig = int(numStr[0])
		secondDig = int(numStr[0] + numStr[1])
		thirdDig = int(numStr[1])
		if numStr[0] == "1":
			count = 10
			result.append(getWordNum(count, secondDig, secondTenArray))
			print(result)
		elif numStr[0] > "1" and numStr[1] == "0":
			count = 2
			result.append(getWordNum(count, firstDig, otherTenArray))
			print(result)
		else:
			count = 2
			result.append(getWordNum(count, firstDig, otherTenArray))
			count = 1
			result.append(getWordNum(count, thirdDig, firstTenArray))
			print(result)
	else:
		firstDig = int(numStr[0])
		count = 1
		result.append(getWordNum(count, firstDig, firstTenArray))
		print(result)
	
	#join result values with spaces in between
	print(' '.join(result))

#getWordNum function
def getWordNum(count, numDig, numArray):
	for num in numArray:
		if count == numDig:
			return num
		else:
			count+=1
		
checkio(4)
checkio(133)
checkio(12)
checkio(101)
checkio(212)
checkio(40)
checkio(212 )
#checkio(12)


# if __name__ == '__main__':
    # #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert checkio(4) == 'four', "1st example"
    # assert checkio(133) == 'one hundred thirty three', "2nd example"
    # assert checkio(12) == 'twelve', "3rd example"
    # assert checkio(101) == 'one hundred one', "4th example"
    # assert checkio(212) == 'two hundred twelve', "5th example"
    # assert checkio(40) == 'forty', "6th example"
    # assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"