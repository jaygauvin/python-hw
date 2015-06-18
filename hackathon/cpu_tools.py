#==========================
# Jay Gauvin
# Hackathon Project
#==========================
#CPU status
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
		print("\nAVAILABLE MEMORY:", self.mem.available)
		print("USED MEMORY:", self.mem.used)
		print("USED PERCENTAGE:", self.mem.percent)