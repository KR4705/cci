#to check if given string is a permutation of 
#a palindrome(ex: madam)
#given that the question is not case sensitive we have to count A as a
#or viceversa

from sys import argv
script,string = argv

#mapping characters to values.
string = string.upper() #small cheat for faster code gen assuming O(n)

#ord value of A = 65
counter = []
for i in range(26):
	counter.append(0)

A = 65

for each in string:
	counter[ord(each) - A] += 1
# check if only one of them is odd
def onlyOneOdd(array):
	middle = 0
	for each in array:
		if each % 2 == 0:
			pass
		elif middle == 1:
			print "false"
			return 
		else:
			middle += 1
	print "true palindrome permutaion"
	return

onlyOneOdd(counter)







