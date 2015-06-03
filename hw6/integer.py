#Jay Gauvin
#Integer Division
#6/3/15

from random import randrange

print("INTEGER DIVISIONS")
difficulty = 0
while(True):
	difficulty += 1
	a = randrange(5 + difficulty)
	b = randrange(5 + difficulty) #seed B
	
	#always have smaller divisior.  No fractions.
	while(b > a):
		b = randrange(5 + difficulty)
	
	answer = input(str(a) + "/" + str(b) + "=")
	
	try:
		answer = int(answer)
	except:
		print("Please enter Integers Only!")
	else:
		try:
			calculated_answer = a // b
		except ZeroDivisionError:
			calculated_answer = 0
		
		if(answer == calculated_answer):
			print("CORRECT")
		else:
			print("INCORRECT:", calculated_answer)
			