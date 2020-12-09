# FIXME: Define the c_to_f function. It should take the degree in Celsius and return the degree in Fahrenheit
def c_to_f(celsius):
    fahrenheit = (celsius * 1.8) + 32 #complete the calculation
    return fahrenheit #return the result of the calculation

# ****************** START RUNNING SCRIPT HERE ********************
if __name__ == "__main__":
    dash = '-' * 20  # to be used in the table format
    print('This program converts the temperature in Celsius to Fahrenheit')
    start_celsius = int(input('Enter start:\n'))
    end_celsius = int(input('Enter end:\n'))
    increments_celsius = int(input('Enter the degree increments:\n'))
    count_celsius = start_celsius
    print('Celsius | Fahrenheit')       # To print the headers
    print(dash)                         # To print dash under the headers

    for celsius in range(start_celsius, end_celsius +1, increments_celsius):
        fahrenheit = c_to_f(celsius) # complete the calculation for fahrenheit through the function
        print('') # print a blank line to stay with formatting in listed example output.
        print('{:<8d}{:>s} {:>3.1f}'.format(celsius, '|', fahrenheit))  # Print the result and align numbers
    # while count_celsius <= end_celsius: # while the incremented celsius does not reach the end celsius requested
        # fahrenheit = c_to_f(count_celsius) # complete the calculation for fahrenheit through the function
        # print('') # print a blank line to stay with formatting in listed example output.
        # print('{:<8d}{:>s} {:>3.1f}'.format(count_celsius, '|', fahrenheit))  # Print the result and align numbers
        
    #     count_celsius += increments_celsius # complete the incrementing
    print(dash)                         # To print dash at the end outside the loop