from tkinter import *

root = Tk()
root.title("Calculator")

# Create all buttons + input: 9 digits & 3 operations ( + = Clear ) + input

input = Entry(root, width=30)
input.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def b_click(number):
    
    return

# 0-9 digits' buttons
button1 = Button(root, text="1",padx=30, pady=20,command=b_click)
button2 = Button(root, text="2",padx=30, pady=20,command=b_click)
button3 = Button(root, text="3",padx=30, pady=20,command=b_click)
button4 = Button(root, text="4",padx=30, pady=20,command=b_click)
button5 = Button(root, text="5",padx=30, pady=20,command=b_click)
button6 = Button(root, text="6",padx=30, pady=20,command=b_click)
button7 = Button(root, text="7",padx=30, pady=20,command=b_click)
button8 = Button(root, text="8",padx=30, pady=20,command=b_click)
button9 = Button(root, text="9",padx=30, pady=20,command=b_click)
button0 = Button(root, text="0",padx=30, pady=20,command=b_click)

# operations' buttons
button_clear = Button(root, text="Clear", padx = 19, pady=20)
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