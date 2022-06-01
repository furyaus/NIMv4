#---------------------------------------------
# Course: DIT10
# Room: L01
# Date: 23/05/2022
# Username: rwebb67   
# Name: Ryan Webb
# Description: Version 3 of the program of NIM
#---------------------------------------------

# Import libraries
import random
pvpversion = False

# Coin pile function
def showcoinpile(coins):
    coinstring = " "
    for count in range(coins):
        coinstring = coinstring + "* "  
    coinstring = coinstring + " ("+str(coins)+")"
    return(coinstring)

def entercoins(user):
    # User pick coin
    while True:     # Error catch and check the input from the user
        try:
            result = int(input(user+" select 3, 2 or 1 coins to pick up: "))
            if result > 3 or result <1:
                raise ValueError
            else:
                break
        except ValueError:
            print('You entered a non valid value, try again.')
            continue
    return result

# Main program function
def start(): 
    print("\n")
    coins = random.randint(10, 40) # Set the beinging coins between 10 and 100
    print("Starting coin pile: "+showcoinpile(coins))

    # While the coins pile still has more than 0, continue the game
    while coins > 0:

        # User 1 coin pick
        coins = coins - entercoins("User1") # Take away the userpick from the current coin pile
        if coins <=0:            # Check if the coin pile is at zero after the user has picked
            userlose = True
            if pvpversion == True:
                print("User1 picked up last coin, User2 wins!")
            else:
                print("User1 picked up last coin, computer wins!")
            break
        print("Coins left after user1: "+showcoinpile(coins))

        # Computer or User 2 coin pick
        if pvpversion == True:
            coins = coins - entercoins("User2") # Take away the userpick from the current coin pile
            print("Coins left after User2: "+showcoinpile(coins))
        else:
            comppick = 1 # Set comppick to 1
            n = ((coins - comppick -5)/4) +1  # Check to see if the n'th term is currently on the lose pattern
            while not n.is_integer():        # While not on the n'th term for losing, caculate how many coins for the comp to pick up
                comppick = comppick +1
                n = ((coins - comppick -5)/4) +1
            if comppick == 4:
                comppick = comppick-1
            print("Computer selects for pickup: "+str(comppick))
            coins = coins - comppick        # Take away the comppick from the current coin pile
            print("Coins left after comp: "+showcoinpile(coins))

        if coins <= 0:                  # Check if the coin pile is at zero after the user has picked
            if pvpversion == True:
                print("User2 picked up last coin, User1 wins!")
            else:
                print("Computer picked up last coin, user wins!")
            break

    print("Thanks for playing, worlds best game")
    
    # Do you want to play again? Check with user
    again = input("Would you like to play again? ")
    if again == "y" or again == "Y":
        print("Great!")
        start()
    else:
        print("You have too, your stuck!")
        start()

# Call the main program function, print welcome and run the game
print("\n")
print("Welcome to the game of NIMv3.0")
print("Nim is a mathematical game of strategy in which two players take turns removing objects from distinct heaps or piles.")
print("In this version, you can select 3, 2 or 1 coins and it will start will a random amount of coins between 10 and 100.")

# Do you want to play again? Check with user
pvp = input("Would you like to play PVP? ")
if pvp == "y" or pvp == "Y":
    pvpversion = True

# Start the game
start()