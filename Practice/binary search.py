#Binary search
lis=[4,5,7,12,45,99]
n=45
l=0
u=len(lis)-1
while l <=u:
    mid=(l+u)//2
    if(lis[mid]==n):
        print("Found at",mid+1)
        break
    elif lis[mid]<n:
        l=mid+1
    else:
        u=mid-1
  
              
   