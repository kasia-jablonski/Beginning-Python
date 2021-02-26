import random

words = ["abruptly", "absurd", "abyss", "affix", "avenue", "awkward", "azure", "bagpipes", "banjo", "bayou", "beekeeper", "bikini", "blizzard", "boggle", "bookworm", "boxful", "buffalo", "buxom", "buzzard", "buzzwords", "caliph", "cockiness", "croquet", "crypt", "curacao", "cycle", "dizzying", "duplex", "dwarves", "equip", "espionage", "exodus", "faking", "fishhook", "fixable", "fjord", "flapjack", "flopping", "fluffiness", "foxglove", "frizzled", "fuchsia", "funny", "gabby", "galaxy", "gazebo", "gizmo", "glowworm", "gnarly", "gnostic", "gossip", "haiku", "hyphen", "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice", "jawbreaker", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", "joking", "joyful", "juicy", "jukebox", "jumbo", "kayak", "keyhole", "khaki", "kilobyte", "kiosk", "kitsch", "kiwifruit", "larynx", "lengths", "lucky", "luxury", "lymph", "marquis", "matrix", "megahertz", "microwave", "mystify", "nightclub", "nowadays", "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "peekaboo", "pixel", "pneumonia", "polka", "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quiz", "quizzes", "rhubarb", "rhythm", "rickshaw", "schnapps", "scratch", "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", "strengths", "stretch", "stronghold", "subway", "swivel", "syndrome", "topaz", "transcript", "transgress", "transplant", "twelfth", "twelfths", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka", "voodoo", "vortex", "walkway", "waltz", "wave", "wavy", "waxy", "wellspring", "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "wristwatch", "xylophone", "yachtsman", "yoked", "youthful", "yummy", "zephyr", "zigzag", "zilch", "zipper", "zodiac"]

continue_game = True

def generate_word(list=words):
    x = random.randint(0, (len(list)-1))
    return list[x]

def create_blanks(word):
    x = len(word)
    tab = []
    for i in range(x):
        tab += "_"
    return tab

def print_word(t):
    print (" ".join(t))

def print_letters_not_in_word(list):
    letter_list = ""
    for i in list:
        letter_list += i.upper() + ", "
    print("Letters not in word: " + letter_list[:-2])

def check_letter(l, word):
    indexes = []
    count = 0
    if word.find(l) != -1:
        for i in word:
            if l == i:
                indexes.append(count)
            count += 1
        return indexes
    else:
        print("Letter %s is not in word" %(l.upper()))
        return False

def game_over(incorrect, word):
    if incorrect >= 8:
        print("You lost the game")
        print(word)
        return True
    else:
        return False

def start_game():
    not_guessed = 0

new_game = True
continue_game = True

while(continue_game):
    if new_game == True:
        not_guessed = 0
        letters_not_in_word = []
        new_word = generate_word()
        guess = create_blanks(new_word)
        print_word(guess)
        letter = ""
        new_game = False
    while(letter.isalpha() == False or len(letter) != 1):
        print("Enter letter: ")
        letter = (input("> ")).lower()
    
    if check_letter(letter, new_word) != False:
        index = check_letter(letter, new_word)
        for i in index:
            guess[i] = letter.upper()
        print_word(guess)
    else:
        not_guessed += 1
        # if game_over(not_guessed, new_word) == True:
        #     break
        letters_not_in_word += letter
        print_letters_not_in_word(letters_not_in_word)
        print_word(guess)
    letter = ""
    
    continue_game = (game_over(not_guessed, new_word) != True) and ("_" in guess != False)
    if continue_game != True:
        print("Play Again (Y/N)")
        answer = (input("> ")).lower()
        if (answer == "y"):
            continue_game = True
            new_game = True
    
    

