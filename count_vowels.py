#count the number of vowels in a string
def vowels(s):
    count=0
    for ch in s.lower():
        if ch in "aeiou":
            count+=1
    return count
print(vowels("programming"))
