def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array [j+1]
                array[j+1] = temp
    
    return array

A = [15, 36, 78, 9, 1, 0]
B = [25, 26, 47, 26, 45, 26]

set_a = bubbleSort(A)
set_b = bubbleSort(B)

print("Using Bubble Sort: ")
print(f"Sorted array (Set A): {set_a}")
print(f"Sorted array (Set B): {set_b}")