# TODO Create an empty list to maintain the player names
players = []

# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'
add_player = input("Would you like to add a player to the list? (Yes/No)  ")
while add_player.lower() == "yes":
    players.append(input("Enter the name of the player to add to the team: "))
    add_player = input("Would you like to add a player to the list? (Yes/No)  ")
# TODO print the number of players on the team
print("There are {} players on the team".format(len(players)))

# TODO Print the player number and the player name
# The player number should start at the number one

for i in range(len(players)):
    print("Player {}: {}".format(i+1, players[i]))

# TODO Select a goalkeeper from the above roster
goalkeeper = int(input("Please select the goal keepr by selecting the player number. (1-{}) ".format(len(players))))

# TODO Print the goal keeper's name
# Remember that lists use a zero based index
print("Great!!! The goalkeeper for the game will be", players[goalkeeper-1])
