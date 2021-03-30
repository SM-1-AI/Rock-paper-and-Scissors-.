import random
import time 

lst = ["r","p","s"]
lst2 = ['q']
chance = 10
your_point = 0
computer_point = 0
no_chance = 0
var1 =("s")

print("Hello!")
time.sleep(2)
print("This is rock,paper,scissors game.")
time.sleep(2)
print("Please use 'r' for rock, 'p' for paper and 's' for scissors and 'q' to quit...")
time.sleep(2)
print("Please press'S' to start the game.. ")
var1 = input()
if var1 =='s':
    print(" OK! the game is about to begin in ")
    time.sleep(2)
    print("And yes you cannot have the same input again and again. Example: if you have 's' as the input then you cannot use 's' in the next round. ")
    time.sleep(4)
    print("All the best!")
    time.sleep(2) 
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("START!")
    time.sleep(1)
    while no_chance < chance:
        player = input("what you want!:\n")
        computer = (random.choice(lst))
        time.sleep(2)
        if player == computer:
            time.sleep(1)
            print("it's a tie! both have guess the same..")

        elif player == "s" and computer == "r":
            computer_point = computer_point + 1
            print("computer has won this time!")
            time.sleep(1)
            print("because you have scissors and computer has rock...")
            time.sleep(1)
            print("computer has broken your scissors.. ")
            time.sleep(1)
            print("computer wins 1 point\n")
            print(f"computer point is{computer_point} and your point is {your_point}")

        elif player== "q":
            print("OK as you are quitting the game therefore the computer is declared as the winner!")
            time.sleep(2)
            print("computer got winner winner chicken dinner!")
            time.sleep(4)
            break

        elif player == "s" and computer == "p":
            your_point = your_point + 1
            print("congratulation! you won this time!")
            time.sleep(1)
            print("because you have scissors and computer has paper...")
            time.sleep(1)
            print("you have cut the paper of the computer... ")
            time.sleep(1)
            print("you wins 1 point\n")
            print(f"computer point is{computer_point} and your point is {your_point}")


        elif player== "p" and computer == "s":
            computer_point = computer_point +1
            print("computer has won this time!")
            time.sleep(1)
            print("because you have paper and computer has scissors...")
            time.sleep(1)
            print("computer has cut your paper... ")
            time.sleep(1)
            print("computer wins 1 point\n")
            print(f"computer point is{computer_point} and your point is {your_point}")


        elif player== "p" and computer == "r":
            your_point = your_point +1
            print("You have won this time!")
            time.sleep(1)
            print("because you have paper and computer has rock...")
            time.sleep(1)
            print("you have covered the rock with paper... ")
            time.sleep(1)
            print("you win 1 point this time...\n")
            print(f"computer point is{computer_point} and your point is {your_point}")


        elif player== "r" and computer == "s":
            your_point = your_point +1
            print("you have won this time!")
            time.sleep(1)
            print("because you have rock and computer has scissors...")
            time.sleep(1)
            print("you have broken the computer's scissors... ")
            time.sleep(1)
            print("You wins 1 point\n")
            print(f"computer point is{computer_point} and your point is {your_point}")


        elif player== "r" and computer == "p":
            computer_point = computer_point +1
            print("computer has won this time!")
            time.sleep(1)
            print("because you have rock and computer has paper...")
            time.sleep(1)
            print("computer has covered  your rock... ")
            time.sleep(1)
            print("computer wins 1 point\n")
            print(f"computer point is{computer_point} and your point is {your_point}")

        else:
            print("you have wrong input dear player..\n")

print("GAME OVER!")      


if computer_point > your_point:
    print("Computer wins and you loose")
    time.sleep(3)
    print("computer got winner winner chicken dinner!!")

if computer_point < your_point:
    print("you win and computer loose")
    time.sleep(3)
    print("you got winner winner chicken dinner!")

print(f"Your point is {your_point} and computer's point is {computer_point}.")