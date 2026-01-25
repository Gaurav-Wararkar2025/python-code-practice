"""Arrays in python:- 
Python does not have built-in support for arrays like some other languages,
but we can use lists to achieve similar functionality.

They store multiple values in a single variable.
"""

#Create an array
arr = [10, 20, 30, 40]
print(arr)

#Access elements
print(arr[0])  # First element
print(arr[-1]) # Last element

#Traverse an array
arr = [1, 2, 3, 4]

#using direct element
for i in arr:
    print(i)

#using index
for i in range(len(arr)):
    print(arr[i])


#Array Input from user
n = int(input("Enter size: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

print("The inputed array is:",arr)


#Insert an element

arr = [1, 2, 3]
arr.append(4)       # End

arr.extend([5, 6])  # Multiple elements
arr2 = [7, 8]
arr.extend(arr2)    # Another array

arr.insert(1, 10)    # At index
print(arr)


#Delete an element

arr = [10, 20, 30, 40, 50, 20, 60]
arr.remove(20)
print(arr)
arr.pop()
print(arr)
arr.pop(2)
print(arr)


#Update an element

arr = [5, 10, 15]
arr[1] = 50
print(arr)
arr[0] += 5
print(arr)


#Search an element

arr = [3, 6, 9, 12]
key = 9

if key in arr:
    print(f"Found at index {arr.index(key)}")
else:
    print("Not Found")


#Find maximum and minimum

arr = [12, 45, 7, 89]
print(f"The max element is {max(arr)}")
print(f"The mim element is {min(arr)}")
