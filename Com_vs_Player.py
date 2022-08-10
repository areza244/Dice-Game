# Amirreza Pazira
# 02 Oct 2020
# Assignment - 1 Problem - 8


# Problem_8 = Player vs Computer

# Importing important packages for generating a random number
# and for delaying the output for better understanding of what is happening
import random
import time

# Creating our variables turn score and total score for both player one and two
turn = 0
score = 0
turn_two = 0
score_two = 0
player_one = True
player_two = True
# generating a number between 1 and 2 to see who goes first
player = random.randint(1,2)

# Welcome prompt and input for starting the game
print ("Welcome To The Pigs Game!")
start = str(input("Enter s to start! : "))

# if start input is s the game will start this our main game loop
while start == "s":
# if the player random number is equal to 1 player one will go first   
    if (player != 2):
        print ()
        print ("It's Player's turn")
        time.sleep(0.5)
        print ()
# player one's inner loop
        while player_one:
# here we ask the player if he wants to roll or hold
            choice = str(input("Do you want to [r]oll or [h]old? "))
# if he chooses to hold the turn will end
            if (choice == "h"):
                player_one = False
                turn = 0
                print ()
                print ("Player's score: ", score)
                print ("Computer's score: ", score_two)
                player = player + 1
                break
# if he chooses to roll he will roll one number
            elif (choice == "r"):
                roll = random.randint(1,6)
                if (roll > 1):
                    print ()
                    print ("you rolled a : ", roll)
                    turn = turn + roll
                    score = score + roll
                    print ("your turn score is: ", turn)
                    print ()
# if the roll is equal to one the loop will break and turn will end with zero score and player will pig out
                elif (roll == 1):
                    score = score - turn
                    turn = 0
                    print ("you rolled a: ", roll)
                    time.sleep(0.5)
                    print ()
                    print ("you pigged out! ")
                    time.sleep(0.5)
                    print ("your turn score is: ", turn)
                    time.sleep(0.5)
                    print ()
                    print ("Player's score: ", score)
                    print ("Computer's score: ", score_two)
                    player = player + 1
                    break
# if the players reaches 100 score he wins and game will end
                if (score >= 100):
                    print ()
                    print ("your score is: ", score)
                    print ("Final score is: ", score ," vs ", score_two)
                    print ()
                    print ("Player wins!")
                    start = "end"
                    break
# if player random number is 2 player two will go first          
    if (player == 2):
        print ()
        print ("It's Computer's turn")
        time.sleep(0.5)
        print ()
        player_two = True
# player two's inner loop
        while player_two:
# computer will roll a number
            roll = random.randint(1,6)
            print ("Computer rolled a: ", roll)
            turn_two = turn_two + roll
            score_two = score_two + roll
            time.sleep(1)
# if roll is equal to 1 loop will break and turn score is 0 and computer will pig out
            if (roll == 1):
                score_two = score_two - turn_two
                turn_two = turn_two - turn_two
                print ()
                print ("Computer pigged out! ")
                time.sleep(0.5)
                print ("Computer's turn score is: ", "0")
                time.sleep(0.5)
                print ()
                print ("Player's score: ", score)
                print ("Computer's score: ", score_two)
                player = player - 1
                player_two = False
                player_one = True
# we don't want the computer to roll until it pigs out so it will hold when turn score is above or equal 20
            elif ( turn_two >= 20):
                print ()
                print ("Computer's turn score is: ", turn_two)
                time.sleep(0.5)
                print ()
                print ("Player's score: ", score)
                print ("Computer's score: ", score_two)
                turn_two = turn_two - turn_two
                player = player - 1
                player_two = False
                player_one = True
# if computer reaches 100 score it wins and the game will end
            if (score_two >= 100):
                print ()
                print ("Computer's turn score is: ", turn_two)
                print ("Final score is: ", score_two ," vs ", score)
                print ()
                print ("Computer wins!")
                start = "end"
                break