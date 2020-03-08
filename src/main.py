import tkinter as tk
from tkinter import *
from datetime import datetime
from datetime import time
from datetime import date
import time

# number of lines
class Lines(object):
	def __init__(self):
		self.value = 0
	def increment(self):
		self.value += 1


# Timing the object that contains the data that needs to be saved
def displaytime(tp, current_elapsed):
		temps = tp
		current_elapsed.config(text= temps)

class Timing(object):
	def __init__(self):
		self.name = ""
		self.elapsed = 0
		self.start = 0
		self.dat = date.today()
	def set_start(self, current_elapsed):
		self.start = time.time()
		current =  time.strftime('%H:%M:%S')
		displaytime(str(current), current_elapsed)
	def set_elapsed(self,total_elapsed, current_elapsed):
		if self.elapsed != 0:
			self.elapsed += (int)(time.time() - self.start)
		else:
			self.elapsed = (int)(time.time() - self.start)
		total_elapsed.config(text = str(self.elapsed))
	def save_me(self, txt):
		f = open("Time.txt","a")
		self.name = txt.get()
		time = self.elapsed 
		hour = (int) (time / 3600)
		minutes = (int) ((time % 3600) / 60)
		seconds =  (int) ((time % 3600) % 60)
		line = "Customer: "+ str(self.name) + " date: " + str(self.dat) + "  total time: " + str(hour) + ":" + str(minutes) + ":" + str(seconds)
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
	beginButton = tk.Button(window, text="Start", command=lambda: records[j].set_start(current_elapsed))
	beginButton.grid(row = j, column = 1)
	current_elapsed = Label(window)
	current_elapsed.grid(row=j, column=2)
	stopButton = tk.Button(window, text="Stop", command=lambda: records[j].set_elapsed(total_elapsed, current_elapsed))
	stopButton.grid(row = j, column = 3)
	total_elapsed = Label(window)
	total_elapsed.grid(row=j, column=4)
	saveButton = tk.Button(window, text="Save", command=lambda: records[j].save_me(txt))
	saveButton.grid(row = j, column = 5)
	i.increment()
	changed(i)

#main part that runs
i = Lines()
records = []
window = tk.Tk()
window.title("TimeMaster")
window.geometry("250x200")
bt = tk.Button(window,text = "Add", command =lambda: add_time(i), anchor=CENTER)
bt.grid(row= i.value +1, sticky=S)
window.mainloop()

	
