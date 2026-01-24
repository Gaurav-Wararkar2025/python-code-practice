#Reverse an Array In-Place

arr = [1, 2, 3, 4, 5]

left, right = 0, len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)

"""

Method 1: Using a Temporary Array
arr = [1, 2, 3, 4]
arr.reverse()
print(arr)

Method 3: Using Slicing
arr = [1, 2, 3, 4]
print(arr[::-1])

"""