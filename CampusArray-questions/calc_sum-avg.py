def calculate_sum_average(arr):
    total = 0
    for num in arr:
        total += num
        avg=total / len(arr)
    
    return total, avg

# Input
n = int(input("Enter the number of elements: "))

arr = list(map(int, input("Enter the elements: ").split()))

total, avg = calculate_sum_average(arr)

print("Total: ",total,"and","Average: ", avg)