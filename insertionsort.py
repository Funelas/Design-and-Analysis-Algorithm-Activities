def insertionSort(arr):
    n = len(arr)

    if n <= 1:
        return 
    
    for i in range (1, n):
        key = arr[1]
        j = i-1 
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(f"Iteration {i}: {arr}")

arr = [-5, 36, 25, 2, -10]
insertionSort(arr)
print(arr)