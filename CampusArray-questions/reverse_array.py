#Reverse an Array In-Place

arr = [6, 2, 3, 4, 5]

left, right = 0, len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)

"""

Method 2: Using a Temporary Array
arr = [1, 2, 3, 4]
arr.reverse()
print(arr)

Method 3: Using Slicing
arr = [1, 2, 3, 4]
print(arr[::-1])

Method 4: Using another array
arr=[4,5,6,7,8,9]
arr2=(arr[-1:0:-1])
print(arr2)


#Method 5: Using Recursion

def reverse_array_recursive(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse_array_recursive(arr, left + 1, right - 1)

"""