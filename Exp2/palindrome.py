def reverse(s): 
    return s[::-1] 
def isPalindrome(s): 
	rev=reverse(s) 
	if(s==rev): 
		return True
	return False
s=input("Enter String: ")
r=s
s=s.lower()
s1=isPalindrome(s) 
if s1==1: 
    print(r," is palindrome") 
else: 
    print(r," is not palindrome") 