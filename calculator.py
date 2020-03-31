resultat = None

def calculatrice():
    global num1, num2, resultat
    while True:
        try:
            num1 = int(input(f"Entrez le premier numéro:   "))
            print()
            num2 = int(input(f"Entrez le deuxième numéro:   "))
            print()
            operation = input(f"Opération souhaitée (+, -, *, /, %) or (quit):   ")

            if operation == "+":
                print(f"Résultat : {num1 + num2}")

            elif operation == "-":
                print(f"Résultat : {num1 - num2}")

            elif operation == "*":
                print(f"Résultat : {num1 * num2}")

            elif operation == "/":
                print(f"Résultat : {num1 / num2}")

            elif operation == "%":
                print(f"Résultat : {num1 % num2}")

            elif operation == "quit":
                break

            else:
                print(f"Suivez les instructions svp")
                print()
        except:
            print(f"Suivez les instructions svp")
            print()
