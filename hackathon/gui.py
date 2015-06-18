#==========================
# Jay Gauvin
# Hackathon Project
#==========================

from tkinter import *
from tkinter import messagebox
import searcher
import indexer
import crawler
import ttk #python -m pip install pyttk

def create_gui():
	root = Tk()

	def about():
	   messagebox.showinfo("About", "Developed by Jay Gauvin. June 2015.")

	#refresh the data sources
	def run():
		result = messagebox.askquestion("Sources", "Refresh Data Sources?")
		if(result == "yes"):
			depth_limit = int(variable.get())
			searchProgress["maximum"] = depth_limit
			searchProgress["value"] = 0
			c = crawler.capture_data(str(domainBox.get()), depth_limit, "crawler.sqlite", searchProgress)
			d = indexer.index("crawler.sqlite", "keywords_shelve")
			searchProgress.stop()
			searchProgress["value"] = depth_limit
			
			searchlbl["text"] = "\nProcessed " + str(len(c)) + " sites. " + str(len(d)) + " search tokens found."
			
	def close():
		root.quit()

	menu = Menu(root)
	root.config(menu=menu)
	root.title("Search Engine Controls")
	root.minsize(350,150)
	root.maxsize(350,150)

	filemenu = Menu(menu)
	menu.add_cascade(label="File", menu=filemenu)
	filemenu.add_command(label="Exit", command=root.quit)

	helpmenu = Menu(menu)
	menu.add_cascade(label="Help", menu=helpmenu)
	helpmenu.add_command(label="About...", command=about)
	
	#textbox frame
	domainFrame = Frame(root)
	domainFrame.pack(anchor=W)
	domainlbl = Label(domainFrame, text="Root Domain:            ")
	domainlbl.pack(side = LEFT)
	domainBox = Entry(domainFrame, width=30)
	domainBox.pack(side = RIGHT)
	domainBox.insert(0, "www.newhaven.edu")
	
	#option frame
	optFrame = Frame(root)
	optFrame.pack(anchor=W)
	optionlbl = Label(optFrame, text="Crawler Page Limit: ")
	optionlbl.pack(side = LEFT)
	variable = StringVar(optFrame)
	variable.set("10") # default value
	w = OptionMenu(optFrame, variable, "1", "5", "10", "25", "50", "100", "500", "1000", "10000")
	w.pack(side = RIGHT)

	#search progress bar
	progFrame = Frame(root)
	progFrame.pack(anchor=W)
	progresslbl = Label(progFrame, text="Progress:                    ")
	progresslbl.pack(side = LEFT)
	searchProgress = ttk.Progressbar(progFrame, orient=HORIZONTAL, length=200, mode='determinate')
	searchProgress.pack(side=RIGHT)

	#search label
	searchlbl = Label(root, text="\nProcessed 0 sites. 0 search tokens found.")
	searchlbl.pack(side = TOP)

	#bottom buttons
	btnFrame = Frame(root)
	btnFrame.pack(side = BOTTOM)
	
	#run button
	button = Button(btnFrame, text="Run", command=run)
	button.config(width=10)
	button.pack(side = LEFT)

	#close button
	button = Button(btnFrame, text="Close", command=close)
	button.config(width=10)
	button.pack(side = RIGHT)
	
	mainloop()