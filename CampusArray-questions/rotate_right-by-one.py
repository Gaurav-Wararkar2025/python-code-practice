def rotate_right_by_one(arr):
    n = len(arr)
    last = arr[n - 1]

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = last


n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))

rotate_right_by_one(arr)
print(*arr)