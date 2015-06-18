#==========================
# Jay Gauvin
# Hackathon Project
#==========================
#reads from sql table to get crawled url and data
#stores the index in a shelved file

from datetime import datetime
import shelve
import sqlite3

#==========================================
# Creates index dictionary off of sql table.
#==========================================
def index(dbName, shelve_name):
	print("\nPre-Processing...")
	dt1 = datetime.now()
	#dictionary list of words
	#each word has a set of line numbers

	#get data_list from database
	conn = sqlite3.connect(dbName)
	cursor = conn.cursor()
	data_list = cursor.execute("SELECT url, data FROM crawler")
	
	dic = {}
	for row in data_list:
		t = row
		path = str(t[0])
		words = str(t[1]).split(" ")
		for word in words:
			word = word.replace(".", "").replace(",", "").lower() #clean up.
			if dic.get(word) == None:
				dic[word] = set() #add word to dictionary and create a set
				dic[word].add(t[0]) #add the line number to the set
			else:
				dic[word].add(t[0]) #add line number to the existing set
	dt2 = datetime.now()
	print("Execution Time: " + str(dt2.microsecond - dt1.microsecond))
	
	#store dictionary in db file
	print("Shelving pre-processed data...")
	sh = shelve.open(shelve_name)
	sh["dic"] = dic
	sh.close()

	conn.commit()
	conn.close()
	
	return dic