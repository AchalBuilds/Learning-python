
print("I am thinking of a number between 1 to 100. Try guessing it!")

while True:
    guess = int(input("Enter your guess: "))
    
    if guess == 42:
        print("Spot on! 42 was the secret number. Great guessing!")
        break

    if guess == 67:
        print("You brainrot kid! Your guess is higher than the actual number.")    

    if guess > 42:
        print("Your guess is higher than the actual number.")
    else:
        print("Your guess is lower that the actual number")