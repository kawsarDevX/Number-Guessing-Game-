import random
print("Welcome to our Number Guessing Game 🎯")

while True:
    try:
        choice = int(input("Game Mode Selection\n 1. Easy: 1-10\n 2. Medium: 1-20\n 3. Hard: 1-30\n (Please select only 1, 2, or 3) : "))
        if 1<= choice <= 3:
            pass
        else:
            print("Error: Invalid Choice! Please select 1, 2, or 3 only........")
            continue
    except:
        print("Error: Invalid Choice! Please select 1, 2, or 3 only........")
        continue
        

    if choice == 1:
        secret = random.randint(1,10)
    elif choice == 2:
        secret = random.randint(1,20)
    elif choice == 3:
        secret = random.randint(1,30)
    
    while True:  
        try:
            if choice == 1:
                guess = int(input("Guess the number (Easy Mode) : "))
                if guess < 1 or guess > 10:
                    print("Please select between 1-10")
                    continue
            elif choice == 2:
                guess = int(input("Guess the number (Medium Mode) : "))
                if guess < 1 or guess > 20:
                    print("Please select between 1-20")
                    continue
            elif choice == 3:
                guess = int(input("Guess the number(Hard Mode) : "))
                if guess < 1 or guess > 30:
                    print("Please select between 1-30")
                    continue
            else:
                print("Error: Please enter valid number")
                continue
                

        except:
            print("Please Enter valid number: ")
            continue

        
        if secret == guess:
            print("🎉 Correct!")
            break
        elif secret > guess:
            print("📉 Too low")
        elif secret < guess:
            print("📈 Too high")

    again = (input("Do you wanna play again? (y/n): ")).lower()
    if again == "n":
        print("thank you for playing our game")
        break
    elif again == "y":
        continue
        
    else:
        print("you press wrong key")
        break

    