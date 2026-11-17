'''
    2.0 branch
'''

# Libraries

import random
import customtkinter as ctk
from tkinter import *



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


  
# Function Calls

app = App()
app.mainloop()