'''
    This now allows the user to make a choice and updates the NPC choice.
    Now I need to make it so that these two ansewrs get compared.
'''

# Libraries

import random
import tkinter as tk
from tkinter import Button
import styles

# Root window parameters

root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("500x400")
root.configure(bg = "#f0f0f0")

# Nav container

navbar = tk.Frame(root, bg = "#2c3e50", height = 50)
navbar.pack(side = "top", fill = "x")
navbar.pack_propagate(False)

# Nav Centering

navContainer = tk.Frame(navbar, bg = "#2c3e50")
navContainer.pack(expand = True, fill = "y")

# Global variables

opponentChoice = tk.StringVar(value = "Waiting for player choice")
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

opponentLabel = tk.Label(root, text=f"Opponent choice: {opponentChoice.get()}", font=("Arial", 12), bg="#f0f0f0")
opponentLabel.pack(padx=10, pady=10)

playerscoreLabel = tk.Label(root, text="Player Score: ", font=("Arial", 12), bg="#f0f0f0")
playerscoreLabel.pack(padx = 10, pady=10)

opponentscoreLabel = tk.Label(root, text="Opponent Score: ", font=("Arial", 12), bg="#f0f0f0")
opponentscoreLabel.pack(padx = 10, pady=10)

# Function definitions

'''
    What are the two variables that we need to be comparing in order to determine the winner?
    I believe that it should be playerChoice and randomChoice.
'''
def setChoice(playerChoice):
    userChoice.set(playerChoice)
    userLabel.config(text=f"Player Choice: {userChoice.get()}", font=("Arial", 12), bg="#f0f0f0")
    print(f"User chose: {userChoice.get()}") 

    '''
        This is set in this function for now.
        I would like to put this in its own funcition eventually.
    '''
    random.seed()
    randomChoice = random.choice(["Rock", "Paper", "Scissors"])
    opponentLabel.config(text=f"Opponent: {randomChoice}", font=("Arial", 12), bg="#f0f0f0")
    print(f"NPC choice: {randomChoice}")

# Playing around with an example that I found
# I think that I can use these to create a frame to put items in, so that they can be side by side.
'''
rectangle_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rectangle_1.pack(ipadx=10, ipady=10, side="left", expand=True, fill="both")

rectangle_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rectangle_2.pack(ipadx=10, ipady=10, side="left", expand=True, fill="both")
'''

# Function Calls

root.mainloop()