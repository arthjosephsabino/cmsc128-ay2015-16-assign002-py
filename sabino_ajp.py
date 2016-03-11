def getHammingDistance(string1, string2):
	#for defensive programming purposes
		if(type(string1) != str or type(string2) != str):
			 return "Error string 1 or string 2 is not a string"
		#counter
		i =0
		#if length of strings are not equal it returns an error
		if(len(string1) != len(string2)):
			return "Error! Strings are not equal"

		else:
			#loops through the string and counts the number of inversions per character
			for index in range(len(string1)):
					if(string1[index] != string2[index]):
						i = i+1

		return i

def countSubstrPattern(string1, string2):
	#for defensive programming purposes
	if(type(string1) != str or type(string2) != str):
		 return "Error string 1 or string 2 is not a string"
	#counter
	counter = 0
	
	#loops through the string one index at a time and  splits according to the length of string2 checks if they are substrings of
	#string1
	for i in range(len(string1)):	
		if string1[i:i+len(string2)] == string2:
			counter = counter + 1

	return counter
def isValidString(string1,string2):
	#replaces all characters of string1 if it has the same character of string2 with "/"
	for str2 in string2:
		string1 = string1.replace(str2, "/")
	#loops through string1, if str2 contains a character that is not "/" it will set isStringValid = False otherwise True
	for str1 in string1:
		if str1 != "/":
			isStringValid = False
			break
		isStringValid = True;

	return isStringValid
def getSkew(string1, n):
	#number of G's
	numberOfGs = 0
	#number of C's
	numberOfCs = 0

	#loops through the string (up to length n) and checks if it contains "G" or "C" and increments a variable depending if it is "G" or "C"
	for index1 in range(n):
		if string1[index1] == "G":
			numberOfGs = numberOfGs + 1
		if string1[index1] == "C":
			numberOfCs = numberOfCs + 1
	
	return numberOfGs - numberOfCs

def getMaxSkewN(string1, n):
	#contains the list of skews
	listm = []

	#loops through the string and appends the skews with listm
	for i in range(1,n+1):
		listm.append(getSkew(string1,i))
	#checks the maximum skew
	return max(listm)
def getMinSkewN(string1, n):
	#contains the list of skews
	listm = []

	#loops through the string and appends the skews with listm
	for i in range(1,n+1):
		listm.append(getSkew(string1,i))
	#checks the minimum skew
	return min(listm)

#test cases
'''
print (getHammingDistance("AACCTT", "GGCCTT"))
print (getHammingDistance("TCGGA","AAAAG"))
print getHammingDistance("A","AG") 
print countSubstrPattern("AATATATAGG","GG")
print countSubstrPattern("AATATATAGG","ATA") 
print countSubstrPattern("AATATATAGG","ACTGACTGACTG") 
print isValidString("AAGGCTATGC","ACGT")
print isValidString("AAGGCTATGa","ACGT")
print isValidString("ACGT","ACGT") 
print isValidString("ACGT101","ACGT") 
print isValidString("091212345","0123456789") 
print getSkew("GGCCAC", 1)
print getSkew("GGCCAC", 2)
print getSkew("GGCCAC", 3)
print getSkew("GGCCAC", 4)
print getSkew("GGCCAC", 5)
print(getMaxSkewN("GGCCAC", 1))
print(getMaxSkewN("GGCCAC", 2))
print(getMaxSkewN("GGCCAC", 3))
print(getMaxSkewN("GGCCAC", 4))
print(getMaxSkewN("GGCCAC", 5))
print(getMinSkewN("GGCCAC", 1))
print(getMinSkewN("GGCCAC", 2))
print(getMinSkewN("GGCCAC", 3))
print(getMinSkewN("GGCCAC", 4))
print(getMinSkewN("GGCCAC", 5))
'''