# FIXME : Complete the program. No need for defining new functions
#  setup variables for counters among other things
num_count = 0
sum_count = 0
avg_count = 0
max_num = 0
min_num = 0

print('Simple Statistics')
numbs = str(input('Please enter numbers, separated by a space:\n'))
my_numbs = [float(numb) for numb in numbs.split()]
sum_count = sum(my_numbs)
my_numbs.sort()
max_num = my_numbs[-1]
min_num = my_numbs[0]
num_count = len(my_numbs)
avg_count = sum_count / num_count

print(f'The number of entered numbers is: {num_count}')
print(f'The Sum of the numbers is: {sum_count}')
print(f'The Average is: {avg_count}')
print(f'The Maximum number is: {max_num}')
print(f'The Minimum number is: {min_num}')