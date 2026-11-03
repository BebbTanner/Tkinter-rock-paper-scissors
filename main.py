import tkinter as tk
from tkinter import Button, messagebox

'''
    Here are the parameters for the main window.
'''
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("600x306")

'''
    This is a set of buttons that will allow the user to select their choice.
'''
rockButton = tk.Button(root, text = "Rock")
scissorsButton = tk.Button(root, text = "Scissors")
paperButton = tk.Button(root, text = "Paper")

'''
    This are the pack fuctions. You must declare a pack method in order for those items to be displayed on the root windwow.
'''
rockButton.pack(pady = 20)
scissorsButton.pack(pady = 20)
paperButton.pack(pady = 20)

'''
    This function will run the main loop that currently just displays a blank window.
'''
root.mainloop()