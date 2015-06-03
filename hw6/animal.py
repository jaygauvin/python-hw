#Jay Gauvin
#Animal Program
#6/3/2015

class Animal:
	def __init__(self, type):
		self.type = type
		self.hint = []
		if(type == "elephant"):
			self.hint += ["I have exceptional memory"]
			self.hint += ["I am the largest land-living mammal in the world"]
			self.hint += ["I have a trunk for a nose"]
		elif(type == "tiger"):
			self.hint += ["I am the biggest cat"]
			self.hint += ["I come in black and white or orange and black"]
			self.hint += ["I have scary teeth and claws"]
		elif(type == "bat"):
			self.hint += ["I use echo-location"]
			self.hint += ["I can fly"]
			self.hint += ["I see well in dark"]
		
	def guess_who_am_i(self):
		print("\nI will give you 3 hints, guess what animal I am.")
		
		correct = False
		for i in range(0, 3):
			print(self.hint[i])
			guess = input("Who am I? ")
			if(guess == self.type):
				print("You got it! I am", self.type)
				correct = True
				break
			else:
				print("Nope, try again!")
				
		if(correct == False): print("I'm out of hints! The answer is:", self.type)



e = Animal("elephant")
t = Animal("tiger")
b = Animal("bat")

e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()