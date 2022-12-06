#  import sys

print('Rock, Paper, Scissors')

#  Variables for Playernames

Name_Player_1 = 0
Name_Player_2 = 0


#  Ask for the names of the players and greet them
#  Player 1

print('Whats your name Player 1?')
Name_Player_1 = input()
print('Welcome to the game ' + Name_Player_1 + '!')

# Player 2

print('And you Player 2, whats your name?')
Name_Player_2 = input()
print('Welcome to you too ' + Name_Player_2 + '!')


#  Variables to keep track of the number of losses, wins and ties for the different Players

winsP1 = 0
lossesP1 = 0
tiesP1 = 0

winsP2 = 0
lossesP2 = 0
tiesP2 = 0


#  Choosing how many rounds to be played - sets the number of iterations of the main game loop
#  NEEDS CHANGE! Only 3, 5 or 7 have to be accepted - has to be added with a loop!

Number_of_rounds = 0


while True:
    print('First, you have to decide how many rounds you both want to play: 3, 5 or 7 rounds?')
    Number_of_rounds = input()
    if (Number_of_rounds == 3) or (Number_of_rounds == 5) or (Number_of_rounds == 7):
        continue
    print('so lets play')
    break


#  Main game for loop with range / rounds set by player

for i in range(Number_of_rounds):

    #  Display the actual results at every start of a new round

    print('Actual results of ' + Name_Player_1 + ':')
    print('Wins: ' + winsP1 + ' ')
    print('Losses: ' + lossesP1 + ' ')
    print('Ties: ' + tiesP1 + ' ')

    print('Actual results of ' + Name_Player_2 + ':')
    print('Wins: ' + winsP2 + ' ')
    print('Losses: ' + lossesP2 + ' ')
    print('Ties: ' + tiesP2 + ' ')

    # Game begins
