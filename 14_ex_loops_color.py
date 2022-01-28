import random
colors = ["black","white","red","green","blue","yellow","purple","grey"]

while True:
    color = colors[random.randint(0,len(colors)-1)]
    guess = input("Guess a colour: ")

    while True:
        if (color == guess.lower()):
            break
        else:
            print(color)
            guess = input("try again: ")
    print ("Correct!")

    play_again = input("play again? Yes or No: ")

    if play_again.lower() == "no":
        break
print("OK, Bye!")

    
