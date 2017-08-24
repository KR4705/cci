def is_permutation(a,b):
	char = [0]*128
	for each in a:
		char[ord(each)] += 1
	for each in b:
		char[ord(each)] -= 1
	for each in char:
		if not each == 0:
			return False
	return True

# it is of the O(len(a)+len(b))
