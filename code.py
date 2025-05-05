import os
import tkinter as tk
from tkinter import *
def xor(input,key):
   return ''.join(chr(ord(char) ^ key) for char in input)


def fil():
   te1 = in1.get("1.0", "end-1c")
   text=en.get()
   with open(text,"w") as f:
      f.write(te1)

def gui():
   global en 
   global in1
   op=Tk()
   op.title("3amk")
   op.geometry("600x400")
   LB=tk.Label(op,text="enter your text value").pack()
   en=tk.Entry(op)
   en.pack()
   in1=tk.Text(op,font=("Arial",10),height=5, width=50)
   in1.pack()
   b1=tk.Button(op,text="clike",command=fil,width=30).pack()
   op.mainloop()
gui()