from tkinter import *
from tkinter.font import BOLD

root = Tk()
root.configure(background = "light grey")
root.title("pyCalc")

e = Entry(root, width = 50, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)
e.insert(0, "0")

def button_click(number):
    current = e.get()
    global s_num

    if current == "0":
        e.delete(0, END)
        e.insert(0, str(current) + str(number))
        e.delete(0, 1)
        new_current = e.get()
        s_num = int(new_current)
    else:
        e.delete(0, END)
        e.insert(0, str(current) + str(number))
        new_current = e.get()
        s_num = int(new_current)

def clear():
    e.delete(0, END)
    e.insert(0, "0")

def add():
    first_number = e.get()
    global data
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    data = []
    e.delete(0, END)

def subtract():
    first_number = e.get()
    global data
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    data = []
    e.delete(0, END)

def multiply():
    first_number = e.get()
    global data
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    data = []
    e.delete(0, END)

def divide():
    first_number = e.get()
    global data
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    data = []
    e.delete(0, END)

def equal():
    data.append(s_num)
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + data[0])
    if math == "subtraction":
        e.insert(0, f_num - data[0])
    if math == "multiplication":
        e.insert(0, f_num * data[0])
    if math == "division":
        e.insert(0, f_num / data[0])

button_1 = Button(root, text = "1", padx = 60, pady = 15, bg = "light grey", font = ("", 15), command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 60, pady = 15, bg = "light grey", font = ("", 15), command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 60, pady = 15, bg = "light grey", font = ("", 15), command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 60, pady = 15, bg = "light grey", font = ("", 15), command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 60, pady = 15, bg = "light grey", font = ("", 15), command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 60, pady = 15, bg = "light grey", font = ("", 15), command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 60, pady = 15, bg = "light grey", font = ("", 15), command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 60, pady = 15, bg = "light grey", font = ("", 15), command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 60, pady = 15, bg = "light grey", font = ("", 15), command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx = 60, pady = 15, bg = "light grey", font = ("", 15), command = lambda: button_click(0))
button_add = Button(root, text = "+", padx = 57, pady = 15, bg = "light grey", font = ("", 15), command = add)
button_subtract = Button(root, text = "-", padx = 59, pady = 14, bg = "light grey", font = ("", 16), command = subtract)
button_multiply = Button(root, text = "*", padx = 53, pady = 6, bg = "light grey", font = ("", 22), command = multiply)
button_divide = Button(root, text = "/", padx = 60, pady = 15, bg = "light grey", font = ("", 15), command = divide)
button_equal = Button(root, text = "=", padx = 59, pady = 14, bg = "light grey", font = ("", 16), command = equal)
button_clear = Button(root, text = "AC", padx = 51, pady = 14, bg = "light grey", font = ("", 16), command = clear)

button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)
button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)
button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)
button_0.grid(row = 4, column = 1)
button_add.grid(row = 3, column = 3)
button_subtract.grid(row = 4, column = 3)
button_multiply.grid(row = 2, column = 3)
button_divide.grid(row = 1, column = 3)
button_equal.grid(row = 4, column = 2)
button_clear.grid(row = 4, column = 0)

root.mainloop()