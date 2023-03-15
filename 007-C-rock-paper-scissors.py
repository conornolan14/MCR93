import random

# our new data dtype for today is a list:
options = ['ROCK', 'PAPER', 'SCISSORS']

human_input = input("'ROCK', 'PAPER' or 'SCISSORS' ")

random_number = random.randrange(0, 3)
random_option = options[random_number]

if human_input == 'ROCK' and random_option == 'SCISSORS':
    print('Python played a',random_option ,': Human Player Wins')
elif human_input == 'PAPER' and random_option == 'ROCK':
    print('Python played a',random_option ,': Human Player Wins')
elif human_input == 'SCISSORS' and random_option == 'PAPER':
    print('Python played a',random_option ,': Human Player Wins')
elif human_input == random_option:
    print('Python played a',random_option ,': It\'s a draw')
else:
    print('Python played a',random_option ,': Human Player Lost')

