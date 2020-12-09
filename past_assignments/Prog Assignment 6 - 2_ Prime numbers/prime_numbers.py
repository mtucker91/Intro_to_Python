# FIXME 1: Complete the function prime_num. It should return True if num is a prime, otherwise, return False
# No print statement in this function.
def is_prime(num):
    num = int(num)
    # If given number is greater than 1 
    if num > 1: 
        # Iterate from 2 to n / 2  
        for i in range(2, num): 
            if (num % i) == 0: 
                prime = False
                break
        else: 
            prime = True
    else: 
        prime = False

    return prime

if __name__ == "__main__":
    num_input = 0
    # FIXME 2-a: print a statement that says what the program is going to do
    print('This program checks if a given number is a prime number')
    while int(num_input) >= 0:
        # FIXME 2-b: Prompt the user to input a number
        num_input = input('Please enter a positive number (or a negative number to exit):\n')
        # FIXME 2-c: while the number entered is positive, print if its a prime or not.
        # Here you need to call the function prime_num
        if int(num_input) > 0:
            check_prime = is_prime(num_input)
            if check_prime == False:
                print(num_input, 'is not a prime number')
            else:
                print(num_input, 'is a prime number')

    # FIXME 2-d: Print a final statement 'Done. Thanks for using the program!'
    print('Done. Thanks for using the program!')

