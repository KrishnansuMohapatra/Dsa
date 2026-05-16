def checkPalindrome(s):
    if s=="":
        return None
    s=s.lower()
    return s==s[::-1]
input_str=input()
print(checkPalindrome(input_str))