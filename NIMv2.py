def start():
    print("\n")
    print("Welcome to the game of NIMv1.0")
    print("Nim is a mathematical game of strategy in which two players take turns removing objects from distinct heaps or piles")
    def showcoinpile():
        coinstring = " "
        for count in range(coins):
            coinstring = coinstring + "* "
        return(coinstring)
    coins = int(input("Enter the amount of coins to start with: "))
    print("Starting coin pile: "+showcoinpile())
    while coins > 0:
        userpick = int(input("Select 3, 2 or 1 coins to pick up: "))
        coins = coins - userpick
        if coins <= 0:
            userlose = True
            print("User picked up last coin, computer wins!")
            break
        print("Coins left after user: "+showcoinpile())
        comppick = 3
        coins = coins - comppick
        if coins <= 0:
            print("Computer picked up last coin, user wins!")
            break
        print("Coins left after comp: "+showcoinpile())
        showcoinpile()
    print("Thanks for playing, worlds best game")
    
    again = input("Would you like to play again? ")
    if again == "y" or again == "Y":
        print("Great! \n")
        start()
    else:
        print("You have too, your stuck! ")
        start()
start()