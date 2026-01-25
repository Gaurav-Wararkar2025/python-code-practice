#Sort an Array and Check if it is Sorted

arr= [1,8, 2, 5,6,3, 4]
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print("Sorted Array is:", arr)

#Check if it is Sorted

#Method 1

arr = [1, 2, 3, 4]

if arr == sorted(arr):
    print("Sorted")
else:
    print("Not Sorted")

#Method 2

arr = [1, 2, 3, 4]
is_sorted = True
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("Sorted")
else:
    print("Not Sorted")
