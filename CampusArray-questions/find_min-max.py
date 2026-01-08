def find_max_min(arr):
    max_val = arr[0]
    min_val = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
        if arr[i] < min_val:
            min_val = arr[i]

    return max_val, min_val


N = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))

max_val, min_val = find_max_min(arr)
print("max: ",max_val,"min: ", min_val)