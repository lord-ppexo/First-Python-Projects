def doIt():
    def collatz(number):
        if number % 2 == 0:
            result = number // 2
            return result
        else:
            result = 3 * number + 1
            return result


    try:
        num = int(input("Enter number:  "))
        result = collatz(num)
        
        while result != 1:
            result = collatz(result)
            print(result)

        
    except:
        print("please enter an integer")
        
