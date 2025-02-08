from tkinter import *
from math import *

def calculate():
    firstcol = entry1.get()
    secondcol = entry2.get()
    count = len(secondcol)
    square = count**2
    squareroot = sqrt(count)
    difference = round((square - squareroot),1)
    output_label.configure(text ='Character: {}, Word: {}, Count: {}, Square: {}, Squareroot: {}, Difference: {}'.format(firstcol,secondcol,count,square,squareroot,difference))
    entry1.delete(0,END)
    entry2.delete(0,END)

root = Tk()

message_label1 = Label(text='Enter a character [0-9][A-Z]: ',font=('Verdana', 16))
entry1 = Entry(font=('Verdana',16), width=1)
message_label2 = Label(text='Enter a word: ',font=('Verdana',16))
entry2 = Entry(font=('Verdana',16), width=50)
output_label = Label(font=('Verdana',16))
calc_button = Button(text='Process', font=('Verdana',16), command=calculate)

message_label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
message_label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
calc_button.grid(row=3, column=0)
output_label.grid(row=4, column=0, columnspan=3)

mainloop ()