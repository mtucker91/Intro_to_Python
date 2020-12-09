# Write a Python program (calculator.py) that makes a simple calculator. 
# The program should add, subtract, multiply and divide numbers using functions.

# Your program should contain five functions:

# (1) add(x, y): This function takes in x and y (both integers) as parameters, and 
# returns the result of x + y. (Submit for 1 point)

# (2) subtract(x, y): This function takes in x and y (both integers) as parameters, 
# and returns the result of x - y. (Submit for 1 point)

# (3) multiply(x, y): This function takes in x and y (both integers) as parameters, 
# and returns the result of x * y. (Submit for 1 point)

# (4) divide(x, y): This function takes in x and y (both integers) as parameters, 
# and returns the result of x / y. (Submit for 1 point)

# (5) __main__: In the main, you do the following: (Submit for 6 points)

# a. Print the list of operations in a menu format:

# Select operation.
# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Divide
# b. Prompt the user to input a choice (1, 2, 3, or 4). If the user input invalid 
# choice, the program should print Invalid input.

# Enter choice(1, 2, 3, or 4):
# 4
# c. Prompt the user to input two numbers.

# Enter first number:
# 5
# Enter second number:
# 2
# d. Call the function that matchs the user choice to do the calculations, then 
# display it as follow:

# FIXME 1: This function add two numbers
def add(x, y):
   return x + y
# FIXME 2: This function subtracts two numbers
def subtract(x, y):
   return x - y

# FIXME 3: This function multiplies two numbers
def multiply(x, y):
    return x * y

# FIXME 4: This function divides two numbers
def divide(x, y):
    return x / y
if __name__ == "__main__":
    # FIXME 5 a: Print the list of operations
    print('Select operation.\n1.Add\n2.Subtract\n3.Multiply\n4.Divide')

    # FIXME 5 b: Prompt the user to input a choice
    oper_choice = int(input('Enter choice (1,2,3, or 4):\n'))

    # FIXME 5 c: Prompt the user to input two numbers
    num1 = int(input('Enter first number:\n'))
    num2 = int(input('Enter second number:\n'))

    # FIXME 5 d: Call the function. if-elif-else
    if oper_choice == 1:
        answer = add(num1, num2)
        print(f'{num1} + {num2} = {answer}')
    elif oper_choice == 2:
        answer = subtract(num1, num2)
        print(f'{num1} - {num2} = {answer}')
    elif oper_choice == 3:
        answer = multiply(num1, num2)
        print(f'{num1} * {num2} = {answer}')
    elif oper_choice == 4:
        answer = divide(num1, num2)
        print(f'{num1} / {num2} = {answer}')
    else:
        print('Invalid input')