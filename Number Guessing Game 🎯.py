import random
secret = random.randint(1,10)
print("Welcome to our Number Guessing Game 🎯")

while True:
    guess = int(input("Guess the number (1-10): "))
    if secret == guess:
        print("Correct")
        again = (input("Do you wanna play again? (y/n): ")).lower()
        if again == "n":
            print("thank you for playing our game")
            break
        elif again == "y":
            secret = random.randint(1,10)
            continue
        else:
            print("you press wrong key")
            break
    elif secret > guess:
        print("Too low")
    else:
        print("Too high")