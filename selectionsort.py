# def findSmallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index 

# def selectionSort(arr):
#     newArr = []
#     for i in range(len(arr)):
#         smallest = findSmallest(arr)
#         newArr.append(arr.pop(smallest))
#     return newArr 
# A = [15, 36, 78, 9, 1, 0]
# B = [25, 26, 47, 26, 45, 26]
# set_a = selectionSort(A)
# set_b = selectionSort(B)

# print("Using Selection Sort")
# print(f"Sorted array (Set A): {set_a}")
# print(f"Sorted array (Set B): {set_b}")


############################################

Better Space Complexity
A = [15, 36, 78, 9, 1, 0]
B = [25, 26, 47, 26, 45, 26]
def selection_sort(array):
    A = array
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        
        A[i] , A[min_idx] = A[min_idx], A[i]
    return A
   
set_a = selection_sort(A)
set_b = selection_sort(B)

print("Using Selection Sort")
print(f"Sorted array (Set A): {set_a}")
print(f"Sorted array (Set B): {set_b}")


# for i in range(len(A)):
#     print(int(A[i]), end= ", " if i!= len(A)-1 else "")