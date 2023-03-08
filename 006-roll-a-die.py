player1_wins = 0
player2_wins = 0
print(".... lots print() functions to state the rules on how to play the game ....")
player1 = int(input('Enter number from 1. roll for player 1: '))
player2 = int(input('Enter number from 1. roll for player 2: '))
if player1 < player2:
    print('Player 2 won this turn')
    player2_wins = player2_wins + 1
elif player1 > player2:
    print('Player 1 won this turn')
    player1_wins = player1_wins + 1
else:
    print('It\'s a draw, this turn is invalid and must be repeated')

player1 = int(input('Enter number from 2. roll for player 1: '))
player2 = int(input('Enter number from 2. roll for player 2: '))
if player1 < player2:
    print('Player 2 won this turn')
    player2_wins = player2_wins + 1
elif player1 > player2:
    print('Player 1 won this turn')
    player1_wins = player1_wins + 1
else:
    print('It\'s a draw, this turn is invalid and must be repeated')

player1 = int(input('Enter number from 3. roll for player 1: '))
player2 = int(input('Enter number from 3. roll for player 2: '))
if player1 < player2:
    print('Player 2 won this turn')
    player2_wins = player2_wins + 1
elif player1 > player2:
    print('Player 1 won this turn')
    player1_wins = player1_wins + 1
else:
    print('It\'s a draw, this turn is invalid and must be repeated')

if player1_wins < player2_wins:
    print('Player 2 won this match with', player2_wins, 'winning turns.')
if player1_wins > player2_wins:
    print('Player 1 won this match with', player1_wins, 'winning turns.')

