# Input
while True: # A loop that will run until it gets desired inputs from end users
    user_op = str(input('{"a"} -> Addition\n{"s"} -> Subtraction\n{"m"} -> Multiplication\n{"di"} -> Division\nPlease select operation of your choice: ')).lower() # For displaying operation choices
    if user_op not in ["a", "s", "m", "di"]:
        print("Please only enter characters from the selection.") # Handling error committed by entering characters that are not included on the choices
        continue
    while True:
        try:
            user_num = str(input("Enter any two numbers of your choice separated by space: "))
            user_nums = list(map(lambda x: int(float(x)) if float(x)%1 == 0 else float(x), user_num.split(" "))) # Separate user input into two numbers with either float or int data type according if they have decimal values or not
            if len(user_nums) != 2:
                print("Please only enter two numbers.") # Handling error committed by not entering two numbers
                continue
        except ValueError:
            print("Please only enter numerical values") # Handling error committed by entering non-numerical values
            continue
        break
    # Process
    # Holds the processes to be executed according to the key provided by the user
    operations = {
        "a" : lambda x,y: x + y,
        "m" : lambda x,y: x * y,
        "di" :lambda x,y: x / y ,
        "s" : lambda x,y: x - y, 
    }
    # Holds the name of the processes to be displayed in the output
    operation_text = {
        "a" : "sum",
        "m" : "product",
        "di" : "quotient",
        "s" : "difference", 
    }
    # Holds the result value of the numbers and operation chosen by the user
    try:
        result = f"{operations[user_op](user_nums[0],user_nums[1]):.2f}"
    except ZeroDivisionError: # Handling error committed by dividing numbers with 0
        result = "undefined"

    # Output
    print(f"The {operation_text[user_op]} of {user_nums[0]} and {user_nums[1]} is {result} .")

    # Loop Input
    user_loop = input("Enter any key to continue, enter 'no' if otherwise: ").lower()
    if user_loop == "no":
        print("Terminating Program...")
        break