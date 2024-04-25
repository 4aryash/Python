def isPalindrome(s):
	lp = 0
	rp = len(s) - 1
	s= s.lower()


	while lp < rp:

		while s[lp].isalnum() == False:
			lp += 1

		while s[rp].isalnum() == False:
			rp -= 1

		if s[lp] == s[rp]:
			lp += 1
			rp -=1
		
		else:
			return False



	return True

flag = isPalindrome("ace car")
print(flag)
