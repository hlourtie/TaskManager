import tkinter as tk
from tkinter import *
from datetime import datetime
from time import *
import time
import datetime
# window = tk.Tk()
# window.title("TimeMaster")
# window.mainloop()
i = 0
records = []
class Timing(object):
	start = 0
	elapsed = 0
	date = ""
	def __init__(self,name):
		self.name = name
		self.date = datetime.datetime.now()
	def set_name(name):
		self.name = name
	def set_start(_):
		start = time.time()
	def set_elapsed(_):
		if elapsed != 0:
			elapsed += time.time() - self.start
		elapsed = time.time() - self.start
	def save_me(_):
		f.write("Customer: %s , date %d, total time %d", name, date, elapsed)

	
def add_time():
	txt = Entry(window, width=10)
	txt.grid(row = i, column = 0)
	records.append(Timing(txt.get))
	beginButton = tk.Button(window, text="Start", command= records[i].set_start)
	beginButton.grid(row = i, column = 1)
	stopButton = tk.Button(window, text="Stop", command= records[i].set_elapsed)
	stopButton.grid(row = i, column = 2)
	saveButton = tk.Button(window, text="Save", command= records[i].save_me)
	saveButton.grid(row = i, column = 3)
	

f = open("Time.txt","w+")
window = tk.Tk()
window.title("TimeMaster")
bt = tk.Button(window,text = "Add", command = add_time)
bt.grid(sticky="s")
f.close()
window.mainloop()

	
