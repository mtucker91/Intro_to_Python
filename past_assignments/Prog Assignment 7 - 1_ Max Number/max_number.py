# Write a Python program (max_number.py) that finds the max number in a set of numbers. 
# The number of numbers the program can test is variable. Meaning, the program can tell 
# you the max number if you test 2 or n numbers.

# For example, if the numbers you are trying to find their max are 3, 4, and -5, 
# the program should print 4. Also, the max of these numbers 11, 3, 4, -5, 7, 5, and 9 is 11.

# Your program should contain two functions:

# (1) max_of_numb: This This function takes a variable number of parameters, all int, 
# and returns the max number. No print in this function. (Submit for 8 point)

# (2) __main__: In the main, you just need to call the function 2 times, one time with 
# the numbers (3, 4, -5), and the second time with the numbers (11, 3, 4, -5, 7, 5, 9) 
# and print the result. (Submit for 2 point)

# Note: This program will not prompt the user for any input, the numbers will be hard 
# coded in the main function. Test your program with numbers list it above.

# FIXME 1: Complete the max_of_numb function. Make sure you fix the header.
def max_of_numb(*argnum):
    for arg in argnum:
        try:
            prevarg
        except:
            prevarg = arg

        if prevarg <= arg:
            prevarg = arg
    return prevarg

if __name__ == "__main__":
    # FIXME 2: Call the function for the second time with (11, 3, 4, -5, 7, 5, 9)
    print(max_of_numb(3, 4, -5))
    print(max_of_numb(11, 3, 4, -5, 7, 5, 9))
