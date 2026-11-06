'''
    This now allows the user to make a choice and updates the NPC choice.
    Now I need to make it so that these two ansewrs get compared.
'''

# Libraries

import random
import tkinter as tk
from tkinter import Button

# Root window parameters

root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("600x600")
root.configure(bg = "#f0f0f0")

# Nav container

navbar = tk.Frame(root, bg = "#2c3e50", height = 50)
navbar.pack(side = "top", fill = "x")
navbar.pack_propagate(False)

# Nav Centering

navContainer = tk.Frame(navbar, bg = "#2c3e50")
navContainer.pack(expand = True, fill = "y")

# Global variables

opponentChoice = tk.StringVar(value = " none ")
userChoice = tk.StringVar(value="None Selected")

# Button Styling

btnStyles = {
    "bg": "#2c3e50",
    "fg": "white",
    "activebackground": "#34495e",
    "activeforeground": "white",
    "bd": 0,
    "padx": 20, 
    "font": ("Arial", 11, "bold"),
    "cursor": "hand2"
}

# Buttons

rockButton = tk.Button(navContainer, text = "Rock", command= lambda: setChoice("Rock"), **btnStyles)
rockButton.pack(side="left", fill="y")

paperButton = tk.Button(navContainer, text = "Paper", command= lambda: setChoice("Paper"), **btnStyles)
paperButton.pack(side="left", fill="y")

scissorsButton = tk.Button(navContainer, text = "Scissors", command= lambda: setChoice("Scissors"), **btnStyles)
scissorsButton.pack(side="left", fill="y")

# Labels

userLabel = tk.Label(root, text=f"Make a choice: {userChoice.get()}", font=("Arial", 14), bg="#f0f0f0")
userLabel.pack(expand=True)

opponentLabel = tk.Label(root, text=f"Opponent choice: {opponentChoice.get()}", font=("Arial", 14), bg="#f0f0f0")
opponentLabel.pack(expand=True)

# Function definitions

def setChoice(playerChoice):
    userChoice.set(playerChoice)
    userLabel.config(text=f"Player Choice: {userChoice.get()}", font=("Arial", 14), bg="#f0f0f0")
    print(f"User chose: {userChoice.get()}") 

    '''
        This is set in this function for now.
        I would like to put this in its own funcition eventually.
    '''
    random.seed()
    randomChoice = random.choice(["Rock", "Paper", "Scissors"])
    opponentLabel.config(text=f"Opponent Choice: {randomChoice}", font=("Arial", 14), bg="#f0f0f0")
    print(f"NPC choice: {randomChoice}")
    
# Function Calls

root.mainloop()