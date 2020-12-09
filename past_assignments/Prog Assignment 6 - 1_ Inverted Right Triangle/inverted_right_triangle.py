# Create a Python program that prompts the user for a number and then prints an inverted right triangle containing
# that many rows 

num_input = 0
while num_input <= 0:
    num_input = input('Please enter a number greater than 0\n')
    num_input = int(num_input)

loopi = num_input
while loopi != 0:
    i = loopi
    while i != 0:
        print(str(loopi), end='')
        i -= 1
        if i == 0:
            print('')
    loopi -= 1