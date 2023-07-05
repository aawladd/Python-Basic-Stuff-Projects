import random as r

num = r.randrange(100)

Guess = 5

while Guess >= 0:
    your_guess = int(input("Enter your Guess : "))

    def check(x):
        if your_guess == x:
            print("You Win")
            exit()
        
        elif your_guess > x:
            print("you are close, keep trying lower")
        
        else:
            print("yor are close, keep trying higher")

    if Guess > 1:
        check(num)
    elif Guess==1:
        check(num)
        print("This is your last chance, make the most of it")
    else:
        print("You Lost")
        print("The number was ", num)
    
    Guess = Guess -1
