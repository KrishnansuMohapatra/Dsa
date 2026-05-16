def checkPalindrome(s):

    s=s.lower()
    rev=""
    for ch in s:
        rev=ch+rev
    if rev==s:
        return True
    return False
input_str=input()
print(checkPalindrome(input_str))




