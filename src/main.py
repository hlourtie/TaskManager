import tkinter as tk
from tkinter import *
from datetime import datetime
from time import *
import time
import datetime

# number of lines
class Lines(object):
	def __init__(self):
		self.value = 0
	def increment(self):
		self.value += 1


# Timing the object that contains the data that needs to be saved
class Timing(object):
	def __init__(self):
		self.name = ""
		self.elapsed = 0
		self.start = 0
		self.date = datetime.datetime.now()
	def set_start(self):
		self.start = time.time()
	def set_elapsed(self):
		if self.elapsed != 0:
			self.elapsed += (int)(time.time() - self.start)
		self.elapsed = (int)(time.time() - self.start)
	def save_me(self, txt):
		f = open("Time.txt","a")
		self.name = txt.get()
		line = "Customer: "+ str(self.name) + " date: " + str(self.date) + "  total time: " + str(self.elapsed)
		f.write(line)
		f.write("\n")
		f.close()

# changes the grid  position of the add button
def changed(i):
	bt.grid(row= i.value + 1, sticky=S)

# adds a line with all the button
def add_time(i):
	j = i.value
	txt = Entry(window, width=10)
	txt.grid(row = j, column = 0)
	records.append(Timing())
	beginButton = tk.Button(window, text="Start", command= records[j].set_start)
	beginButton.grid(row = j, column = 1)
	stopButton = tk.Button(window, text="Stop", command= records[j].set_elapsed)
	stopButton.grid(row = j, column = 3)
	saveButton = tk.Button(window, text="Save", command=lambda: records[j].save_me(txt))
	saveButton.grid(row = j, column = 5)
	i.increment()
	changed(i)

#main part that runs
i = Lines()
records = []
window = tk.Tk()
window.title("TimeMaster")
bt = tk.Button(window,text = "Add", command =lambda: add_time(i))
bt.grid(row= i.value +1, sticky=S)

window.mainloop()

	
