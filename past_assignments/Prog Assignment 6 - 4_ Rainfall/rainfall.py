# FIXME 1: Complete the rainfall function. Use nested loops.
def rainfall(year):
    y = 1
    m = 0
    i = 0
    #rainfalls = []
    rainfalls = 0
    while y <= year:
        print('For year', y, ':')
        while m < 12:
            #rainfalls.append(float(input('Enter the rainfall amount for the month ' + str(i + 1) + ' in inches:\n')))
            rainfall_input = float(input('Enter the rainfall amount for the month ' + str(i + 1) + ' in inches:\n'))
            m += 1
            i += 1
            rainfalls += rainfall_input
        m = 0
        y += 1
    return rainfalls, i

if __name__ == "__main__":
    averageRainfall = 0.0
    totalRainfall = 0.0     # Holds the total rainfall for all months
    totalMonths = 0         # Holds the total number of months
    # FIXME 2-a: Prompt the user to input the number of years
    # years must be >0
    years = int(input('Enter the number of years (Greater than 0):\n'))
    # FIXME 2-b: Call rainfall function
    outputs = rainfall(years)
    #rainfalls = rainfall(years)
    # FIXME 2-c: Calculate the average
    totalRainfall = outputs[0]
    totalMonths = outputs[1]
    averageRainfall = totalRainfall / totalMonths
    # for inches in rainfalls:
    #     totalRainfall += inches
    #     totalMonths += 1
    #     averageRainfall = totalRainfall / totalMonths
    # FIXME 2-d: Display the number of months, the total inches of rainfall,
    # and the average rainfall per month for the entire period.
    print('For', totalMonths, 'months')
    print('Total rainfall:', totalRainfall, 'inches')
    print('Average monthly rainfall:', averageRainfall, 'inches')