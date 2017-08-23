# to check a string has no unique characters.
# assuming ASCII
from sys import argv

file_name,string = argv
print string

def is_unique(string):
	char = [False]*128
	for each in string:
		val = ord(each)
		if char[val]:
			return False
		char[val] = True
	return True

print is_unique(string)


