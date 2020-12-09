# This part is to ask the user to input the list items.
# It works, don't change or delete.
# The way it works is not the scope of this question, we will cover it later
#commented this out for testing
#list_string = input('Enter list items (all int):\n')
list_string = "7 5 6 5 4 9"

my_list = [int(elem) for elem in list_string.split()]

#my_list = [7, 5, 6, 5, 4, 9]

print('The list entered is:')
print(my_list)


# FIXME: complete the program after this line
print('The even numbers in the list with their indexes:')
#

for index, x in enumerate(my_list): 
    if(x % 2) == 0:
        #print('my_list[%s]: %d' % (index, elem))
        print('my_list[' + str(index) + ']: ' + str(x))
        #print('my_list[' + index + ']: ' + x)
    
#placeholder
k = 1
for j in my_list:
    #adding to said placeholder
    k += 1
    print('the amount of indexes = ' + str(k))


i = 0

while(i < k): #compare i (iteration) to my placeholder k
    x = my_list[i]
    if(x % 2) == 0:
        print('my_list[' + str(i) + ']: ' + str(x))
        i += 1