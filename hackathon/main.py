#==========================
# Jay Gauvin
# Hackathon Project
# ==> MAIN PROGRAM <==
# Requires: pyttk, psutil
#==========================
#hackaton
#main program
import threading
import gui
import server

#==========================================
# Main Program to call to start gui & server
#==========================================
def main():
	t1 = threading.Thread(target=gui.create_gui)
	t1.start()
	
	t2 = threading.Thread(target=server.start_Search_Server)
	t2.start()
	
	t3 = threading.Thread(target=server.start_CPU_Server)
	t3.start()
	
main()