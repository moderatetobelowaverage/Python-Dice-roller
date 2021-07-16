import tkinter as tk
from random import randint


root = tk.Tk()
root.geometry("200x200")
label = tk.Label(root, text="Amount of Sides")
entry = tk.Entry(root)
label2 = tk.Label(root, text='result: ')


def roll_dice():
    Number = entry.get()
    value = randint(1,int(Number))
    label2.configure(text="result: "+str(value))


button = tk.Button(root, text ='roll dice', command=roll_dice)


label.pack()
label2.pack()
button.pack()
entry.pack()
tk.mainloop()