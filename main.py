# Libraries

import random
import tkinter as tk
from tkinter import Button

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

# Function

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

# Opponent choice?
def opponentChoice():
    choices = ["Rock", "Paper", "Scissors"]
    random_choice = random.choice(choices)

    #opponentLabel.config(text=f"Opponent: {random_choice}")
    print(f"NPC choice: {random_choice}")

    return random_choice

# Player choice?
def setChoice(playerChoice):
    userChoice.set(playerChoice)
    userLabel.config(text=f"Player Choice: {userChoice.get()}", font=("Arial", 12), bg="#f0f0f0")
    print(f"Player: {userChoice.get()}") 

    currentChoice = userChoice.get()
    npcChoice = opponentChoice()

    result = determineWinner(currentChoice, npcChoice)

    print(result)


# Global variables

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

userLabel = tk.Label(root, text=f"Make a choice: {userChoice.get()}", font=("Arial", 12), bg="#f0f0f0")
userLabel.pack(padx = 10, pady=10)

#opponentLabel = tk.Label(root, text=f"Opponent choice: {opponentChoice.get()}", font=("Arial", 12), bg="#f0f0f0")
#opponentLabel.pack(padx=10, pady=10)

#playerscoreLabel = tk.Label(root, text="Player Score: ", font=("Arial", 12), bg="#f0f0f0")
#playerscoreLabel.pack(padx = 10, pady=10)

#opponentscoreLabel = tk.Label(root, text="Opponent Score: ", font=("Arial", 12), bg="#f0f0f0")
#opponentscoreLabel.pack(padx = 10, pady=10)

# Function Calls

root.mainloop()