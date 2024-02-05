import tkinter as tk
from tkinter import *

m = tk.Tk() # m is the name of the main window object
m.title("GUI Calculator") # main window title
#m.geometry("320x300")

ent_input = Entry(m)
ent_input.grid(row=0,column=0)

fr_btn = Frame(m, borderwidth=1)
fr_btn.grid(row=1,column=0)
b7 = Button(fr_btn, text = '7', fg = 'black', width='8', height='2',)
b7.grid(row=1,column=0,padx=5, pady=5)
b8 = Button(fr_btn, text = '8', fg = 'black', width='8', height='2',)
b8.grid(row=1,column=1,padx=5, pady=5)
b9 = Button(fr_btn, text = '9', fg = 'black', width='8', height='2',)
b9.grid(row=1,column=2,padx=5, pady=5)
b_multiply = Button( fr_btn, text = 'x', fg = 'black', width='8', height='2')
b_multiply.grid(row=1,column=3,padx=5, pady=5)

b4 = Button(fr_btn, text ='4', fg ='black', width='8', height='2')
b4.grid(row=2,column=0,padx=5, pady=5)
b5 = Button(fr_btn, text ='5', fg ='black', width='8', height='2')
b5.grid(row=2,column=1,padx=5, pady=5)
b6 = Button(fr_btn, text ='6', fg ='black', width='8', height='2')
b6.grid(row=2,column=2,padx=5, pady=5)
b_subtract = Button(fr_btn, text ='-', fg='black', width='8', height='2')
b_subtract.grid(row=2,column=3,padx=5, pady=5)

b1 = Button(fr_btn, text ='1', fg ='black', width='8',height='2')
b1.grid(row=3,column=0,padx=5, pady=5)
b2 = Button(fr_btn, text ='2', fg ='black', width='8',height='2')
b2.grid(row=3,column=1,padx=5, pady=5)
b3 = Button(fr_btn, text ='3', fg ='black', width='8',height='2')
b3.grid(row=3,column=2,padx=5, pady=5)
b_plus = Button(fr_btn, text='+', fg='black', width='8', height='2')
b_plus.grid(row=3,column=3,padx=5, pady=5)

b_posneg = Button(fr_btn, text ='+/-', fg ='black', width='8',height='2')
b_posneg.grid(row=4,column=0,padx=5, pady=5)
b0 = Button(fr_btn, text='0', fg='black', width='8', height='2')
b0.grid(row=4,column=1,padx=5, pady=5)
b_point = Button(fr_btn, text = '.', fg='black', width='8', height='2')
b_point.grid(row=4,column=2,padx=5, pady=5)
b_equals = Button(fr_btn, text='=', width='8', height='2')
b_equals.grid(row=4,column=3,padx=5, pady=5)


m.mainloop()