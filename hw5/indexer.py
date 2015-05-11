#Jay Gauvin
#homework5

from datetime import datetime
import pickle
import shelve

#==========================================
# Creates dictionary off of pickled file.
#==========================================
def process_datafile(file_name, shelve_name):
	print("\nPre-Processing...")
	dt1 = datetime.now()
	#dictionary list of words
	#each word has a set of line numbers
	
	f = open(file_name, "br")
	data_list = pickle.load(f)
	f.close()
	
	dic = {}
	for i in range(0, len(data_list)):
		t = data_list[i]
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
	
	return dic