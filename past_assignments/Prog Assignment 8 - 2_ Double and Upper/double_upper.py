# FIXME 1: Complete the function double_upper. The function takes in a string and return a string. No print.
def double_upper(str):
  doubled_str = ''
  for index in range(len(str)):
    doubled_str += str[index] + str[index]
  doubled_str = doubled_str.upper()
  return doubled_str

if __name__ == "__main__":
  pass
  # FIXME 2a: Print a statement that says what the program is going to do.
  print('Double and Upper word')
  # FIXME 2b: Prompt the user to enter a word
  string_input = str(input('Enter a word:\n'))
  # FIXME 2c: Call the function, and print the result.
  str_output = double_upper(string_input)
  print(f'{string_input} becomes: {str_output}')
  # FIXME 2d: Print Done! at the end.
  print('Done!')
