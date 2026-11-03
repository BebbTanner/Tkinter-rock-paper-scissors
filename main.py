'''
    So I need to figure out how to switch the user's choice when the button is clicked how?
    So I think rather than having the userChoice variable inside of each function I should instead allow that functions to change the value of a global variable.
'''

# Libraries

import random
import tkinter as tk
from tkinter import Button, messagebox

# Root window parameters

root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("600x600")

# Global variables?

choices = ["Rock", "Paper", "Scissors"]
opponentChoice = random.choice(choices)

# Functions

def rockButtonClick():
    global userChoice
    userChoice = "Rock"
    messagebox.showinfo("Rock", "You chose " + userChoice)
    return userChoice

# Widgets

rockButton = tk.Button(root, text = "Rock", command = rockButtonClick)
Label_1 = tk.Label(root, text = f" {opponentChoice}")

# Packing

rockButton.pack(pady = 20)
Label_1.pack(pady = 20)

# Function Calls

root.mainloop()