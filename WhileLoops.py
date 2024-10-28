### Part Two -- your code goes here. 
import random
 secret_number = random.randit(1,100)
guess = None

print("Welcome to the guessing gamee!")
print("I'm thinking of a number between 1 & 100.")

while guess != secret_number:
  guess =input("Enter your guess:")
if not guess.isdigit():
   print("Please enter a valid number.")
        continue
    
guess = int(guess)

    
if guess < secret_number:
    print("Lower! Try again.")
elif guess > secret_number:
    print("Higher! Try again.")
else:
    print("Congratulations! You've guessed the right number!")
