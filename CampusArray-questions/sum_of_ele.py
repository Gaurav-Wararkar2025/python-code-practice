arr = [1, 2, 3, 4]
print("Sum of elements:", sum(arr))

#OR
sum = 0
average = 0
for i in range(len(arr)):
    sum+=arr[i]
    average=sum/len(arr)

print("Sum of elements:", sum)
print("Average of elements:", average)