
def print_frequency_of_elements(arr):
    visitied = [False]*len(arr)
    for i in range(len(arr)):
        if visitied[i] == True:
            continue
        count = 1
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                count += 1
                visitied[j] = True
        print(arr[i],":",count)


arr=list(map(int,input("Enter the elements of array: ").split()))
print_frequency_of_elements(arr)