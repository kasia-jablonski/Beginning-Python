from tkinter import *
import random

words = ["zigzag", "zilch", "zipper", "zodiac"]
root = Tk()
root.title("Hangman game")

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
    return (" ".join(t))

new_word = generate_word()
not_guessed = 0
letters_not_in_word = []
guess = create_blanks(new_word)

label_word = Label(root, text = print_word(guess))
label_word.grid(row=0,column=0, columnspan=4)

label_not_guessed = Label(root, text="Letters not guessed: " + str(not_guessed) + " out of 8")
label_not_guessed.grid(row=8, column=0, columnspan=4)

def button_click(index, letter):
    globals()['button_A'].config(state = DISABLED)
# frame = Frame(root)
# frame.pack()

button_A = Button(root, text="A", padx=19.5, pady=10, command=lambda index=1: button_click(1, "a"))
button_B = Button(root, text="B", padx=20, pady=10, command=lambda: button_click("b"))
button_C = Button(root, text="C", padx=20, pady=10, command=lambda: button_click("c"))
button_D = Button(root, text="D", padx=20, pady=10, command=lambda: button_click("d"))
button_E = Button(root, text="E", padx=20, pady=10, command=lambda: button_click("e"))
button_F = Button(root, text="F", padx=21, pady=10, command=lambda: button_click("f"))
button_G = Button(root, text="G", padx=20, pady=10, command=lambda: button_click("g"))
button_H = Button(root, text="H", padx=19, pady=10, command=lambda: button_click("h"))
button_I = Button(root, text="I", padx=22, pady=10, command=lambda: button_click("i"))
button_J = Button(root, text="J", padx=22, pady=10, command=lambda: button_click("j"))
button_K = Button(root, text="K", padx=20, pady=10, command=lambda: button_click("k"))
button_L = Button(root, text="L", padx=20, pady=10, command=lambda: button_click("l"))
button_M = Button(root, text="M", padx=18, pady=10, command=lambda: button_click("m"))
button_N = Button(root, text="N", padx=19, pady=10, command=lambda: button_click("n"))
button_O = Button(root, text="O", padx=19, pady=10, command=lambda: button_click("o"))
button_P = Button(root, text="P", padx=20, pady=10, command=lambda: button_click("p"))
button_Q = Button(root, text="Q", padx=19, pady=10, command=lambda: button_click("q"))
button_R = Button(root, text="R", padx=20, pady=10, command=lambda: button_click("r"))
button_S = Button(root, text="S", padx=21, pady=10, command=lambda: button_click("s"))
button_T = Button(root, text="T", padx=20, pady=10, command=lambda: button_click("t"))
button_U = Button(root, text="U", padx=19, pady=10, command=lambda: button_click("u"))
button_V = Button(root, text="V", padx=20, pady=10, command=lambda: button_click("v"))
button_W = Button(root, text="W", padx=19, pady=10, command=lambda: button_click("w"))
button_X = Button(root, text="X", padx=20, pady=10, command=lambda: button_click("x"))
button_Y = Button(root, text="Y", padx=20, pady=10, command=lambda: button_click("y"))
button_Z = Button(root, text="Z", padx=20, pady=10, command=lambda: button_click("z"))

button_A.grid(row=1, column=0)
button_B.grid(row=1, column=1)
button_C.grid(row=1, column=2)
button_D.grid(row=1, column=3)

button_E.grid(row=2, column=0)
button_F.grid(row=2, column=1)
button_G.grid(row=2, column=2)
button_H.grid(row=2, column=3)

button_I.grid(row=3, column=0)
button_J.grid(row=3, column=1)
button_K.grid(row=3, column=2)
button_L.grid(row=3, column=3)

button_M.grid(row=4, column=0)
button_N.grid(row=4, column=1)
button_O.grid(row=4, column=2)
button_P.grid(row=4, column=3)

button_Q.grid(row=5, column=0)
button_R.grid(row=5, column=1)
button_S.grid(row=5, column=2)
button_T.grid(row=5, column=3)

button_U.grid(row=6, column=0)
button_V.grid(row=6, column=1)
button_W.grid(row=6, column=2)
button_X.grid(row=6, column=3)

button_Y.grid(row=7, column=0)
button_Z.grid(row=7, column=1)




root.mainloop()