def linearSearch(l,s):
    for i in l:
        if i==s:
            return l.index(i) 
    if s not in l:
        return False
print(linearSearch([5,6,2,7],0))