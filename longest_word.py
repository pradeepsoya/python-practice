def longest(s):
    li=s.split()
    long=0
    for word in li:
        if len(word)>long:
            long=len(word)
    return word
print(longest("I love python"))
