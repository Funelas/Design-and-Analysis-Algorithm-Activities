def binary_search(user_nums, search_number, base_index = 0, loop = 0): # A recursive function that will use BinarySearch Algorithm ( O(log n) )
    median = int((len(user_nums) -1) / 2) # A variable used for determining the median where we will divide the list
    loop += 1
    print(user_nums)
    if len(user_nums) == 0: # A condition that checks if the list contains no more number
        return 'not found', loop
    elif user_nums[median] > search_number: # Checks if the searchee number is less than the median of the list ( meaning the number is on the left side of divided list)
        return binary_search(user_nums[:median], search_number, base_index, loop) # Redo function on the left side of the list
    elif user_nums[median] < search_number: # Checks if the searchee number is greater than the median of the list ( meaning the number is on the right side of divided list)
        return binary_search(user_nums[median+1:], search_number, base_index + median + 1, loop) # Redo function on the right side of the list
    else:
        if len(user_nums) > 1: # If the searchee number is the median of the currently scanning list
            return f'found at index {base_index + median}', loop
        else: # The searchee number is the remaining number on the list
            return f'found at index {base_index}', loop

while True:
    try:
        user_nums = sorted(list(map(int,input("Enter twenty (20) numbers separated by spaces: ").strip().split())))
        print(user_nums)
        if len(user_nums) != 20: # To check if user inputted 20 numbers
            print(f"Please input exact number of 20 values only (you inputted {len(user_nums)}).")
            continue
        else:
            break
    except ValueError:
        print('Please enter numerical values only.')
        continue
while True:
    try:
        search_num = int(input("Enter the number you want to find in prior number list input: "))
        break
    except ValueError: # Error handling when user inputted an alphacharacter
        print("Please input a numerical value only.")
result , loop = binary_search(user_nums, search_num) # Stores value for the string and number of loop the binary search took
if result == "not found": # If number entered is not found at the list provided
    print(f"It took {loop} loop(s) yet {search_num} {result}.")
else: # If number entered is found at the list provided
    print(f"{search_num} is found!")
    print(f"It took {loop} loop(s) to find {search_num}")
    print(f'The number {search_num} is {result}.')
