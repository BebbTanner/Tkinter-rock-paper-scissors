# Libraries

import random
import tkinter as tk
from tkinter import *

# UI setup

root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("500x400")
root.configure(bg = "#f0f0f0")

navbar = tk.Frame(root, bg = "#2c3e50", height = 50)
navbar.pack(side = "top", fill = "x")
navbar.pack_propagate(False)
navContainer = tk.Frame(navbar, bg = "#2c3e50")
navContainer.pack(expand = True, fill = "y")



# Functions

# Determine winner function
def determineWinner(player, opponent):
    if player == opponent:
        return "it's a tie"

    winningRule = {
        "Rock":"Scissors",
        "Scissors":"Paper",
        "Paper": "Rock"
    }

    if winningRule[player] == opponent:
        return "You win"
    else:
        return "Opponent wins"

# Opponent choice
def opponentChoice():
    choices = ["Rock", "Paper", "Scissors"]
    random_choice = random.choice(choices)

    opponentLabel.config(text=f"Opponent choice: {random_choice}")

    return random_choice

# Player choice
def setChoice(playerChoice):
    userChoice.set(playerChoice)
    userLabel.config(text=f"Player Choice: {userChoice.get()}", font=("Arial", 12), bg="#f0f0f0")

    currentChoice = userChoice.get()
    npcChoice = opponentChoice()
    result = determineWinner(currentChoice, npcChoice)

    playerScore = 0
    opponentScore = 0

    if result == 'Opponent wins':
        opponentScore = opponentScore + 1
    
    elif result == 'You win':
        playerScore = playerScore + 1

    playerscoreLabel.config(text=f"Player score: {playerScore}")
    opponentscoreLabel.config(text=f"Opponent score: {opponentScore}")



# Global variables

userChoice = tk.StringVar()



# Button Styling

btnStyles = {
    "bg": "#2c3e50",
    "fg": "white",
    "activebackground": "#34495e",
    "activeforeground": "white",
    "bd": 0,
    "padx": 20, 
    "font": ("Arial", 12, "bold"),
    "cursor": "hand2"
}

lblStyles = {
    "font":("Arial", 12)
}



# Buttons

rockButton = tk.Button(navContainer, text = "Rock", command= lambda: setChoice("Rock"), **btnStyles)
rockButton.pack(side="left", fill="y")

paperButton = tk.Button(navContainer, text = "Paper", command= lambda: setChoice("Paper"), **btnStyles)
paperButton.pack(side="left", fill="y")

scissorsButton = tk.Button(navContainer, text = "Scissors", command= lambda: setChoice("Scissors"), **btnStyles)
scissorsButton.pack(side="left", fill="y")



# Labels

userLabel = tk.Label(root, text=f"Make a choice {userChoice.get()}", **lblStyles)
userLabel.pack(padx = 10, pady=10)

opponentLabel = tk.Label(root, text=f"Waiting for player", **lblStyles)
opponentLabel.pack(padx=10, pady=10)

playerscoreLabel = tk.Label(root, text="Player Score: 0", **lblStyles)
playerscoreLabel.pack(padx = 10, pady=10)

opponentscoreLabel = tk.Label(root, text="Opponent Score: 0", **lblStyles)
opponentscoreLabel.pack(padx = 10, pady=10)



# Function Calls

root.mainloop()