# our new data dtype for today is a list:
options = ['ROCK', 'PAPER', 'SCISSORS']

# in above's list we gave it  -a variable name: options
#                             -3 list items: 'ROCK', 'PAPER', 'SCISSORS'
#                              Note that all list items are strings, but could
#                              be any other data type.

# we need to find a random number between 0 and 2
import random  # imports (or you may say links) the random Python library
               # the Python random library allows us to use a method to pick a
               # random number

did_i_find_a_zero = False
did_i_find_a_one = False
did_i_find_a_two = False
zeros = 0
ones = 0
twos = 0

for i in range(10000):
    random_number = random.randrange(0, 3)
    if random_number == 0:
        did_i_find_a_zero = True
        zeros += 1
    if random_number == 1:
        did_i_find_a_one = True
        ones += 1
    if random_number == 2:
        did_i_find_a_two = True
        twos += 1

print('Did I find a 0:', did_i_find_a_zero, 'I found', zeros, ' zeros')
print('Did I find a 1:', did_i_find_a_one, 'I found', ones, ' ones')
print('Did I find a 2:', did_i_find_a_two, 'I found', twos, ' twos')


