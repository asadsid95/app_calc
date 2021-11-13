from tkinter import *

root = Tk()

# Create all buttons: 9 digits & 3 operations ( + = Clear )

input = Entry(root, width=30)
input.get()
input.pack()

button1 = Button(root, text="1")

button1.pack()

root.mainloop()