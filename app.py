from tkinter import *

root = Tk()
root.title("Calculator")

# Create all buttons + input: 9 digits & 3 operations ( + = Clear ) + input

input = Entry(root, width=30)
input.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def b_click(number):
    # interesting method: assign input's value so far to a variable -> clear out input's value (since it's been saved -> save to input the old + new value
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(number))
    return

def b_clear():
    input.delete(0, END)

def b_add():
    first = input.get()
    global first_num
    global math
    math = 'add'
    first_num = int(first)
    input.delete(0, END)

def b_equal():
    second = input.get()
    input.delete(0, END)
    if math == 'add':
        input.insert(0, first_num + int(second))
    if math == 'subtract':
        input.insert(0, first_num - int(second))
    if math == 'multiply':
        input.insert(0, first_num * int(second))
    if math == 'divide':
        input.insert(0, first_num / int(second))

def b_subtract():
    first = input.get()
    global first_num
    global math
    math = 'subtract'
    first_num = int(first)
    input.delete(0, END)

def b_multiply():
    first = input.get()
    global first_num
    global math
    math = 'multiply'
    first_num = int(first)
    input.delete(0, END)

def b_divide():
    first = input.get()
    global first_num
    global math
    math = 'divide'
    first_num = int(first)
    input.delete(0, END)

# 0-9 digits' buttons; use of lambda func (takes many argument but has one expression)
button1 = Button(root, text="1",padx=30, pady=20,command=lambda: b_click(1))
button2 = Button(root, text="2",padx=30, pady=20,command=lambda: b_click(2))
button3 = Button(root, text="3",padx=30, pady=20,command=lambda: b_click(3))
button4 = Button(root, text="4",padx=30, pady=20,command=lambda: b_click(4))
button5 = Button(root, text="5",padx=30, pady=20,command=lambda: b_click(5))
button6 = Button(root, text="6",padx=30, pady=20,command=lambda: b_click(6))
button7 = Button(root, text="7",padx=30, pady=20,command=lambda: b_click(7))
button8 = Button(root, text="8",padx=30, pady=20,command=lambda: b_click(8))
button9 = Button(root, text="9",padx=30, pady=20,command=lambda: b_click(9))
button0 = Button(root, text="0",padx=30, pady=20,command=lambda: b_click(0))

# operations' buttons
button_clear = Button(root, text="Clear", padx = 19, pady=20, command=b_clear, background='gray')
button_add = Button(root, text="+", padx = 67, pady=20, command=b_add)
button_equal = Button(root, text="=", padx = 67, pady=20, command=b_equal)
button_subtract = Button(root, text="-", padx = 30, pady=20, command=b_subtract)
button_multiply = Button(root, text="*", padx = 30, pady=20, command=b_multiply)
button_divide = Button(root, text="/", padx = 30, pady=20, command=b_divide)

#adding buttons to screen


button7.grid(row= 1,column=0)
button8.grid(row= 1,column=1)
button9.grid(row= 1,column=2)

button4.grid(row= 2,column=0)
button5.grid(row= 2,column=1)
button6.grid(row= 2,column=2)

button1.grid(row= 3,column=0)
button2.grid(row= 3,column=1)
button3.grid(row= 3,column=2)

button0.grid(row= 4,column=0)
button_equal.grid(row=4, column=1, columnspan=2)

button_clear.grid(row=5, column=0)
button_add.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()