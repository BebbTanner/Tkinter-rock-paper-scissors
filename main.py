'''
    I found a navbar example that I think would work really well for this program.
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

# Button Styling

rockButton = tk.Button(navContainer, text = "Rock", command= lambda: navigate("Rock"), **btnStyles)
rockButton.pack(side="left", fill="y")

paperButton = tk.Button(navContainer, text = "Paper", command= lambda: navigate("Paper"), **btnStyles)
paperButton.pack(side="left", fill="y")

scissorsButton = tk.Button(navContainer, text = "Scissors", command= lambda: navigate("Scissors"), **btnStyles)
scissorsButton.pack(side="left", fill="y")

# Function definitoins

'''
    I am keeping this in for now because I believe that I will be using it for the choice implmentation.
'''
def rockButtonClick():
    global userChoice
    userChoice = "Rock"
    messagebox.showinfo("Rock", "You chose " + userChoice)
    return userChoice

def navigate(page_name):
    contentLabel.config(text=f"You chose {page_name}")

# Function Calls

root.mainloop()