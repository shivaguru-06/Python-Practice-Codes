#Selection sort
def sort(nums):
    for i in range(len(nums)):
        minpos=i
       
        for j in range(i,len(nums)):
            
            
            if(nums[j]<nums[minpos]):
                minpos=j
            temp=nums[i]
            nums[i]=nums[minpos]
            nums[minpos]=temp
            print(i,":",nums)
nums=[5,2,6,9,7,3]
sort(nums)
print(nums)   

