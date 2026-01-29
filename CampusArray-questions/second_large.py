arr = [10, 20, 75,4, 45, 99]
arr = list(set(arr))
arr.sort()
print("Array is:",arr)
print("Second largest element is: ",arr[-2])


"""
#Method 2 without sorting

def second_largest(arr):
    first = second = 0
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
            
    return second

arr = [10, 20, 4,75, 45, 99]
print("Second largest element is:", second_largest(arr))


#Method 3 using max() function

arr = [10, 20, 4,75, 45, 99]
arr.remove(max(arr))
print("Second largest element is:", max(arr))

"""