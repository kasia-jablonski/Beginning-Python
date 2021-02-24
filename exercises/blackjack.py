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

deck = []

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
        # print(number)
        # print("usuwana " + d[number])
        shuffled_deck.append( d.pop(number))
        # print("shuffled ")
        # print(len(shuffled_deck))
        # print(shuffled_deck)
        # print("original")
        # print(len(d))
        # print(d)
    print(shuffled_deck)
    print(len(shuffled_deck))
    return shuffled_deck

new_deck = create_deck()
shuffled_deck = shuffle_cards(new_deck)

player_deck = []
dealer_deck = []

player_deck.append(shuffled_deck.pop())
dealer_deck.append(shuffled_deck.pop())
player_deck.append(shuffled_deck.pop())
dealer_deck.append(shuffled_deck.pop())

print("Player cards: %s, %s" %(player_deck[0], player_deck[1]))
print("Dealer cards: " + dealer_deck[0])
