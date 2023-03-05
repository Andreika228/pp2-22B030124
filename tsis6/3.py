def isPalindrome(n):
	left = 0
	right = len(n) - 1
	
	while right >= left:
		if not n[left] == n[right]:
			return False
		left += 1
		right -= 1
	return True
n=input()
print(isPalindrome(n)) 