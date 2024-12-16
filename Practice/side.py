def move(nums):
    left=-1
    right=1
    count=0
    
    for i in range(0,a,2):
        if(i+1<len(nums)):
            if (nums[i]+nums[i+1]==0):
                count+=1
    return count
a=int(input())
nums=list(map(int,input().split()))
a=move(nums)
print(a)
            
            