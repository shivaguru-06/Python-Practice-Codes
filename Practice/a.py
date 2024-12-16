a=int(input())
b=int(input())
arr=list(map(int,input().split()))
mx=-1
for i in range(0,len(arr)-b-1):
    temp=arr[i: i+b]
    k,s=1,0
    for j in temp:
        s+=(j*k)
        k+=1
        if(s>mx):
            mx=s
print(mx)  

