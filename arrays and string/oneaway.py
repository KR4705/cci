
def is_one_away(s1,s2):
	if len(s1) == len(s2):
		return is_replace(s1,s2)
	elif len(s1) +1 == len(s2):
		return is_add(s2,s1)
	elif len(s2) +1 == len(s1):
		return is_add(s1,s2)
	else:
		return False

def is_replace(s1,s2):
	diff = 0
	for i in range(len(s1)):
		if s1[i] == s2[i]:
			continue
		elif diff == 0:
			diff += 1
		else:
			return False
	return True


def is_add(s1,s2):
	print s1,s2
	diff = 0
	i , j = 0 , 0
	for each in s2:
		if s1[i] == s2[j]:
			i , j = i+1 , j+1
		elif diff == 0 and s1[i] != s2[j]:
			i , j , diff = i+1 , j , diff +1 
		else:
			return False
#this arises because we are using the smaller string 
#if the left element is the different one then diff should be zero
#else it is false

	if diff == 0:
		return True
	else:
		return False

print is_one_away("abcdfgg","abcdfg")
	



