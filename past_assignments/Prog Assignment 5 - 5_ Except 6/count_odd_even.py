def create_list():
    the_list = []
    num_input = 0
    while (int(num_input) != -1):
        if(the_list == []):
            num_input = input('Input numbers or -1 to stop:\n')
        else:
            num_input = input('Input another numbers or -1 to stop:\n')
        
        if(int(num_input) != -1):
            the_list.append(int(num_input))
    
    print('The list entered is: ' + str(the_list))
    return the_list
    

def count_even(my_list):
    i = 0
    for x in my_list: 
        if(x % 2) == 0:
            i += 1

    print('Number of even numbers: ' + str(i))
    

def count_odd(my_list):
    i = 0
    for x in my_list: 
        if(x % 2) != 0:
            i += 1
    print('Number of odd numbers: ' + str(i))


if __name__ == "__main__":
    print('This program will count the number of odd and even numbers in a list')
    shitty_list = create_list()
    count_odd(shitty_list)
    count_even(shitty_list)