import random
def rolling():
    return random.randint(1, 6)

print(rolling())
while True:
    
    roll = input("Would you like to roll again? Y/N ")
    if roll.lower() == 'y' or roll.lower() == 'yes':
        print(rolling())
    else:
        break

