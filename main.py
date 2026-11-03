# Libraries

import random
import tkinter as tk
from tkinter import Button, messagebox

# Root window parameters

root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("600x600")

# Global variables

opponentChoice = random.choice(["Rock", "Paper", "Scissors"])

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