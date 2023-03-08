# Rev 3.0 with functions and loops and validate input for a number from 1 to 6
player1_wins = 0
player2_wins = 0
number_turns = 3
current_turn = 0
print(".... lots print() functions to state the rules on how to play the game ....")

def number_input(player_number, current_turn):
    number_entered = 0
    while number_entered == 0:
        number_entered = int(input('Enter number from ' + str(current_turn) +
        '. roll for player ' + player_number + ': '))
        if number_entered <= 0 or number_entered >= 7:
            number_entered = 0
    return number_entered


def turn():
    global current_turn
    global player1_wins
    global player2_wins
    current_turn += 1
    player1 = number_input('1', current_turn)
    player2 = number_input('2', current_turn)
    if player1 < player2:
        print('Player 2 won this turn')
        player2_wins = player2_wins + 1
    elif player1 > player2:
        print('Player 1 won this turn')
        player1_wins = player1_wins + 1
    else:
        print('It\'s a draw, this turn is invalid and must be repeated')
        current_turn -= 1

while current_turn < number_turns:
    turn()


if player1_wins < player2_wins:
    print('Player 2 won this match with', player2_wins, 'winning turns.')
if player1_wins > player2_wins:
    print('Player 1 won this match with', player1_wins, 'winning turns.')
