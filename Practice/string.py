def covst(s):
    result=[]
    for i,ch in enumerate(s):
        if ch.isupper() and i!=0:
            result.append(" ")
        result.append(ch.lower())
    return  ''.join(result)  
s=input()
ot=covst(s)
print(ot)    
