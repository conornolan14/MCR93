# In this version we reduce the line count

import random

# our new data dtype for today is a list:
options = ['ROCK', 'PAPER', 'SCISSORS']

def get_options(options):
    human_input = ''
    input_prompt = 'Please enter your choice of ' + options[0] + ', ' + options[1] + ' or ' + options[2] + ': '
    while not(human_input == options[0] or human_input == options[1] or human_input == options[2]):
        human_input = input(input_prompt).upper().strip()
    random_number = random.randrange(0, 3)
    random_option = options[random_number]
    return [human_input, random_option]

selected_options = get_options(options)

while selected_options[0] == selected_options[1]:
    print('Python played a',selected_options[1] ,': It\'s a draw. There must be a new turn')
    selected_options = get_options(options)


if selected_options[0] == 'ROCK' and selected_options[1] == 'SCISSORS':
    print('Python played a',selected_options[1] ,': Human Player Wins')
elif selected_options[0] == 'PAPER' and selected_options[1] == 'ROCK':
    print('Python played a',selected_options[1] ,': Human Player Wins')
elif selected_options[0] == 'SCISSORS' and selected_options[1] == 'PAPER':
    print('Python played a',selected_options[1] ,': Human Player Wins')

else:
    print('Python played a',selected_options[1] ,': Human Player Lost')
