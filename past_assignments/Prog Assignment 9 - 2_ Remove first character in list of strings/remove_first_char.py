# FIXME 1: This function takes in a list, and returns a new list with the first char is removed from each item.
def remove_first(old_list):
    i = 0
    changed_list = old_list
    for word in old_list:
        slice_object = slice(1, len(word))
        rest_of_word = word[slice_object]
        changed_list[i] = rest_of_word
        i += 1
    return changed_list

if __name__ == "__main__":
    # FIXME 2a: Print a statement that says the program's name "Remove first character in list of strings"
    print('Remove first character in list of strings')
    # FIXME 2b: Use the list in this program. You may change it here for more testing
    #test_list = ["#apple", "#banana", "#cherry"]
    test_list = ['$25.0', '$13.75', '$10.95', '$4.99']
    # FIXME 2c: printing original list
    print(f'The original list: {test_list}')
    
    # FIXME 2d: Call the function remove_first, then print the list after removing first char
    new_list = remove_first(test_list)
    print(f'The list after removing first characters: {new_list}')