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

def scissorsButtonClick():
    userChoice = "Scissors"
    messagebox.showinfo("Scissors", "You chose " + userChoice)

def paperButtonClick():
    userChoice = "Paper"
    messagebox.showinfo("Paper", "You chose " + userChoice)

'''
    Here are the parameters for the main window.
'''
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("600x306")

'''
    This is a set of buttons that will allow the user to select their choice.
    These are tied to commands that will run the functions defined when the user clicks on the buttons.
'''
rockButton = tk.Button(root, text = "Rock", command = rockButtonClick)
scissorsButton = tk.Button(root, text = "Scissors", command = scissorsButtonClick)
paperButton = tk.Button(root, text = "Paper", command = paperButtonClick)

'''
    This are the pack fuctions. You must declare a pack method in order for those items to be displayed on the root windwow.
'''
rockButton.pack(pady = 20)
scissorsButton.pack(pady = 20)
paperButton.pack(pady = 20)

'''
    This function will run the main loop that currently just displays a blank window.
'''
root.mainloop()