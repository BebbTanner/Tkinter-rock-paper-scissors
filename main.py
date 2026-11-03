# Libraries

import tkinter as tk
from tkinter import Button, messagebox

# Root window parameters

root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("600x600")

# Global variables?

choices = ["Rock", "Paper", "Scissors"]

# Functions

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

def npcChoice(item_list):
    import random
    return random.choice(item_list)

opponentChoice = npcChoice(choices)

# Widgets

rockButton = tk.Button(root, text = "Rock", command = rockButtonClick)
scissorsButton = tk.Button(root, text = "Scissors", command = scissorsButtonClick)
paperButton = tk.Button(root, text = "Paper", command = paperButtonClick)
Label_1 = tk.Label(root, text = f" {opponentChoice}")

# Packing

rockButton.pack(pady = 20)
scissorsButton.pack(pady = 20)
paperButton.pack(pady = 20)
Label_1.pack(pady = 20)

# Function Calls

npcChoice(choices)

root.mainloop()