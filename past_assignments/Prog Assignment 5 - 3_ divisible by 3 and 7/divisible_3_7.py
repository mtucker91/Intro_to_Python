# FIXME 3-a: Complete the boo_function function. 
new_list = []
#my_list = [3, 5, 7, 12, 15, 16, 25, 36, 49, 60, 103, 220]
def boo_function(low, high):
    for i in range(int(low), int(high)+1):
            if i >= int(low) and i <= int(high):
                if i % 15 == 0:
                    new_list.append('Boo')
                elif i % 3 == 0 or i % 7 == 0:
                    new_list.append(i)
    return new_list
    
if __name__ == "__main__":
    # FIXME 1: Prompt the user to input the lower limit and the upper limit
    llimit = input('Please input lower limit:\n')
    hlimit = input('Please input higher limit:\n')
    
    # FIXME 2: Update your output
    print('The list of numbers between 10 and 100 that are divisible by 3 or 7 is: ')
    
    # FIXME 3-b: Call the boo_function and print the list
    print(boo_function(llimit, hlimit))