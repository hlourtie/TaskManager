import tkinter as tk
from tkinter import *
from datetime import datetime
from time import *
# window = tk.Tk()
# window.title("TimeMaster")
# window.mainloop()
int i = 0

class timing():
	def __init__(self,name,time):
		self.name = name
		self.time = time
		self.date = datetime.date(datetime.now())
	
	
def add_time():
	txt = Entry(window, width=10)
	txt.grid(row = i, column = 0)
	label
f = open("Time.txt","w+")
window = tk.Tk()
window.title("TimeMaster")
bt = tk.Button(window,text = "Add", command = add_time)
bt.pack(side = BOTTOM)
window.mainloop()

	
