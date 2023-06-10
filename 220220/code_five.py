# fcheck for palindrome

def isPalindrome(s):
	return (s == s[::-1])

s=input("Enter a string")
ans = isPalindrome(s)

if ans:
	print("Yes, the string is a palindrome")
else:
	print("No, the string is not a palindrome")

