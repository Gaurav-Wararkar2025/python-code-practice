def move_zeros_to_end(arr):
    j = 0  # position for next non-zero element

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1


n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))

move_zeros_to_end(arr)
print(*arr)