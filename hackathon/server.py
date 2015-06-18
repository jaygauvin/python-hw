#==========================
# Jay Gauvin
# Hackathon Project
#==========================
#wsgiref server

from wsgiref.simple_server import make_server
import weather
import sqlite3
import searcher
import html
import cpu_tools

#server base class
class Server:
	#initialize class with port
	@classmethod
	def __init__(self, port):
		self.port = port
		self.httpd = None

	# Starts the web server
	@classmethod
	def start_server(self):
		self.httpd = make_server('', self.port, self.server_engine)
		print("Serving on port " + str(self.port) + "...")
		self.httpd.serve_forever()

	#the server engine to override
	@classmethod
	def server_engine(self, environ, start_response):
		message=""
		status = '200 OK'
		headers = [('Content-type', 'html; charset=utf-8')]
		start_response(status, headers)

		message += '<!DOCTYPE html><html><body>'
		message += 'Server is running.'
		message += '</body></html>'
			
		return[bytes(message,'utf-8')]

	#parse post forms
	@staticmethod
	def post_form_vals(post_str):
		form_vals = {item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")}
		return form_vals

	#parse get forms
	@staticmethod
	def get_form_vals(get_str):
		form_vals = {item.split("=")[0]: item.split("=")[1] for item in get_str.split("&")}
		return form_vals

#search engine -- inherited class
class SearchEngine(Server):		
	#==========================================
	# HTML Search Engine.  Override base class
	#==========================================
	@classmethod
	def server_engine(self, environ, start_response):
		#print("ENVIRON:", environ)
		message=""
		status = '200 OK'
		headers = [('Content-type', 'html; charset=utf-8')]
		start_response(status, headers)

		message += '<!DOCTYPE html>'
		message += '<html>'
		message += '<body>'
		message += '<center>'
		message += "<h1>"
		message += '<font color="#71431A">P</font>'
		message += '<font color="#899D5E">o</font>'
		message += '<font color="#E4CA3C">o</font>'
		message += '<font color="#361600">h</font>'
		message += '<font color="#71431A">g</font>'
		message += '<font color="#A54631">l</font>'
		message += '<font color="#F09327">e</font>'
		message += "</h1>"
		message += "<h5>A search engine that doesn't stink too bad...</h5>"
		message += "<h5>Weather in New Haven: "
		message += weather.getWeather("new%20haven")
		message += "</h5>"
		message += '<form action="search" method="GET">'
		message += '<input type="text" name="query">'
		message += '<input type="submit" value="Search">'
		message += '</form>'
		message += '</center>'
		message += '</br>'
		message += '</br>'
		
		if(len(environ['QUERY_STRING'])>1):
			form_vals = Server.get_form_vals(environ['QUERY_STRING'])
			query = form_vals["query"]
			query = html.unescape(query) #convert %20,+, etc back to spaces
			query = query.replace("+", " ") #convert %20,+, etc back to spaces

			results = searcher.search(query)
			
			for i, link in enumerate(results):
				print("Result " + str(i + 1) + ": " + link)
				
				message += '<a href="' + link + '">' + link + '</a></br>'
				#get data_list from database.. the data text
				conn = sqlite3.connect("crawler.sqlite")
				cursor = conn.cursor()
				data_list = cursor.execute("SELECT data FROM crawler WHERE url='" + str(link) + "'")
				
				for row in data_list:
					description = row[0]; #website text
					searchedWords = query.split(" ")[0].lower() #first search token				
					index_start = description.lower().find(searchedWords) #find occurance of first token
					
					if(index_start == -1):
						message += description[:300] + "..."
					else:
						#bold the first word that it found as a match
						message += '<b>' + description[index_start:index_start+len(searchedWords)] + '</b>'
						message += description[index_start+len(searchedWords):index_start+300] + "..."
					
				conn.commit()
				conn.close()
				
				message += '</br>'
				message += '</br>'

		message += '</body>'
		message += '</html>'
			
		return[bytes(message,'utf-8')]

#server for the cpu web monitor
class ServerMonitor(Server):
	#==========================================
	# Server Monitor.  Override base class
	#==========================================
	@classmethod
	def server_engine(self, environ, start_response):
		#print("ENVIRON:", environ)
		message=""
		status = '200 OK'
		headers = [('Content-type', 'html; charset=utf-8')]
		start_response(status, headers)

		c = cpu_tools.CPU()
			
		message += '<head><meta http-equiv="refresh" content="1"></head>' #refresh
		message += "<body>"
		message += "<table width='40%' border=0>"
		message += "<tr bgcolor='#FF1ADB'>"
		message += "<td>BOOT TIME</td>"
		message += "<td>" + c.boot_time + "</td></tr>"
		message += "<tr><td>CPU UTILIZATION</td>"
		message += "<td><table border=0 width='100%'>"
		
		for i, cpu in enumerate(c.cpu_util):
			message += "<tr><td>CPU " + str(i + 1) + " </td><td bgcolor='#00FF00'> " + str(cpu) + "%</td></tr>"
		
		message += "</table></td></tr><tr bgcolor='#FF1ADB'>"
		message += "<td>AVAILABLE MEMORY</td><td>" + str(c.mem.available) + "</td></tr>"
		message += "<tr><td>USED MEMORY</td><td>" + str(c.mem.used) + "</td></tr>"
		message += "<tr bgcolor='#FF1ADB'><td>USED PERCENTAGE</td><td>" + str(c.mem.percent) + "</td></tr></table>"
		message += "</body>"
			
		return[bytes(message,'utf-8')]


def start_CPU_Server():
	x = ServerMonitor(8001)
	x.start_server()
	
def start_Search_Server():
	x = SearchEngine(8000)
	x.start_server()