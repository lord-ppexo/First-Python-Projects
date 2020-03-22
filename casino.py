from random import randint
bank = int(100)
decision = False

print("Welcome to the casino !!")
print("Your current bank is", bank)

while bank > 0:
    print("Would you like to play ?")

    debut = input()
    if debut == ('yes' or 'Yes'):
        
        computer_choice = randint(1, 5)
        human_choice = int(input("Choose a number between 1 et 5 :    "))
        mise = int(input("How much would you like to bet ?    "))
        
        while mise > bank:
            print("You don't have enough money to bet that much, try again.")
            mise = int(input("How much would you like to bet ?    "))
            
        if computer_choice == human_choice:
            print("You won !!")
            bank = bank - mise
            bank = mise * 10
            print("Bank : ", bank)
            print()

        else:
            print("You lost !!")
            bank = bank - mise
            print("Bank : ", bank) 
            print()



    else:
        break

    
print("You have no money left :( ")
