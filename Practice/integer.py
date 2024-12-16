#factorial
'''def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
n=5
result=fact(n)         
print(result)   
'''

#recursion
import sys
sys.setrecursionlimit(20)
sys.getrecursionlimit()
i=0
def great():
    global i
    i+=1
    print("Have a nice day",i)
    great()
great()    


#factorial usind recursion
'''def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)
v=5
o=fact(v)
print(o)    
'''    