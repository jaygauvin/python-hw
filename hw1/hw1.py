#JAY GAUVIN
#HOMEWORK1
#PYTHON PROGRAMMING
#APRIL 10, 2015

#will accept yes, no, YES, NO, Y, N, y, n as inputs for yes/no questions.

play = True
name=input("Hi, What is your name? ")
print("Hello " + name + "! lets play a game!")

while(play == True):
	print("Think of a random number from 1 to 100, and I'll try to guess it!")
	max = 100
	min = 1
	count = 0

	while(True):
		guess = (max + min) // 2 #get the whole number (int)
		count = count + 1

		check = input("Is it " + str(guess) + "? (yes/no) ")
		if check.lower()[0] == 'y':
			print("Yeey! I got it in " + str(count) + " tries!")
			
			#loop for valid input so it won't crash on a blank
			#I didn't do this for all inputs, but this as an example 
			#to match your output
			while(True):
				more = input("Do you want to play more? ")
				if more.strip() != '':
					if more.lower()[0] == 'n':
						play = False
						print("Bye-bye")
					else:
						play = True
					break
			break

		check = input("Is the number larger than " + str(guess) + "? ")

		if check.lower()[0] == 'y':
			min = guess + 1
		else:
			max = guess - 1