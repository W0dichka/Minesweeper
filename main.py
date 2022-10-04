from tkinter import *
from tkinter import Menu

# close game
def close():
    window.destroy()

# start game
def start_game():
    x =10



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
#TODO game.add_command(label = "New Game", command = start_game)
#TODO game.add_command(label = "Pause")
game.add_separator()

# difficulty game menu
#TODO game.add_command(label = "Beginner") # 8x8 and 10 bomb
#TODO game.add_command(label = "Intermediate") #
#TODO game.add_command(label = "Expert")
#TODO game.add_command(label = "Custom")
game.add_separator()
#TODO game.add_command(label = "Best Record")
game.add_separator()
game.add_command(label = "Close", command  = close)

# options menu


options = Menu(window)
options = Menu(menu, tearoff=0)
menu.add_cascade(label="Options", menu = options)

# help menu

help = Menu(window)
help = Menu(menu, tearoff=0)
menu.add_cascade(label = "Help", menu = help)

window.config(menu = menu)

# buttons
# smile = Button(window , text = "Start Game")
# smile.grid(column = 0, row = 0)


window.mainloop()