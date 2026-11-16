# Libraries

import random
import customtkinter as ctk
from tkinter import *

# UI setup

root = ctk.CTk()
root.title("Rock, Paper, Scissors")
root.geometry("500x400")
root.configure(bg = "#a9a9a9")

navbar = ctk.CTkFrame(root, fg_color = "#2c3e50", height = 50)
navbar.pack(side = "top", fill = "x")
navbar.pack_propagate(False)
navContainer = ctk.CTkFrame(navbar, fg_color = "#2c3e50")
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

    opponentLabel.configure(text=f"Opponent choice: {random_choice}")

    return random_choice

# Player choice
def setChoice(playerChoice):
    userChoice.set(playerChoice)
    userLabel.configure(text=f"Player Choice: {userChoice.get()}",)

    currentChoice = userChoice.get()
    npcChoice = opponentChoice()
    result = determineWinner(currentChoice, npcChoice)

    updateScore(result)


# Scoring function
def updateScore(result):
    global playerScore,opponentScore

    if result == 'Opponent wins':
        opponentScore = opponentScore + 1
    
    elif result == 'You win':
        playerScore = playerScore + 1

    playerscoreLabel.configure(text=f"Player score: {playerScore}")
    opponentscoreLabel.configure(text=f"Opponent score: {opponentScore}")

    float(playerScore)
    float(opponentScore)
    ratio = playerScore / opponentScore

    ratioLabel.configure(text=f"W/L: {ratio:.2f}")

  

# Global variables

userChoice = ctk.StringVar()
playerScore = 0
opponentScore = 0



# Button Styling

btnStyles = {
    "bg": "#2c3e50",
    "fg": "white",
    "activebackground": "#34495e",
    "activeforeground": "white",
    "bd": 0,
    "padx": 10, 
    "font": ("Arial", 12, "bold"),
    "cursor": "hand2"
}

lblStyles = {
    "font":("Arial", 12),
    "bg": "#a9a9a9"
}



# Buttons

rockButton = ctk.CTkButton(
    navContainer, 
    text = "Rock", 
    command= lambda: setChoice("Rock"), 
)
rockButton.pack(
    side="left", 
    fill="y"
)

paperButton = ctk.CTkButton(
    navContainer, 
    text = "Paper", 
    command= lambda: setChoice("Paper"), 
)
paperButton.pack(
    side="left", 
    fill="y"
)

scissorsButton = ctk.CTkButton(
    navContainer, 
    text = "Scissors", 
    command= lambda: setChoice("Scissors"), 
)
scissorsButton.pack(
    side="left", 
    fill="y"
)



# Labels

userLabel = ctk.CTkLabel(
    root, 
    text=f"Make a choice {userChoice.get()}", 
)
userLabel.pack(padx = 10, pady=10)

opponentLabel = ctk.CTkLabel(
    root, 
    text=f"Waiting for player", 
)
opponentLabel.pack(
    padx=10, 
    pady=10
)

playerscoreLabel = ctk.CTkLabel(
    root, 
    text="Player Score: 0", 
)
playerscoreLabel.pack(
    padx = 10, 
    pady=10
)

opponentscoreLabel = ctk.CTkLabel(
    root, 
    text="Opponent Score: 0", 
)
opponentscoreLabel.pack(
    padx = 10, 
    pady=10
)

ratioLabel = ctk.CTkLabel(
    root, 
    text="W/L: "
    )
ratioLabel.pack(
    padx=10, 
    pady=10
)

# Function Calls

root.mainloop()