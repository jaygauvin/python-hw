#Jay Gauvin
#homework5
#modified unh_crawler.py code

import urllib.request
from urllib.error import  URLError
import re
import html
import os
import pickle

def visit_url(url, domain):
	global crawler_backlog
	global url_data
	dictionary = {}
	if(len(crawler_backlog)>100):
		return
	if(url in crawler_backlog and crawler_backlog[url] == 1):
		return
	else:
		crawler_backlog[url] = 1
		print("===================================================")
		print("Processing:", url)
	try:
		page = urllib.request.urlopen(url)
		code=page.getcode()
		if(code == 200):
			content=page.read()
			content_string = content.decode("utf-8")
			regexp_title = re.compile('<title>(?P<title>(.*))</title>')
			regexp_js_remove = re.compile('<script([^\'"]|"[^"]*"|\'[^\']*\')*?</script>')
			regexp_junk_remove= re.compile("{[A-z0-9'\\;:,\s-]+}{1,2}|{}|(\\[A-z0-9]+\\[A-z0-9]+)/g") #remove stuff inside {}
			regexp_body = re.compile('(<.*?>\\s*)+')
			
			regexp_url = re.compile("http://"+domain+"[/\w+]*")

			result = regexp_title.search(content_string, re.IGNORECASE)

			if result:
				title = result.group("title")
				print(title)
				print("===================================================")
			
			result = str(result)
			result = regexp_js_remove.sub(" ", content_string) #remove javascript
			result = regexp_body.sub(" ", result) #remove the tags < >
			result = regexp_junk_remove.sub(" ", result) #remove some junk
			result = result.replace("\'", "'").replace("\r\n", "").replace("{}","")
			result = html.unescape(result).encode("utf-8") #conver the &amp; stuff to regular chars
						
			if result:
				url_data.append((url, result))
				print(result)

			for (urls) in re.findall(regexp_url, content_string):
					if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
						crawler_backlog[urls] = 0
						visit_url(urls, domain)
	except URLError as e:
		print("error")

url_data = []
crawler_backlog = {}
seed = "http://www.newhaven.edu/"
crawler_backlog[seed]=0
	
def get_data(filename):

	visit_url(seed, "www.newhaven.edu")
	
	#read pickled data
	print("Reading File Data from: " + filename)
	p = open(os.path.join(os.getcwd(), filename), "br")
	file_list = pickle.load(p)
	p.close()
	
	file_list.extend(url_data)	
	
	#pickle it
	print("Storing File Data to: " + filename)
	p = open(os.path.join(os.getcwd(), filename), "bw")
	pickle.dump(file_list, p)
	p.close()
