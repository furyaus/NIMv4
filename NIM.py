print("\n\nWelcome to the game of NIMv1.0\n")
coins = 20
userlose = False
while coins > 0:
    userpick = int(input("Select 3, 2 or 1 coins to pick up: "))
    coins = coins - userpick
    if coins <= 0:
        userlose = True
        break
    print("Coins left after user: "+str(coins))
    comppick = 3
    coins = coins - comppick
    if coins <= 0:
        print("Coins left after comp: 0\n")
        break
    print("Coins left after comp: "+str(coins)+"\n")
if userlose == True:
    print("Computer wins - Thanks for playing!")
else:
    print("User wins - Thanks for playing!\n")
