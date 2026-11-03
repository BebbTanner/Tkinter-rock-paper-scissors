'''
    Ok so I need to make it so that the buttons actually do something rather than just being there.
'''

import tkinter as tk
from tkinter import Button, messagebox

'''
    Start of the function definitions for the buttons.
'''
def rockButtonClick():
    userChoice = "Rock"
    messagebox.showinfo("Rock", "You chose " + userChoice)
    return userChoice


def scissorsButtonClick():
    userChoice = "Scissors"
    messagebox.showinfo("Scissors", "You chose " + userChoice)

def paperButtonClick():
    userChoice = "Paper"
    messagebox.showinfo("Paper", "You chose " + userChoice)

'''
    This function will take an array as the argument and then return a random value from that array.
'''
def npcChoice(item_list):
    import random
    return random.choice(item_list)


'''
    Here are the parameters for the main window.
'''
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("600x306")

'''
    Here is the list of choices that the NPC is going to select from.
    I will take these and pass them off to the function that I have defined above.
'''
choices = ["Rock", "Paper", "Scissors"]

'''
    This is declaring a varible that will hold the random value "choice" that is randomly generated from the predefined list.
    It is then passing that off to the npcChoice function that should randomly select one of the three choices.
'''
opponentChoice = npcChoice(choices)

'''
    This is a set of buttons that will allow the user to select their choice.
    These are tied to commands that will run the functions defined when the user clicks on the buttons.
'''
rockButton = tk.Button(root, text = "Rock", command = rockButtonClick)
scissorsButton = tk.Button(root, text = "Scissors", command = scissorsButtonClick)
paperButton = tk.Button(root, text = "Paper", command = paperButtonClick)
Label_1 = tk.Label(root, text = f" {opponentChoice}")

'''
    This are the pack fuctions. You must declare a pack method in order for those items to be displayed on the root window.
    The items will be displayed in the order that they are packed.

    This bitch is not displaying the label that I have created.
'''
rockButton.pack(pady = 20)
scissorsButton.pack(pady = 20)
paperButton.pack(pady = 20)
Label_1.pack(pady = 20)

'''
    Dipshit you forgot to call the function.
    How is this supposed to do the thing if you don't call the got damned function.
    Ok so now I think I want to make it so that this function will not run until after the user has made their choice.

    Okay so here is where I am going to call of the fucntions that will need ran.
    If a funciton is updating something on the root window the function will need to be called before the root.mainloop() function...I think.
'''
npcChoice(choices)

'''
    This function will run the main loop that currently just displays a blank window.
'''
root.mainloop()