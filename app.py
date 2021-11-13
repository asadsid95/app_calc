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
button_clear = Button(root, text="Clear", padx = 20, pady=20)
button_add = Button(root, text="+", padx = 70, pady=20)
button_equal = Button(root, text="=", padx = 70, pady=20)

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



root.mainloop()