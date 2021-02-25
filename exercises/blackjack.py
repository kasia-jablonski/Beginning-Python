import random
import math
cards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,    
    "Q": 10,
    "K": 10,
    "A": [1, 11],
}
symbols = ["\u2665", "\u2660", "\u2663", "\u2666"]

def create_deck():
    deck = list(cards.keys())*4
    for i in range(len(deck)):
        deck[i] += symbols[math.floor(i / 13)]
    return deck

def shuffle_cards(d):
    shuffled_deck = []
    number_cards = len(d) - 1
    for x in range(51, 0, -1):
        number = random.randint(0, x)
        shuffled_deck.append( d.pop(number))
    return shuffled_deck

def count_points(deck):
    count = 0
    ace_count = 0
    for i in deck:
        if len(i) == 2:
            a = i[0]
            if a != 'A':
                count += cards[a]
            else:
                ace_count += 1
                count += cards[a][1]
        else:
            a = i[0:2]
            count += cards[a]
    if count > 21 and ace_count >= 1:
        count -= ace_count * 10
    return count

def compare(dd, pd):
    if count_points(dd) > 21:
        print("Bust")
        print("You win")
    else: 
        if count_points(pd) > count_points(dd):
            print("You win")
        else:
            print("Dealer wins") 

def print_deck(deck, playerName):
    card_list = ""
    for i in deck:
        card_list += i + ", "
    print(playerName + " cards: " + card_list[:-2])
    print(playerName + " points: %s" %count_points(deck))

def hit(pd, deck, playerName):
    pd.append(deck.pop())
    card_list = ""
    print_deck(pd, playerName)

def stand(dd, deck):
    print_deck(dd, "Dealer")
    if count_points(dd) == 21:
        print("Blackjack")
    else:
        while count_points(dd) < 17:
            hit(dd, deck, 'Dealer')
    return count_points(dd)

def check21(deck):
    if count_points(deck) == 21:
        print("Blackjack")
        print("You win")
        return False
    else:
        return True

CONTINUE_GAME = True
while (CONTINUE_GAME):
    new_deck = create_deck()
    shuffled_deck = shuffle_cards(new_deck)

    player_deck = []
    dealer_deck = []

    player_deck.append(shuffled_deck.pop())
    dealer_deck.append(shuffled_deck.pop())
    player_deck.append(shuffled_deck.pop())
    dealer_deck.append(shuffled_deck.pop())


    print("Player cards: %s, %s" %(player_deck[0], player_deck[1]))
    print("Player points: %s" %count_points(player_deck))
    print("Dealer cards: " + dealer_deck[0])
    print("Dealer points: %s" %count_points(dealer_deck[0:1]))
    count_points(player_deck)

    CONTINUE_GAME = check21(player_deck)
    choice = ''
    while (choice != 'hit' or choice != 'stand'):
        print("Do you want to hit or stand?")
        print("Enter HIT or STAND")
        choice = (input("> ")).lower()
        if choice == 'hit':
            hit(player_deck, shuffled_deck, 'Player')
            if (count_points(player_deck) > 21):
                CONTINUE_GAME = False
                print("Bust")
                print("Dealer wins")
                break
        elif choice == 'stand':
            stand(dealer_deck, shuffled_deck)
            compare(dealer_deck, player_deck)
            CONTINUE_GAME = False
            break
    print("Play Again (Y/N)")
    continueGame = (input("> ")).lower()
    if (continueGame == "y"):
        CONTINUE_GAME = True


