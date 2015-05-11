#JAY GAUVIN
#homework5

import os
import shutil
import fnmatch
import pickle

file_list = []

def get_traversal_data(filename):
	traverse_directory(os.path.join(os.getcwd(), "fortune1"))
	#pickle it
	print("Storing File Data to: Raw_Data.pickle")
	p = open(os.path.join(os.getcwd(), filename), "bw")
	pickle.dump(file_list, p)
	p.close()

def traverse_directory(path):
	l = os.listdir(path)
	for f in l:
		if os.path.isdir(os.path.join(path, f)):
			hp = os.path.join(path,f)
			traverse_directory(hp)
		elif fnmatch.fnmatch(os.path.join(path, f), "*.txt") or fnmatch.fnmatch(os.path.join(path, f), "*.log"):
			file = open(os.path.join(path, f), "r")
			content = file.read()
			t = (os.path.join(path, f), content)
			file_list.append(t)
			file.close()
			print("Added: " + str(os.path.join(path, f)))
		