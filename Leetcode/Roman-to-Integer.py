#incomplete code

def romantoInt(s: str):
	symbols = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

	point = 0
	temp = 0
	result = 0

	while True:

		# if 1st and 2nd chars are equal, then check the 3rd char. If all 3 equal, add them. Else add 1st and 2nd.
		if s[point] == s[point + 1]:

			# if 3 equal chars, shift pointer to 4th char.
			if s[point + 1] == s[point + 2]:
				temp = s[point] + s[point + 1] + s[point + 2]
				point += 3
				break

			# Else, if 2 equal, shift pointer to 3rd char
			else:
				temp = s[point] + s[point + 1]
				point += 2

		elif s[point] > s[point + 1]:
			temp = s[point]
			point += 1
			


romantoInt('MCMXCIV')
