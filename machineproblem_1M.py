import timeit
def merge_sort(array):
    if len(array) > 1:
        median = len(array) // 2
        left = array[:median]
        right = array[median:]
        

        merge_sort(left)
        merge_sort(right)
        
        left_index = 0
        right_index = 0
        main_index = 0
        
     
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]: 
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

def selection_sort(array):
    for i in range(len(array)):
        sml_index = i
        for j in range(i+1, len(array)):  # Fixed loop range here
            if array[j] < array[sml_index]:  # Compare with sml_index
                sml_index = j
        array[i], array[sml_index] = array[sml_index], array[i]  # Swap the smallest element

# Bubble Sort

# Insertion Sort
user_inputs = []


while True:
    try:
        suffix = "st" if (len(user_inputs)%10)+1 == 1 and (len(user_inputs) < 10 or len(user_inputs)+1 > 20) else "nd" if (len(user_inputs)%10)+1 == 2 and (len(user_inputs) < 10 or len(user_inputs)+1 > 20) else "rd" if (len(user_inputs)%10)+1 == 3 and (len(user_inputs) < 10 or len(user_inputs)+1 > 20) else "th"
        user_input = list(map(int,(input(f"Please enter the values of the {len(user_inputs)+1}{suffix} list on the 2D array separated by spaces (enter 'no' to stop): ").split())))
        for num in user_input:
            if num < 0:
                print("Only enter positive integers.")
                continue
        else:
            user_inputs.append(user_input)
            print(user_inputs)
    except ValueError:
        break


# for arr in user_inputs:
#     merge_sort(arr)

for arr in user_inputs:
    selection_sort(arr)

# mergesort_timer = timeit.timeit(stmt='for arr in user_inputs: merge_sort(arr)', setup="from __main__ import merge_sort, user_inputs", number= 10)
# print(mergesort_timer)
selectionsort_timer = timeit.timeit(stmt='for arr in user_inputs: selection_sort(arr)', setup="from __main__ import selection_sort, user_inputs", number= 10)
print(selectionsort_timer)