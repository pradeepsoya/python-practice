#validparanthesis leetcode
def valid(s):
    sta=[]
    dict={'[':']','(':')','{':'}'}
    if len(s)%2!=0:
        return "Invalid"
    for i in s:
        if i in ['[','(','{']:
            sta.append(i)
        else:
            if sta==[]:
                return False
        a=sta.pop()
        if i!=dict[a]:
            return False
    return sta==[]
print(valid("{]("))