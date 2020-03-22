from random import randint
import sys
player = False
win = 0
loss = 0

decision = input("Would you like to play rock, paper, scissors ??   ")

while decision !=('yes' or 'Yes') and ('no' or 'No'):
    decision = input("Would you like to play rock, paper, scissors ??   ")

if decision == ('no' or 'No'):
    sys.exit('Goodbye')
    

    
while player == False:
    human_choice = input("Choose from 'rock', 'paper', 'scissor'   ")
    computer_number = randint(1, 3)

    if computer_number == 1:
        computer_choice = 'rock'

    elif computer_number == 2:
        computer_choice = 'paper'

    elif computer_number == 3:
        computer_choice = 'scissor'


        
    if human_choice == computer_choice:
        print("Draw")

    elif human_choice == 'rock':
        if computer_choice == 'scissor':
            print("You win")
            win += 1
            
        else:
            print("You lose")
            loss += 1

    elif human_choice == 'paper':
        if computer_choice == 'rock':
            print("You win")
            win += 1
            
        else:
            print("You lose")
            loss += 1

    elif human_choice == 'scissor':
        if computer_choice == 'paper':
            print("You win")
            win += 1

        else:
            print("You lose")
            loss += 1

    print("You have", win,"wins and", loss,"losses.")
    print()
    re = input("Do you want to play again ?   ")
    if re != ('yes' or 'Yes'):
        break
    
