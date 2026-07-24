#string palindrome
def palindrome(s):
    temp=s
    result=""
    for i in range(len(s) - 1, -1, -1):
            result += s[i]
    if temp==result:
          return "Palindrome"
    else:
          return "Not palindrome"
print(palindrome("malayalam"))