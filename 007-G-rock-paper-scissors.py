# This is the international version !

import random

print('[P] Portuguese')
print('[I] Irish')
print('[E] English')
print('[G] German')
print()
language = input('Please select a language [P, I, E or G]')


if language == 'P':
    options = ['PEDRA', 'PAPEL', 'TESOURA']
elif language == 'I':
    options = ['CLOCH', 'PAIPEAR', 'SISUR']
elif language == 'E':
    options = ['ROCK', 'PAPER', 'SCISSORS']
else:
    options = ['STEIN', 'PAPIER', 'SCHERE']

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


if selected_options[0] == options[0] and selected_options[1] == options[2]:
    print('Python played a',selected_options[1] ,': Human Player Wins')
elif selected_options[0] == options[1] and selected_options[1] == options[0]:
    print('Python played a',selected_options[1] ,': Human Player Wins')
elif selected_options[0] == options[2] and selected_options[1] == options[1]:
    print('Python played a',selected_options[1] ,': Human Player Wins')

else:
    print('Python played a',selected_options[1] ,': Human Player Lost')
