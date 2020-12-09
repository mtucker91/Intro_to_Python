# FIXME 1: Complete this function. It takes in a list and returns a dictionary,
# where the key is a word and the value the word-frequency
def word_frequency(passed_list):
    word_freq_dict = {}
    for item in passed_list:
        word_freq_dict[item] = int(passed_list.count(item))
    return word_freq_dict
# FIXME 2: This function takes in a dictionary and prints a table of the words and their frequencies
def print_dict(dict_list):
    dash = '-' * 22
    # Go back to PA 6 (celsius_to_fahrenheit_table) to see the table format
    # Hint: '{:<9s}{:>s} {:>d}'
    
    print('Word     |   frequency')
    print(dash)
    for item in dict_list:
        print('{:<9s}{:>s} {:>d}'.format(item, '|', dict_list[item]))  # Print the result and align numbers
    

if __name__ == "__main__":
    # FIXME 3a: Print the name of the program. (Word Frequencies)
    print('Word Frequencies')
    # FIXME 3b: Prompt the user to to input a sentence. Then put it in a list
    input_list = str(input('Enter a sentence:\n'))
    #input_list = 'This is my test sentence for my moment is This This moment'
    entered_list = [str(item) for item in input_list.split()]
    
    # FIXME 3c: Call the function word_frequency with the list made from the sentence
    created_dict = word_frequency(entered_list)
    
    # FIXME 3d: call print_dict with the dictionary returned from the above step
    print_dict(created_dict)
    
    