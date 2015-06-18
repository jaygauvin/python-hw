#==========================
# Jay Gauvin
# Hackathon Project
#==========================
#search the shelved preprocessed data

from datetime import datetime
import shelve
import sqlite3

#===================================================
# Searches the query words against the indexed data
#===================================================
def search(query):

	print("Reading shelved data...")
	sh = shelve.open("keywords_shelve")
	dic = sh["dic"]
	sh.close()

	query = query.strip().lower() #normalize, remove spacing, go to lower case
	tokens = query.split(" "); #parse into tokens by spaces
	results = []

	#find operator
	if "or" in tokens:
		if "and" in tokens:
			operator = "AND" #if user enters both 'and' and 'or', then 'and'
		else:
			operator = "OR"
	else:
		operator = "AND" #default operator
		
	#remove operator from tokens
	while("and" in tokens):
		tokens.remove("and")
	while("or" in tokens): 
		tokens.remove("or")

	#remove duplicates using a set
	unique_tokens = set()
	for x in tokens:
		unique_tokens.add(x)

	#=======================================
	print("Performing: " + operator + " search for: " + str(unique_tokens) + "\n")

	dt1 = datetime.now()
	if(operator == "OR"):
		bigset = set()
		biglist = []
		for x in unique_tokens:
			if dic.get(x) != None:
				bigset = set(bigset).union(set(dic[x])) #adding all the sets up to get a unique list of line numbers
		biglist = list(bigset)
		biglist.sort()
		results = biglist
	else:
		andlist = []
		for x in unique_tokens:				
			if dic.get(x) != None:
				newlist = []
				smlist = []
				if(len(andlist) == 0):
					andlist = list(dic[x]) #initialize the set from the first find.
				else:
					smlist = list(dic[x])
					#keep removing from the first found set.
					for j in smlist:
						if j in andlist:
							newlist.append(j)
					andlist = newlist
			else:
				andlist = [] #no result found for this one so no match
		andlist.sort()
		
		results = andlist				
		
	dt2 = datetime.now()
	print("\nExecution Time: " + str(dt2.microsecond - dt1.microsecond))

	return results
