'''
    So now that I somewhat have the layout that I want I need to figure out how to implement the functions of this page.
'''

# Libraries

import random
import tkinter as tk
from tkinter import Button, messagebox

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

opponentChoice = random.choice(["Rock", "Paper", "Scissors"])
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

label = tk.Label(root, text=f"Current choice: {userChoice.get()}")
label.pack(pady=5)

# Function definitions

'''
    I am keeping this in for now because I believe that I will be using it for the choice implmentation.

    I think that instead of the navigate function injected into the buttons.
    Instead of switching between pages I think that I need it to switch between variable choices instead.
    I am unsure of how to do that at this time.
'''

#def navigate(page_name):
#    contentLabel.config(text=f"You chose {page_name}")

def setChoice(choice_value):
    userChoice.set(choice_value)
    print(f"User chose: {userChoice.get()}") 
    label.config(text=f"Current Choice: {userChoice.get()}")

# Function Calls

root.mainloop()