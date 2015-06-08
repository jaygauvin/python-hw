#Jay Gauvin
#CPU status with http server

from http.server import HTTPServer, BaseHTTPRequestHandler
import psutil, datetime

class CPU:
	boot_time = ""
	def __init__(self):
		self.boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
		self.cpu_util = psutil.cpu_percent(interval=1, percpu=True)

		i=1
		print("\nCPU UTILIZATION:")
		for cpu in self.cpu_util:
			print("CPU {} : {}%".format(i, cpu))
			i+=1

		self.mem = psutil.virtual_memory()
		THRESHOLD = 100 * 1024 * 1024  # 100MB
		print("\nAVAILABLE MEMORY:", self.mem.available)
		print("USED MEMORY:", self.mem.used)
		print("USED PERCENTAGE:", self.mem.percent)

class MyHTTPHandler(BaseHTTPRequestHandler):
	def do_GET(self):
	    self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
		c = CPU()
		message = ""
		with self.wfile as f:
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
			f.write(bytes(message,'utf-8'))
			f.close()
		return

server = HTTPServer(("", 8000), MyHTTPHandler)
print("Serving on port 8000...")
server.serve_forever()