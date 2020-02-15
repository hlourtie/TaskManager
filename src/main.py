import tkinter as tk
from tkinter import *
# window = tk.Tk()
# window.title("TimeMaster")
# window.mainloop()
f = open("Time.txt","w+")
window = tk.Tk()
window.title("TimeMaster")
def add_time(window):
	txt = Entry(window, width=10)
	txt.pack(side = BOTTOM)

bt = tk.Button(window,text = "Add", command = add_time(window))
bt.pack(side = BOTTOM)
window.mainloop()

	
