#==========================
# Jay Gauvin
# Hackathon Project
#==========================
#modified unh_crawler.py code
#stores url and parsed content to data table: crawler (url, data)

import urllib.request
from urllib.error import  URLError
import re
import sqlite3
import ttk

url_data = []
crawler_backlog = {}
seed = ""
crawler_backlog[seed]=0

#==========================================
# Crawls through URLs
#==========================================
def visit_url(url, domain, depth_limit, progressbar):
	global crawler_backlog
	global url_data
	dictionary = {}
	
	if(url.endswith("/")):
		url = url[:len(url) - 1]
	
	if(len(crawler_backlog) > depth_limit):
		return
	if(url in crawler_backlog and crawler_backlog[url] == 1):
		return
	else:
		crawler_backlog[url] = 1
		print("===================================================")
		print("Processing:", url)
	try:
		#update progress bar
		progressbar.step(1.0)
		progressbar.update_idletasks()
		
		page = urllib.request.urlopen(url)
		code=page.getcode()
		if(code == 200):
			content=page.read()
			content_string = content.decode("ascii", "ignore")
			
			regexp_title = re.compile('<title>(?P<title>(.*))</title>')
			regexp_body = re.compile('<body[^>]*>(?P<body>([\s\S]*))<\/body>')
			regexp_url = re.compile("http://"+domain+"[/\w+]*")
		
			regexp_js_remove = re.compile('<script([^\'"]|"[^"]*"|\'[^\']*\')*?</script>') #remove javascript
			regexp_junk_remove= re.compile("{[A-z0-9'\\;:,\s-]+}{1,2}|{}|(\\[A-z0-9]+\\[A-z0-9]+)/g") #remove stuff inside {}
			regexp_text_remove = re.compile('(<.*?>\\s*)+|&[#A-z0-9]+;') #remove the tags < > and &amp; &nbsp; html encoding
			regexp_space_fix = re.compile('\s{2,}')

			result = regexp_title.search(content_string, re.IGNORECASE)

			if result:
				title = result.group("title")
				print(title)
				print("===================================================")
			
			result = regexp_body.search(content_string, re.IGNORECASE) #remove binary problems, get text within body tags

			if result:
				result = result.group("body")
				result = regexp_js_remove.sub(" ", result) #remove javascript
				result = regexp_text_remove.sub(" ", result) #remove the tags < >
				result = regexp_junk_remove.sub(" ", result) #remove some junk
				result = regexp_space_fix.sub(" ", result) #remove extra spaces
											
				if result:
					url_data.append((url, result))
					print(result)

			for (urls) in re.findall(regexp_url, content_string):
					if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
						crawler_backlog[urls] = 0
						visit_url(urls, domain, depth_limit, progressbar)
			
			return url_data
	except URLError as e:
		print("error")
		
#==========================================
# Creates index dictionary off of sql table.
#==========================================
def capture_data(domain, depth_limit, dbName, progressbar):
	conn = sqlite3.connect(dbName)
	cursor = conn.cursor()
	
	#initialize
	global url_data
	global crawler_backlog
	global seed
	
	url_data = []
	crawler_backlog = {}
	seed = ""
	crawler_backlog[seed]=0
	
	#get data
	data = visit_url("http://" + domain, domain, depth_limit, progressbar)
	
	#store data
	print("Creating SQL Database:")
	cursor.execute("DROP TABLE IF EXISTS crawler")
	cursor.execute("CREATE TABLE IF NOT EXISTS crawler (url text, data text)") #execute the create table query	
	cursor.executemany("INSERT INTO crawler (url, data) values(?, ?)", data)
	conn.commit()
	conn.close()
		
	print("Database Created.")
	
	return data