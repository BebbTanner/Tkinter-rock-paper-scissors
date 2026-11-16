'''
    For the next steps I will be attempting to change the layout that way everything is not just stacked on top of each other.
'''

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

    totalGames = playerScore + opponentScore

    ratioLabel.configure(text=f"W/L: {ratio:.2f}")
    gamesPlayed.configure(text=f"Games played: {totalGames}")

  

# Global variables

userChoice = ctk.StringVar()
playerScore = 0
opponentScore = 0



# Button Styling

btnStyles = {
    "fg_color": "#2b8a3e",
    "text_color": "white",
    "hover_color":"#237032",
    "font": ("Arial", 12, "bold"),
    "cursor": "hand2"
}

lblStyles = {
    "font":("Arial", 18),
}



# Buttons

rockButton = ctk.CTkButton(
    navContainer, 
    text = "Rock", 
    command= lambda: setChoice("Rock"), 
    **btnStyles
)
rockButton.pack(
    side="left",
    padx=10, 
    pady=10
)

paperButton = ctk.CTkButton(
    navContainer, 
    text = "Paper", 
    command= lambda: setChoice("Paper"), 
    **btnStyles
)
paperButton.pack(
    side="left",
    padx=10, 
    pady=10
)

scissorsButton = ctk.CTkButton(
    navContainer, 
    text = "Scissors", 
    command= lambda: setChoice("Scissors"), 
    **btnStyles
)
scissorsButton.pack(
    side="left",
    padx=10, 
    pady=10
)



# Labels

userLabel = ctk.CTkLabel(
    root, 
    text=f"Make a choice {userChoice.get()}", 
    **lblStyles
)
userLabel.pack(
    padx = 10, 
    pady=10)


opponentLabel = ctk.CTkLabel(
    root, 
    text=f"Waiting for player", 
    **lblStyles
)
opponentLabel.pack(
    padx=10, 
    pady=10
)


playerscoreLabel = ctk.CTkLabel(
    root, 
    text="Player Score: 0",
    **lblStyles 
)
playerscoreLabel.pack(
    padx = 10, 
    pady=10
)


opponentscoreLabel = ctk.CTkLabel(
    root, 
    text="Opponent Score: 0", 
    **lblStyles
)
opponentscoreLabel.pack(
    padx = 10, 
    pady=10
)


ratioLabel = ctk.CTkLabel(
    root, 
    text="W/L: ",
    **lblStyles
)
ratioLabel.pack(
    padx=10, 
    pady=10
)

gamesPlayed = ctk.CTkLabel(
    root, 
    text="Games played: 0",
    **lblStyles
)
gamesPlayed.pack(
    padx=10, 
    pady=10 
)


# Function Calls

root.mainloop()