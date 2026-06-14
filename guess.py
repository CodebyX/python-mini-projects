import random
secret_number = random.randint(1,10)
print("Welcome to the number guessing game")
print("I have selected number between 1 and 10.")

attempts = 0

while True:
    guess=int(input("Enter your guess:"))
    
    attempts=attempts+1

    if guess < secret_number:
        print("Too low,try again")
    elif guess>secret_number:
        print("Too high,try again")

    else:
        print("Congratulations! You guessed the number.")
        print("You took",attempts,"attempts.")
        break    