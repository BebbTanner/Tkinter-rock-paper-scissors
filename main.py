'''
    Right now I am trying to convert the legacy layout to the new class based system layout.
    This should help with building out the layout that I actually want. 
    I am using the example that I uploaded earlier.

    I am slowly using my sanity with the conversion for this got damned app.
    Why do I continue to do this to myself?

    Ok so I got the layout of the UI set.
    Now the next step in the process is to start getting the functions and placing them on the window.

    Im thinking I might lift out the 2.0 variant to its own repo.
    This is starting to look rather messy and I think it would be better if I had these both seperated.
    Because with the 2.0 build I believe I am to the point where I am ready to start implementing the logic for the buttons.

    I have created a 2.0 branch for this repo.
    Now I want to go to the main branch and remove any of the 2.0 code from it.
'''

# Libraries

import random
import customtkinter as ctk
from tkinter import *

# Navbar Class
class Navbar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):

        kwargs.setdefault("fg_color","#2c3e50")
        kwargs.setdefault("height",50)
        kwargs.setdefault("corner_radius", 0)

        super().__init__(master, **kwargs)

        self.pack_propagate(False)

        self.navContainer = ctk.CTkFrame(self, fg_color="transparent")
        self.navContainer.pack(expand=True, fill="y")

        # --- Add your navbar buttons/labels inside self.nav_container below ---
        self.rockButton = ctk.CTkButton(self.navContainer, text="Rock", command= lambda: setChoice("Rock"), **btnStyles)
        self.rockButton.pack(side="left", padx=10, pady=10)

        self.paperButton = ctk.CTkButton(self.navContainer, text="Paper", command= lambda: setChoice("Paper"), **btnStyles)
        self.paperButton.pack(side="left", padx=10, pady=10)

        self.scissorsButton = ctk.CTkButton(self.navContainer, text="Scissors", command= lambda: setChoice("Scissors"), **btnStyles)
        self.scissorsButton.pack(side="left", padx=10, pady=10)



class frameOne(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure((0,1,2), weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.playerLabel = ctk.CTkLabel(self, text="Player Choice: ")
        self.playerLabel.grid(row=0, column=0, padx=10, pady=10)

        self.choiceLabel = ctk.CTkLabel(self, text="Make a choice")
        self.choiceLabel.grid(row=0, column=1, padx=10, pady=10)

        self.opponentLabel = ctk.CTkLabel(self, text="Opponent Choice: ")
        self.opponentLabel.grid(row=1, column=0, padx=10, pady=10)

        self.oppChoiceLabel = ctk.CTkLabel(self, text="Waiting for player")
        self.oppChoiceLabel.grid(row=1, column=1, padx=10, pady=10)



class frameTwo(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure((0,1,2), weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.playerLabel = ctk.CTkLabel(self, text="Player Score: ")
        self.playerLabel.grid(row=0, column=0, padx=10, pady=10)

        self.choiceLabel = ctk.CTkLabel(self, text="0")
        self.choiceLabel.grid(row=0, column=1, padx=10, pady=10)

        self.opponentLabel = ctk.CTkLabel(self, text="Opponent Score: ")
        self.opponentLabel.grid(row=1, column=0, padx=10, pady=10)

        self.oppChoiceLabel = ctk.CTkLabel(self, text="0")
        self.oppChoiceLabel.grid(row=1, column=1, padx=10, pady=10)



class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Rock, Paper, Scissors")
        self.geometry("500x400")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0,1), weight=1)

        self.navbar = Navbar(self)
        self.navbar.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.gameframe = frameOne(self)
        self.gameframe.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.scoreFrame = frameTwo(self)
        self.scoreFrame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")



root = ctk.CTk()
root.title("Rock, Paper, Scissors")
root.geometry("500x400")



navbar = ctk.CTkFrame(root, fg_color = "#2c3e50", height = 50)
navbar.pack(side = "top", fill = "x")
navbar.pack_propagate(False)
navContainer = ctk.CTkFrame(navbar, fg_color = "#2c3e50")
navContainer.pack(expand = True, fill = "y")



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

  

# Global variables
userChoice = ctk.StringVar()
playerScore = 0
opponentScore = 0



# Button Styling
btnStyles = {
    "fg_color": "#A73535",
    "text_color": "white",
    "hover_color":"#702323",
    "font": ("Arial", 12, "bold"),
    "cursor": "hand2"
}



# Label styling.
lblStyles = {
    "font":("Arial", 18),
}

# Function Calls

app = App()
app.mainloop()