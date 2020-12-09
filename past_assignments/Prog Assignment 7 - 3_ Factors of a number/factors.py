# Write a Python program (factors.py) finds the factors of a given number.
#  A factor is a number that divides evenly into another number. As an example, 
# the factors of 20 are 1,2,4,5, and 10. Why? Because all of these numbers divide 
# evenly into 20 (Hint: 20 % 5 = 0).

# Your program should run, as long as the entered number is not 0. Assume the 
# numbers entered by the user are all positive.

# Your program should contain two functions:

# (1) print_factors(x): This function takes one parameter (an int), and prints 
# the factors of the number. This function does not have return statement. 
# (Submit for 5 points)

# (2) __main__: In the main, you do the following: (Submit for 5 points)

# a. When you start the program, print Find the factors of a number

# b. Prompt the user to input a number to find its factors.

# c. Make sure your program can run as long as the number entered is not equal to 0.

# d. Call print_factors with the number entered by the user.

# e. When the user wants to quit and enters 0, the program should print Done!.

# FIXME 1: Complete print_factors function. You need a loop to check every number 
# less than x if it's a factor, then print it. No return.
def print_factors(x):
    print(f'The factors of {x} are:')
    for i in range(1,x+1):
        if x % i == 0:
            print(i)

    #goes from 1 - number before end, then prints end number
    # for i in range(1,x):
    #     print(i)
    # print(x)


if __name__ == "__main__":
    pass
    # FIXME 2a: print Find the factors of a number
    print('Find the factors of a number')
    # FIXME 2b: Prompt the user to input a number to find its factors.
    fact_num = int(input('Enter a number to find its factors or 0 to quit:\n'))

    # FIXME 2c: Make sure your program can run as long as the number entered is not equal to 0.
    while fact_num != 0:
        # FIXME 2d: Call print_factors with the number entered by the user.
        print_factors(fact_num)
        fact_num = int(input('Enter another number to find its factors or 0 to quit:\n'))
        # FIXME 2e: print Done! when finished
    print('Done!')

