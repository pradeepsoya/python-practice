#count the number of consonants in a string
def vowels(s):
    count=0
    for ch in s.lower():
        if ch not in "aeiou":
            count+=1
    return count
print(vowels("programming"))
