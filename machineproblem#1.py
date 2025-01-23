# Input
while True: # A loop that will run until it gets desired inputs from end users
    user_input = str(input("Enter any two numbers of your choice separated by space: "))
    try:
        user_inputs = list(map(float, user_input.split(" "))) # Converts the string input into separate numbers that has a data type of float
    except ValueError: 
        print("Please only enter numerical values.") # Handling errors committed by entering non-numerical values
        continue
    if len(user_inputs) != 2:
        print("Please only enter 2 numbers") # Handling errors committed by not entering two numbers
        continue
    break

# Process
summation = user_inputs[0] + user_inputs[1]
difference = user_inputs[0] - user_inputs[1]
product = user_inputs[0] * user_inputs[1]
quotient = user_inputs[0] / user_inputs[1]

# Output
print(f"The sum of {user_inputs[0]} and {user_inputs[1]} is equal to {summation}.")
print(f"The difference of {user_inputs[0]} and {user_inputs[1]} is equal to {difference}.")
print(f"The product of {user_inputs[0]} and {user_inputs[1]} is equal to {product}.")
print(f"The quotient of {user_inputs[0]} and {user_inputs[1]} is equal to {quotient:.2f}.")