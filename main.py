from tkinter import *
from tkinter import Menu
from PIL import ImageTk, Image
import random

bomb = 10
size = 8
# close game
def close():
    window.destroy()

#difficulty
def beginner():
    global bomb, size
    bomb = 10
    size = 8
    start_game()

def inter():
    global bomb, size
    bomb = 40
    size = 16
    start_game()

def expert():
    global bomb, size
    bomb = 80
    size = 20
    start_game()

def custom():
    global bomb, size
    bomb = 10
    size = 8
    start_game()

# start game
def start_game():
    # field
    field = [[0] * (size+2) for i in range(size+2)]
    for i in range(size+2):
        for j in range(size+2):
            field[i][j] = 0
    # bomb
    for i in range(bomb):
        x = random.randint(1,size)
        y = random.randint(1,size)
        if field[x][y] == -1:
            i = i-1
        else:
            field[x][y] = -1
    # numbers
    kolvo = 0
    for i in range(1 , size+1):
        for j in range(1, size+1):
            if field[i-1][j-1] == -1:
                kolvo = kolvo + 1
            if field[i][j-1] == -1:
                kolvo = kolvo + 1
            if field[i+1][j-1] == -1:
                kolvo = kolvo + 1
            if field[i][j+1] == -1:
                kolvo = kolvo + 1
            if field[i-1][j+1] == -1:
                kolvo = kolvo + 1
            if field[i+1][j+1] == -1:
                kolvo = kolvo + 1
            if field[i-1][j] == -1:
                kolvo = kolvo + 1
            if field[i+1][j] == -1:
                kolvo = kolvo + 1
            field[i][j] = kolvo
            kolvo = 0
    # draw field

# window settings

window = Tk()
window['bg'] = '#bebebe'
window.title("Minesweeper")
window.geometry('400x600')

# menu

menu = Menu(window)
game = Menu(window)

# game menu
game = Menu(menu, tearoff=0)
menu.add_cascade(label = "Game", menu = game)

# settings game menu
game.add_command(label = "New Game", command = start_game)
game.add_command(label = "Pause")
game.add_separator()
game.add_command(label = "Best Record")
game.add_command(label = "Close", command  = close)

# options menu


options = Menu(window)
options = Menu(menu, tearoff=0)
menu.add_cascade(label="Options", menu = options)
options.add_command(label = "Beginner", command = beginner) # 8x8 and 10 bomb
options.add_command(label = "Intermediate", command = inter) #
options.add_command(label = "Expert", command = expert)
options.add_command(label = "Custom", command = custom)
# help menu

help = Menu(window)
help = Menu(menu, tearoff=0)
menu.add_cascade(label = "Help", menu = help)
help.add_command(label = "How to play")
window.config(menu = menu)

# canva
# canva
canvas = Canvas(window,width=300,height=500)
canvas.pack()
pilImage = Image.open("example.png")
image = ImageTk.PhotoImage(pilImage)
imagesprite = canvas.create_image(image=image)


window.mainloop()