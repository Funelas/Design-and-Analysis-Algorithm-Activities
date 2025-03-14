import timeit # Package for Calculating Average Time of Execution
def merge_sort(array): # Function for the Merge Sort Algorithm
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

def selection_sort(array): # Function for the Selection Sort Algorithm
    for i in range(len(array)):
        sml_index = i
        for j in range(i+1, len(array)):  
            if array[j] < array[sml_index]:  
                sml_index = j
        array[i], array[sml_index] = array[sml_index], array[i] 


def bubble_sort(array): # Function for the Bubble Sort Algorithm
    not_swapped = True
    for i in range(len(array)):
        for j in range(1, len(array) - i):
            if array[j] < array[j-1]:
                array[j],array[j-1] = array[j-1],array[j]
                not_swapped = False
        if not_swapped:
            break
            

def insertion_sort(array): # Function for the Insertion Sort Algorithm
    for i in range(1, len(array)):
        j = i-1
        key = array[i]
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key 

user_inputs = [] # The array of the user input arrays

# Input
while True: # A loop that runs to get user data until they don't want to anymore
    try:
        # A variable holder for the suffix of the number to improve quality of life of the user when knowing how many arrays of numbers have they inputted
        suffix = "st" if (len(user_inputs)%10)+1 == 1 and (len(user_inputs) < 10 or len(user_inputs)+1 > 20) else "nd" if (len(user_inputs)%10)+1 == 2 and (len(user_inputs) < 10 or len(user_inputs)+1 > 20) else "rd" if (len(user_inputs)%10)+1 == 3 and (len(user_inputs) < 10 or len(user_inputs)+1 > 20) else "th"
        # A variable that takes space-separated values, converts each values to int data type and stores them in a list/array
        user_input = list(map(int,(input(f"Please enter the values of the {len(user_inputs)+1}{suffix} list on the 2D array separated by spaces (enter 'no' to stop): ").split())))
        for num in user_input: # Error handling for numbers that are less than 0 and greater than 100
            if num < 0:
                print("Only enter positive integers.")
                break
            elif num > 100:
                print("Only enter an integer between 0 and 100")
                break
        else:
            user_inputs.append(user_input) # To add the array to the main array
    except ValueError:
        break

selection_copy = user_inputs.copy() # Main array copy to be used by selection sort
bubble_copy = user_inputs.copy()  # Main array copy to be used by bubble sort
insertion_copy = user_inputs.copy() # Main array copy to be used by insertion sort
merge_copy = user_inputs.copy() # Main array copy to be used by merge sort

# Process
for arr in insertion_copy: # Application of Insertion Sort Algorithm to each array inside a copy of the main array
    insertion_sort(arr)
insertionsort_timer = timeit.timeit(stmt='for arr in user_inputs: insertion_sort(arr)', setup="from __main__ import insertion_sort, user_inputs", number= 10) # A method used to get the average execution times that is based on the number of preferred executions / iterations 

for arr in selection_copy: # Application of Selection Sort Algorithm to each array inside a copy of the main array
    selection_sort(arr)
selectionsort_timer = timeit.timeit(stmt='for arr in user_inputs: selection_sort(arr)', setup="from __main__ import selection_sort, user_inputs", number= 10) # A method used to get the average execution times that is based on the number of preferred executions / iterations 

for arr in bubble_copy: # Application of Bubble Sort Algorithm to each array inside a copy of the main array
    bubble_sort(arr)
bubblesort_timer = timeit.timeit(stmt='for arr in user_inputs: bubble_sort(arr)', setup="from __main__ import bubble_sort, user_inputs", number= 10) # A method used to get the average execution times that is based on the number of preferred executions / iterations 


for arr in merge_copy: # Application of Merge Sort Algorithm to each array inside a copy of the main array
    merge_sort(arr)
mergesort_timer = timeit.timeit(stmt='for arr in user_inputs: merge_sort(arr)', setup="from __main__ import merge_sort, user_inputs", number= 10) # A method used to get the average execution times that is based on the number of preferred executions / iterations 

# Output
print(f"Sorted by Insertion Sort: {insertion_copy}")
print(f"Insertion Sort Average Timer: {insertionsort_timer}")
print(f"Sorted by Selection Sort: {selection_copy}")
print(f"Selection Sort Average Timer: {selectionsort_timer}")
print(f"Sorted by Bubble Sort: {bubble_copy}")
print(f"Bubble Sort Average Timer: {bubblesort_timer}")
print(f"Sorted by Merge Sort: {merge_copy}")
print(f"Merge Sort Average Timer: {mergesort_timer}")
