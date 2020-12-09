# FIXME 3-a: Complete the no_6 function.
def no_6(l,h):
    new_list = ""
    for x in range(int(l), int(h)):

        if (str(x).find('6') != -1):
            continue
        else:
            new_list = int(x)
            # if(new_list == ""):
            #     new_list = str(x)
            # else:
            #     new_list = new_list + ' ' + str(x)
    return new_list

if __name__ == "__main__":
    # FIXME 1: Print what the program is going to do.
    print('This program will print all numbers except the ones that have 6 in them')
    
    # FIXME 2: Prompt the user to input the lower limit and the upper limit
    llimit = input('Please input lower limit:\n')
    hlimit = input('Please input higher limit:\n')
    
    # FIXME 3-b: Call the no_6
    val = no_6(llimit,hlimit)
    print(val)