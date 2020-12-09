# Write a Python program (min_word_length.py) that counts the number of words 
# in a sentence that has a minimum length. The sentence will be entered by the user, 
# as well as the minimum length.

# Your program should contain two functions:

# (1) min_len_count(word_list, length): This function takes in two parameters, a word_list 
# as a list of words and length as the minimum word length int. And returns the total number 
# of words in the list that has the length of length or greater. This function has no print 
# statement. (Submit for 6 point)

# (2) __main__: In the main, you do the following: (Submit for 4 point)

# a. Prompt the user to input a sentence then put it in a list. This part is provided in 
# the template file.

# b. Prompt the user to input the minimum length of the words that need to be counted.

# c. Call the function min_len_count with values entered by the user, and print the result.


# FIXME 1: Complete min_len_count function. It takes a list and an int. And returns the count (int)
def min_len_count(word_list, length):
    len_char_words = 0

    for words in word_list:
        if len(words) >= length:
            len_char_words += 1

    return len_char_words

if __name__ == "__main__":
    # 2a: NOTE: The code that reads the sentence and put the words in a list is already provided.
    # the way it works is beyond the scope of this lab.
    line = input('Enter a sentence:\n')
    my_list = [str(elem) for elem in line.split()]
    #print('The sentence entered in a list:\n', my_list)

    # FIXME 2b: Prompt the user for the min length of the words.
    len_char = int(input('Enter the minimum length:\n'))

    # FIXME 2c: Call the function min_len_count and print out the result.
    print('The number of words that has the minimum length of ' + str(len_char) + ' is ' + str(min_len_count(my_list, len_char)))