def validPalindrome(s):
    left=0
    s=s.lower()
    right=len(s)-1
    while left<=right:
        if s[left].isalnum()==False:
            left+=1
            continue
        elif s[right].isalnum()==False:
            right-=1
            continue
        elif s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True
print(validPalindrome("race a car"))