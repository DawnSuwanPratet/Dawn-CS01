from tkinter import *

root = Tk()
root.title("My First GUI")
myText = Label(text = "My name is", fg = "blue", font = 20).grid(row = 0, column = 0)
myText = Label(text = "Dawn", fg = "green", font = 20).grid(row = 1, column = 1)
myText = Label(text = "Suwanpratet", fg = "red", font = 20).grid(row = 2, column = 2)
root.geometry("300x300")
root.mainloop()