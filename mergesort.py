def merge_sort(array):
    if len(array) > 1:
        median = len(array) // 2
        left = array[:median]
        right = array[median:]
        left_index = 0
        right_index = 0
        main_index = 0
        merge_sort(left)
        merge_sort(right)
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                array[main_index] = left[left_index]
                left_index += 1
            else:
                array[main_index] = right[right_index]
                right_index += 1
            main_index += 1
        while left_index < len(left):
            array[main_index] = left[left_index]
            main_index += 1
            left_index += 1
        while right_index < len(right):
            array[main_index] = right[right_index]
            main_index += 1
            right_index += 1
    

A = [15, 36, 78, 9, 1, 0]
B = [25, 26, 47, 26, 45, 26]
merge_sort(A)
merge_sort(B)
print("Using Merge Sort: ")
print(f"Sorted array (Set A): {A}")
print(f"Sorted array (Set B): {B}")
