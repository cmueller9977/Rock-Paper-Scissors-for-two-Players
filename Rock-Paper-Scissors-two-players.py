#  import sys

print('Rock, Paper, Scissors')

# Variables for Playernames and how many rounds to be played

Name_Player_1 = 0
Name_Player_2 = 0


# Ask for the names of the players and greet them
# Player 1

print('Whats your name Player 1?')
Name_Player_1 = input()
print('Welcome to the game ' + Name_Player_1 + '!')

# Player 2

print('And you Player 2, whats your name?')
Name_Player_2 = input()
print('And you too ' + Name_Player_2 + '!')


# Variables to keep track of the number of losses, wins and ties for the different Players

winsP1 = 0
lossesP1 = 0
tiesP1 = 0

winsP2 = 0
lossesP2 = 0
tiesP2 = 0

# Main game loop
# Choosing how many rounds to be played - sets the number of iterations of the main game loop

Number_of_rounds = 0
print('First you have to decide how many rounds you both want to play: 3, 5 or 7 rounds?')
Number_of_rounds = input()
