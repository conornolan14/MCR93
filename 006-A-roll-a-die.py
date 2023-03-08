# Rev 2.0 with functions
player1_wins = 0
player2_wins = 0
number_turns = 3
current_turn = 0
print(".... lots print() functions to state the rules on how to play the game ....")

def turn():
    global current_turn
    global player1_wins
    global player2_wins
    current_turn += 1
    player1 = int(input('Enter number from ' + str(current_turn) + '. roll for player 1: '))
    player2 = int(input('Enter number from ' + str(current_turn) + '. roll for player 2: '))
    if player1 < player2:
        print('Player 2 won this turn')
        player2_wins = player2_wins + 1
    elif player1 > player2:
        print('Player 1 won this turn')
        player1_wins = player1_wins + 1
    else:
        print('It\'s a draw, this turn is invalid and must be repeated')

turn()
turn()
turn()

if player1_wins < player2_wins:
    print('Player 2 won this match with', player2_wins, 'winning turns.')
if player1_wins > player2_wins:
    print('Player 1 won this match with', player1_wins, 'winning turns.')
