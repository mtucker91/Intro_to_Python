# FIXME 1: Complete the print_box function. No return, just print. Think about what kind of loops you need to use.
def print_box(w, h):
    count = 0
    loopi = 0
    while loopi != h:
        i = 0
        while i != w:
            print('{:<3d}'.format(count), end=' ')
            count += 2
            i += 1
            if i == w:
                print('')
        loopi += 1

if __name__ == "__main__":
    width =0
    height = 0
    # FIXME 2-a: Prompt the user for the width, and make sure it is >0
    while width <= 0:
        width = int(input('Please enter a width greater than 0:\n'))

    # FIXME 2-b: Prompt the user for the height, and make sure it is >0
    while height <= 0:
        height = int(input('Please enter a height greater than 0:\n'))

    # FIXME 2-c: Call the print_box function
    print_box(width, height)