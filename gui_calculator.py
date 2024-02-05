import tkinter as tk
from tkinter import *

m = tk.Tk() # m is the name of the main window object
m.title("GUI Calculator") # main window title



bt_frame_r1 = Frame(m)
bt_frame_r1.pack()
b8 = Button(bt_frame_r1, text = '7', fg = 'black', width='8', height='2',)
b8.pack(side = LEFT)
b8 = Button(bt_frame_r1, text = '8', fg = 'black', width='8', height='2')
b8.pack(side = LEFT)
b9 = Button(bt_frame_r1, text = '9', fg = 'black', width='8', height='2')
b9.pack(side = LEFT)
b_multiply = Button(bt_frame_r1, text = 'X', fg = 'black', width='8', height='2')
b_multiply.pack(side = LEFT)

bt_frame_r2 = Frame(m)
bt_frame_r2.pack()
b4 = Button(bt_frame_r2, text ='4', fg ='black', width='8', height='2')
b4.pack(side = LEFT)
b5 = Button(bt_frame_r2, text ='5', fg ='black', width='8', height='2')
b5.pack(side = LEFT)
b6 = Button(bt_frame_r2, text ='6', fg ='black', width='8', height='2')
b6.pack(side = LEFT)
b_subtract = Button(bt_frame_r2, text ='-', fg='black', width='8', height='2')
b_subtract.pack(side = LEFT)

bt_frame_r3 = Frame(m)
bt_frame_r3.pack()
b1 = Button(bt_frame_r3, text ='3', fg ='black', width='8',height='2')
b1.pack(side = LEFT)
b2 = Button(bt_frame_r3, text ='2', fg ='black', width='8',height='2')
b2.pack(side = LEFT)
b3 = Button(bt_frame_r3, text ='1', fg ='black', width='8',height='2')
b3.pack(side = LEFT)
b_plus = Button(bt_frame_r3, text='+', fg='black', width='8', height='2')
b_plus.pack(side = LEFT)

bt_frame_r4 = Frame(m)
bt_frame_r4.pack()
b_posneg = Button(bt_frame_r4, text ='+/-', fg ='black', width='8',height='2')
b_posneg.pack(side = LEFT)
b0 = Button(bt_frame_r4, text='0', fg='black', width='8', height='2')
b0.pack(side = LEFT)
b_point = Button(bt_frame_r4, text = '.', fg='black', width='8', height='2')
b_point.pack(side = LEFT)
b_equals = Button(bt_frame_r4, text='=', width='8', height='2')
b_equals.pack(side = LEFT)
# d1 = tk.Button(m, text="1", width="5", height="5", command=m.destroy, bg="black") 
# d1.pack()


m.mainloop()