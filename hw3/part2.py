#JAY GAUVIN
#HW3 Part 2
#Dictionaries

def count_frequency(list):
	dic = {}

	for item in list:
		key = item
		if(dic.get(key) == None):
			dic[key] = 1
		else:
			dic[key] = dic[key] + 1
		
	return dic

mylist=["one", "two", "eleven", "one", "three", "two", "eleven", "three", "seven", "eleven"]

print(count_frequency(mylist))