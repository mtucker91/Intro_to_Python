# FIXME 1: Complete the residential function. no print. return charge, usage
def residential(begin, end):
    usage = end - begin
    charge = (usage * 0.0005) + 5
    return charge, usage
# FIXME 2: Complete the commercial function. no print. return charge, usage
def commercial(begin, end):
    usage = end - begin
    charge = (usage * 0.00025) + 1000
    return charge, usage

# FIXME 3: All print statements, no return
def print_info(code, begin, end, charge, usage):
    print('The customer\'s code:', code)
    print('The customer\'s beginning meter reading:', begin)
    print('The customer\'s ending meter reading:', end)
    print('The gallons of water used by the customer:', usage)
    print('The amount of money billed to the customer: $', charge)
    pass

if __name__ == "__main__":
    # FIXME 4a: Print 'Utility Company'
    print("Utility Company")
    # FIXME 4b:  Prompt the user to input the customer code
    custcode = input("Enter the customer code ('r': Residential, 'c': Commercial, or 'q' to quit)\n")
    # FIXME 4c: Make sure the program runs while the code is not q.
    while (custcode != 'q'):
        # FIXME 4d:  Prompt the user to input meter readings.
        begmeter = int(input("Enter the customer's beginning meter reading:\n"))
        endmeter = int(input("Enter the customer's ending meter reading:\n"))
        # FIXME 4e: Call the either function to calculate the charges and usage
        if custcode.lower() == 'r':
            retvalues = residential(begmeter, endmeter)
        elif custcode.lower() == 'c':
            retvalues = commercial(begmeter, endmeter)
        else:
            print('Invalid Input')
            

        # FIXME 4f: And Call print_info function
        print_info(custcode, begmeter, endmeter, retvalues[0], retvalues[1])
        
        custcode = input("Enter the customer code ('r': Residential, 'c': Commercial, or 'q' to quit)\n")
    else:
        # FIXME: at the end, print 'Thank you for using the program'
        print('Thank you for using the program')