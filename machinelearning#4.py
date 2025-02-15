while True: # A loop for validating the twenty numbers that the user will input
    try:
        user_nums = list(map(int,input("Enter twenty (20) numbers separated by spaces: ").strip().split()))
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
        searchee_num = int(input("Enter the number you want to find on the entered numbers: ")) # The number that the user wants to find
    except:
        print("Please enter a numerica value only.")
        continue
    break


found_num = False # A condition used for handling print values




for i in range(len(user_nums)): # 'i' represents each number from 0 to 20
    if searchee_num == user_nums[i]:
        if found_num == False: # if number to be searched is not yet encountered in the list
            print(f"\n{searchee_num} is found!")
            found_num = True
        else: # if number is already encountered on the list
            print(f"\n{searchee_num} is found again!")
        print(f"It took {i+1} loops to find {searchee_num}.")
        print(f"{searchee_num} is found at index {i}.")
else:
    if not found_num: # If number to be searched is not encountered on the list
        print(f"It took {len(user_nums)} loops yet {searchee_num} is not found!")
