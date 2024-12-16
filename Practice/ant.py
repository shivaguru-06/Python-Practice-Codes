#Ant Rail
n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(n):
    if sum(arr[:i+1])==0:
        c+=1
print(c)        