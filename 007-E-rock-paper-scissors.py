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
human_input = selected_options[0]
random_option = selected_options[1]

while human_input == random_option:
    print('Python played a',random_option ,': It\'s a draw. There must be a new turn')
    selected_options = get_options(options)
    human_input = selected_options[0]
    random_option = selected_options[1]

if human_input == 'ROCK' and random_option == 'SCISSORS':
    print('Python played a',random_option ,': Human Player Wins')
elif human_input == 'PAPER' and random_option == 'ROCK':
    print('Python played a',random_option ,': Human Player Wins')
elif human_input == 'SCISSORS' and random_option == 'PAPER':
    print('Python played a',random_option ,': Human Player Wins')

else:
    print('Python played a',random_option ,': Human Player Lost')
