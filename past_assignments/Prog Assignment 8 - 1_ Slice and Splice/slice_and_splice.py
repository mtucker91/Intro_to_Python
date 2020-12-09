# FIXME 1: Complete the function. The function takes a string (slice it and splice
#  it) then return the modified string.
def slice_and_splice(s):
    half = round((len(s) / 2))
    slice_object = slice(half)
    front_s = s[slice_object]
    slice_object = slice(half, len(s), 1)
    back_s = s[slice_object]
    new_s = back_s + front_s
    return(new_s)



if __name__ == "__main__":
    pass
    # FIXME 2a: Print a statement that says what the program is going to do.
    print('This program is going to slice and splice a string')
    # FIXME 2b: Prompt the user to enter a string
    string_input = str(input('Enter a string to be sliced and spliced:\n'))
    # FIXME 2c: Call the function and print the result
    splice_val = slice_and_splice(string_input)
    print(f'"{string_input}" after being sliced and spliced is "{splice_val}"')
    # FIXME 2d: Print Done! at the end
    print('Done!')
