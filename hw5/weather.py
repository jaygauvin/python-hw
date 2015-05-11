#Jay Gauvin
#homework5

import urllib.request
import json
from pprint import pprint

def getWeather(search):
	try:
		page = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=" + search)
		content=page.read()
		content_string = content.decode("utf-8")
		json_data = json.loads(content_string)

		if(json_data["cod"] != "404"):
			print("Weather: " + json_data["weather"][0]["main"])
		#else:
			#print("Weather: " + json_data["message"])
	except:
		print("Server error retrieving weather.")