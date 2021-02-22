name = input("What's your name? ")

# TODO: Ask the user by name if they understand Python while loops
print("{}, do you understand Python while loops?".format(name))
answer = input("(Enter yes/no)")
# TODO: Write a while statement that checks if the user doesn't understand while loops
# TODO: Since the user doesn't understand while loops, let's explain them.
# TODO: Ask the user again, by name, if they understand while loops.
while answer.lower() != "yes":
    print("Ok, {}, while loops in Python repeat as long as a certain Boolean condition is met.".format(name))
    print("{}, do you understand Python while loops?".format(name))
    answer = input("(Enter yes/no)")
print("That's great, {}. I'm pleased that you understand while loops now.".format(name))
# TODO: Outside the while loop, congratulate the user for understanding while loops
 
