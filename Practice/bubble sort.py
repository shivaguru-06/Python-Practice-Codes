def bubble_sort(nums):
    for i in range(len(nums)):
        sorting=False
       
        for j in range(0,len(nums)-i-1):
            
            
            if(nums[j]>nums[j+1]):
                s=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=s
                sorting=True
        if(sorting==False):
            break
nums=[5,7,3,6,9]
bubble_sort(nums)   
for i in range (len(nums)):
    print(nums[i],end=" ")        

