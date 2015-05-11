#Jay Gauvin
#homework5

# this is the main program

import searcher
import data_load
import indexer
import unh_crawler

traverse = input("Refresh Data Sources? (y/n): ")
if(traverse == "y"): 
	data_load.get_traversal_data("raw_data.pickle") #creates raw_data.pickle only need to run once.
	unh_crawler.get_data("raw_data.pickle") #appends data
	indexer.process_datafile("raw_data.pickle", "fortunes_shelve")
searcher.search("fortunes_shelve", "raw_data.pickle")
