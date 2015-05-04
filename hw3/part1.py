#JAY GAUVIN
#HW3 - PART 1
#RECURSIVE BUNNIES

#returns True if the number is odd.
def isOdd(value):
	if(value%2==0):
		return False;
	else:
		return True;

#0, 2, 5, 7, 10
def bunnyEars2(value):
	if(value == 0): 
		return 0
	elif(isOdd(value)):
		return bunnyEars2(value - 1) + 2
	else:
		return bunnyEars2(value - 1) + 3

lineNumber = int(input("What line position number?: "))
print("Total Ears: " + str(bunnyEars2(lineNumber)))