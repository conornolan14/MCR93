import random

repeat_times = 2
count_times = 0
count_human_wins = 0
count_human_losses = 0    # this would be the same as count_times - count_human_wins


#user_selected_the_language = False
#while user_selected_the_language == False:
print('[P] Portuguese')
print('[I] Irish')
print('[E] English')
print('[G] German')
print()
language = input('Please select a language [P, I, E or G]')
#    user_selected_the_language == True

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


for i in range(repeat_times):
    selected_options = get_options(options)

    while selected_options[0] == selected_options[1]:
        print('Python played a',selected_options[1] ,': It\'s a draw. There must be a new turn')
        selected_options = get_options(options)

    count_times += 1
    if selected_options[0] == options[0] and selected_options[1] == options[2]:
        print('Python played a',selected_options[1] ,': Human Player Wins This Turn')
        count_human_wins += 1
    elif selected_options[0] == options[1] and selected_options[1] == options[0]:
        print('Python played a',selected_options[1] ,': Human Player Wins This Turn')
        count_human_wins += 1
    elif selected_options[0] == options[2] and selected_options[1] == options[1]:
        print('Python played a',selected_options[1] ,': Human Player Wins This Turn')
        count_human_wins += 1
    else:
        print('Python played a',selected_options[1] ,': Human Player Lost This Turn')
        count_human_losses += 1


if count_human_losses < count_human_wins:
    print('Human won this tournament with', count_human_wins, 'wins out of', count_times, 'turns.')
elif count_human_losses > count_human_wins:
    print('Human lost this tournament with only', count_human_wins, 'wins out of', count_times, 'turns.')
else:
    print('The tournament is a draw. There was no winner.')




