from datetime import datetime
import shelve

def search(shelve_name):

	print("Reading shelved data...")
	sh = shelve.open(shelve_name)
	dic = sh["dic"]
	sh.close()

	query=input("\nSearch Query:")
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
		operator = "AND"

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
		andlist.sort()
		results = andlist				

	for x in results:
		print(x)
		
	dt2 = datetime.now()
	print("\nExecution Time: " + str(dt2.microsecond - dt1.microsecond))