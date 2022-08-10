# Amirreza Pazira
# 02 Oct 2020
# Assignment - 1 Problem - 7


# Problem_7 = Computer vs Computer

# Importing "random" package for generating a random number
import random

# Creating our variables turn score and total score for both player one and two
turn = 0
score = 0
turn_two = 0
score_two = 0
player_one = True
player_two = True
game = True
# generating a number between 1 and 2 to see who goes first
player = random.randint(1,2)
# Our main game loop
while game:
# if the player random number is equal to 1 player one will go first 
    if (player != 2):
        player_one = True
        print ()
        print ("It's Player One's turn")
        print ()
# player one loop
        while player_one:
# player one will roll a number
            roll = random.randint(1,6)
            print ("you rolled a: ", roll)
            turn = turn + roll
            score = score + roll
# if the roll is equal to 1 loop will break and turn score is 0 and player will pig out
            if (roll == 1):
                score = score - turn
                turn = turn - turn
                print ()
                print ("you pigged out! ")
                print ("your turn score is: ", turn)
                print ()
                print ("Player One's score: ", score)
                print ("Player Two's score: ", score_two)
                player = player + 1
                player_one = False
# we don't want the computer to roll until it pigs out so it will hold when turn score is above or equal 20
            elif ( turn >= 20):
                print ()
                print ("your turn score is: ", turn)
                print ()
                print ("Player One's score: ", score)
                print ("Player Two's score: ", score_two)
                turn = turn - turn
                player = player + 1
                player_one = False
# if a player reaches 100 score he wins and the game will end
            if (score >= 100):
                print ()
                print ("your turn score is: ", turn)
                print ("Final score is: ", score ," vs ", score_two)
                print ()
                print ("Player One wins!")
                game = False
                break
# if the player random number is equal to 1 player one will go first           
    if (player == 2):
        print ()
        print ("It's Player Two's turn")
        print ()
        player_two = True
# player two loop
        while player_two:
# player two will role a number
            roll = random.randint(1,6)
            print ("you rolled a: ", roll)
            turn_two = turn_two + roll
            score_two = score_two + roll
# if the roll is equal to 1 loop will break and turn score is 0 
            if (roll == 1):
                score_two = score_two - turn_two
                turn_two = turn_two - turn_two
                print ()
                print ("you pigged out! ")
                print ("your turn score is: ", "0")
                print ()
                print ("Player One's score: ", score)
                print ("Player Two's score: ", score_two)
                player = player - 1
                player_two = False
# hold when turn score is above or equal 20
            elif ( turn_two >= 20):
                print ()
                print ("your turn score is: ", turn_two)
                print ()
                print ("Player One's score: ", score)
                print ("Player Two's score: ", score_two)
                turn_two = turn_two - turn_two
                player = player - 1
                player_two = False
# here player two will win if he gets 100 score
            if (score_two >= 100):
                print ()
                print ("your turn score is: ", turn_two)
                print ("Final score is: ", score_two ," vs ", score)
                print ()
                print ("Player Two wins!")
                game = False
                break