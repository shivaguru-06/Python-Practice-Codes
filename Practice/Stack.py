#subarray problems
'''arr=[1,4,20,3,10,5]
sum=0
list1=[]
a=[]
for i in range(len(a)):
    for j in range(len(arr)):
        if j+1<len(arr):
            a.append(arr[j+1:len(a)])
            b=arr[i]+sum(a)
            if b==33:
                list1.append(j+1)
print(list1)    
'''
'''arr = [1, 4, 20, 3, 10, 5]
target_sum = 33
list1 = []

for i in range(len(arr)):
    current_sum = 0
    for j in range(i, len(arr)):
        current_sum += arr[j]
        if current_sum == target_sum:
            list1.append(arr[i:j+1])  # Append the subarray that sums to 33
            break  # Stop once we find the subarray

print(list1)
'''
arr = [1, 4, 20, 3, 10, 5]
target_sum = 33
indices = []

for i in range(len(arr)):
    for k in range(i, len(arr)):  
        current_sum = 0
        current_indices = []  
        for j in range(i, len(arr)):
            if j != k:  
                current_sum += arr[j]
                current_indices.append(j)  
            if current_sum == target_sum:
                indices.append(tuple(current_indices))  
                break  

print(indices)



            
                        
            
    
            
            