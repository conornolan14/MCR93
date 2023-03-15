# our new data dtype for today is a list:
options = ['ROCK', 'PAPRE', 'SCISSORS']

# in above's list we gave it  -a variable name: options
#                             -3 list items: 'ROCK', 'PAPER', 'SCISSORS'
#                              Note that all list items are strings, but could
#                              be any other data type.

# selecting items from the list with indeces:
print('The first list item is:', options[0])
print('The second list item is:', options[1])
print('The third list item is:', options[2])

# oops the second list item is spelled incorrectly
options[1] = 'PAPER'
print('The corrected second list item is:', options[1])

# we can also output the whole list:
print(options)



