def insertionSort(arr):
    n = len(arr)

    if n <= 1:
        return 
    for i in range (1, n):
        key = arr[i]
        j = i-1 
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

A = [15, 36, 78, 9, 1, 0]
B = [25, 26, 47, 26, 45, 26]
insertionSort(A)
insertionSort(B)
print("Using Insertion Sort: ")
print(f"Sorted array (Set A): {A}")
print(f"Sorted array (Set B): {B}")