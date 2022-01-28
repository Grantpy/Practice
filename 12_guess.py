number = 5
guess = int(input("Guess number 0 to 10"))

while True:
    if guess == number:
        break
    else:
        guess = int(input("try again"))
print("Correct")
