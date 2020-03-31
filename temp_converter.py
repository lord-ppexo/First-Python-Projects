

try:
    choice = input("Celsius to Fahrenheit (cf)? Other way around ? (fc) ")

    if choice == "cf":
        temp = int(input("What is the temperature ?   "))
        new_temp = int(temp*1.8 + 32)
        print(f"{temp}°C is equal to {new_temp}°F")
        
    elif choice == "fc":
        temp = int(input("What is the temperature ?   "))
        new_temp = (temp - 32) / 1.8
        print(f"{temp}°F is equal to {new_temp}°C")


    user_again = input("Do you want to convert again ? (y / n)   ")
    if user_again == "y":
        print()

    elif user_again == "n":
        exit()
            
except:
    print("Please enter a valid input")
    print()
    
