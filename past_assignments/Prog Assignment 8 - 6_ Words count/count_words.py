# FIXME 1: Complete the function word_count.
# Note: use methods such as split(), lower(), and upper()
def word_count(sentence , letter):
    count = 0
    sentence = sentence.upper()
    my_sent = [str(elem) for elem in sentence.split()]
    letter = letter.upper()
    for words in my_sent:
        if words[0] == letter:
            count += 1
    return count

if __name__ == "__main__":
    pass
    # FIXME 2a:
    print('Words count')
    # FIXME 2b: Prompt the user to input a sentence.
    sent_input = str(input('Please enter a sentence:\n'))
    # FIXME 2c: Prompt the user to input a letter.
    letter_input = str(input('Please enter a letter:\n'))
    # FIXME 2d: Call `word_count` with the values entered by the user, then print the result.
    count_letter = word_count(sent_input, letter_input)
    print(f'The number of words in the sentence that start with "{letter_input}" or {letter_input.upper()} is {count_letter}')
    # FIXME 2e: Print Done! at the end.
    print('Done!')

