#JAY GAUVIN
#HOMEWORK 4

# this is the main program

import searcher
import data_load
import indexer

traverse = input("Refresh/Traverse Data Files? (y/n): ")
if(traverse == "y"): 
	data_load.get_traversal_data() #creates raw_data.pickle only need to run once.
	dic = indexer.process_datafile("raw_data.pickle", "fortunes_shelve")
#dic = indexer.process_data(data_load.data_list) #the original process method
searcher.search("fortunes_shelve")
