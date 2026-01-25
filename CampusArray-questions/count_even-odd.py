def count_even_odd(arr):
    
    even = 0
    odd = 0
    
    for num in arr:
        if num % 2 == 0:
            even += 1 
        else: 
            odd += 1 
    return even, odd

# Input

n = int(input("Enter the number of elements: ")) 
arr = list(map(int, input("Enter the elements: ").split()))

even, odd = count_even_odd(arr) 
print("Even: ",even, "Odd: ",odd)

"""
arr = [1, 2, 3, 4, 5]
even = odd = 0

for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("The even numbers are:",even,end="\n")
print("The odd numbers are:",odd)

"""