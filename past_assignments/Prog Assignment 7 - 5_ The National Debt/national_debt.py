# Write a Python program (national_debt.py) that tries to help us understand 
# this big number.

# Your program will prompt for two numbers:

# (1) The size of the national debt in dollars. It is a number that is hard to track, 
# but there are various web sites that are only too happy to give you a number. 
# Try http://www.usdebtclock.org.

# (2) The denomination of U.S. currency bills you want to use. You can go up to $100, 
# common U.S. bill (see http://en.wikipedia.org/wiki/LargedenominationsofUnitedStates_currency)

# You program will print out two numbers:

# (1) The height in miles of your chosen bill denomination required to equal the 
# debt number that was input.

# (2) The calculated distance in miles translated to a multiple of the average 
# distance to the Earth's moon.

# Some useful facts:

# • The thickness of every U.S. denomination bill is 0.0043 inches.

# • The average distance to the moon is 239,228 miles. 
# (http://en.wikipedia.org/wiki/Lunardistance(astronomy))

# • One mile has 63360 inches.

# Your program should contain three functions:

# (1) height_mile(debt, denomination): This function takes two parameters, debt 
# and denomination. Then calculates and returns the height in miles. (Submit for 2 points)

# (2) distance_to_moon(miles): This function takes one parameter, miles. Then 
# calculates and returns distance in miles translated to a multiple of the average 
# distance to the Earth's moon. The miles this function takes is the value returned 
# by height_mile(debt, denomination) function. (Submit for 2 points)

# (3) __main__: In the main, you do the following: (Submit for 6 points)

# a. When you start the program, print How big is the national debt?

# b. Prompt the user to input the the national debt. As I am making this program, 
# the current national debt is 22,114,394,554,000

# c. Prompt the user to input the denomination of currency, ($1, $5, $10, $20, $50, $100).

# d. Call the above functions to find the results.

# 'e.' Print the output.
#import urllib.request
#debt = int(str(urllib.request.urlopen('https://www.pgpf.org/national-debt-clock').read()[20878:20896]).replace(',', '')[2:-1])
#print(debt)
# thickness and to_moon are global variables that you need in your function
thickness = 0.0043
to_moon = 239228
# FIXME 1: Complete the height_mile function. No print.
def height_mile(debt, denomination):
    tot_height = (((debt / denomination) * thickness) / 63360) 
    return tot_height
# FIXME 2: Complete the distance_to_moon function. No print.
def distance_to_moon(miles):
    return miles / to_moon

if __name__ == "__main__":
    # FIXME 3a: print a statement that says 'How big is the national debt?'
    print('How big is the national debt?')
    # FIXME 3b: Prompt the user to input the national debt
    nd = int(input('National Debt: '))
    # FIXME 3c: Prompt the user to input the denomination of currency
    denom = int(input('Input the denomination of currency: '))
    # FIXME 3d: Call the functions
    #miles = height_mile(debt, denom)
    miles = height_mile(nd, denom)
    dtm = distance_to_moon(miles)
    # FIXME 3e: Print the results
    print(f'height in miles = {miles}\ndistance to moon = {dtm}')
    