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

# print(selectionSort([5,3,6,2,10]))


############################################

# Better Space Complexity
A = [64,25,12,22,11]

for i in range(len(A)):
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    
    A[i] , A[min_idx] = A[min_idx], A[i]

print("Sorted array")

for i in range(len(A)):
    print(int(A[i]), end= ", " if i!= len(A)-1 else "")