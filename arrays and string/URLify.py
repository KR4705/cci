# to replace all spaces in given truelength of string to %20

def url(string,truelength):
	# counting the length after urlifying
	# truelength - spaces + 3*spaces
	length = truelength
	for i in range(truelength):
		if string[i] == ' ':
			length += 2

	for i in range(truelength-1,-1,-1):
		answer = [None]*length
		if string[i] == ' ':
			answer[length - 1] = '0'
			answer[length - 2] = '2'
			answer[length - 3] = '%'
			length -= 3
		else:
			answer[length - 1] = string[i]
			length -= 1
	return answer

print url('Mr John Smith    ',13)



