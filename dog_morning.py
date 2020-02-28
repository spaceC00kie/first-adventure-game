def question_one():
	x = input("You wake up. Do you want to go potty or eat? Choose A or B\n")
	return x

def potty_and_eat(x):
	if x == "A":
		usr_ans = "A"
		#loop until usr_ans is Y or N
		while usr_ans != "Y" and usr_ans != "N":
			usr_ans = input("Do you want to go for a walk? Y or N?\n")
			if usr_ans == "Y":
				print("Your human takes you on a walk, you find a lot of smells, and you make some of your own.")
			elif usr_ans == "N":
				print("You are let into the yard to go potty then you come back inside. You're a very low energy dog")
			else:
				print("Do you want to go on a walk? Pick Y or N.")
	if x == "B":
		usr_ans = "B"
		#loop until usr_ans is Y or N
		while usr_ans != "Y" and usr_ans != "N":
			usr_ans = input ("Do you want to ask for breakfast like a good dog? Y or N?\n")
			if usr_ans == "Y":
				print("You bring you food bowl to your human. That's adorable, so your human feeds you immediately. It's a good morning!")
			elif usr_ans == "N":
				print("You stand by the food and bark at the containter. Your owner will not let you tell them what to do by barking. You'll have to wait a while to eat now.")
			else:
				print("You said you wanted to eat. Are you a good dog or not?")

x = question_one()

potty_and_eat(x)

