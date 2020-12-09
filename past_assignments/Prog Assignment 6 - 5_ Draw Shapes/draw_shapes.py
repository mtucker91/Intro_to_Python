# FIXME 1: complete the function draw_triangle. No return, just prints.
def draw_triangle(num):
    loopi = 0
    while loopi != num:
        i = 0
        while i != loopi + 1:
            print('*', end='')
            i += 1
            if i == loopi + 1:
                print('')
        loopi += 1

# FIXME 2: complete the function draw_square. No return, just prints.
def draw_square(num):
    loopi = 0
    while loopi != num:
        i = 0
        while i != num:
            print('*', end='')
            i += 1
            if i == num:
                print('')
        loopi += 1

if __name__ == "__main__":
    # FIXME 3: prompt the user to input a positive int (> 0)
    # Reprompts until the user enters a positive integer. use While loop
    sizeinput = 0
    attempt = 0
    while sizeinput <= 0:
        if attempt == 0:
            sizeinput = int(input('Input a positive integer (greater than 0):\n'))
        else:
            sizeinput = int(input('Try again (Note: greater than 0):\n'))
        attempt += 1
    
    entry = False
    while entry != True:
        shapeinput = input("Choose which shape: 'triangle', 'square', or 'all':\n")
        if shapeinput == "triangle":
            draw_triangle(sizeinput)
            entry = True
        elif shapeinput == "square":
            draw_square(sizeinput)
            entry = True
        elif shapeinput == "all":
            draw_square(sizeinput)
            print('')
            draw_triangle(sizeinput)
            entry = True
        else:
            entry = False

    # Prompt the user to choose which shape: “triangle”, “square”, or "all"
    # Reprompts until the user enters a valid choice. use While loop.
    
    # Call the function based on the choice. use If-elif-else