import random
import re

def generate():
    return random.randint(1, 100)

def compare(g, r):
    if g > r:
        print("Number is too high")
    elif g < r:
        print("Number is too low")
    else:
        print("You guessed number")
        return True   

random = generate()

# print("Guess number between 1 and 100")
# guess = input("> ")
guess = 0
# while ( (re.match("\d+", guess) == None) and (int(guess) not in range(1, 100))):
#     print("Guess number between 1 and 100")
#     guess = (input("> "))

x = False
while (x != True):
    if (guess not in range(1, 100)):
        print("Guess number between 1 and 100")
        guess = int(input("> "))
    else:
        x =  compare(guess, random)
        guess = int(input("> "))

