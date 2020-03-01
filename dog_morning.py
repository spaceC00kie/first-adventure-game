def question_one():
	x = input("You wake up in your human's bed because they love you way too much. Do you want to go potty or eat? Choose A or B\n")
	return x

def potty_or_eat(x):
	if x == "A":
		usr_ans = "A"
		#loop until usr_ans is Y or N
		while usr_ans != "Y" and usr_ans != "N":
			usr_ans = input("Do you want to go for a walk to do your businesss? Y or N?\n")
			if usr_ans == "Y":
				print("Your human takes you on a walk, you find a lot of smells, and you make some of your own. What a great day!")
			elif usr_ans == "N":
				print("Your human lets you into the yard to go potty then you come back inside. You're a pretty low energy dog so this is perfect for you.")
			else:
				print("You said you needed to go potty and you can't go in the house. So:")
	if x == "B":
		usr_ans = "B"
		#loop until usr_ans is Y or N
		while usr_ans != "Y" and usr_ans != "N":
			usr_ans = input ("Do you want to ask for breakfast like a good dog? Y or N?\n")
			if usr_ans == "Y":
				print("You bring you food bowl to your human. That's adorable, so your human feeds you immediately. It's a good morning and you are such a good dog!")
			elif usr_ans == "N":
				print("You stand by the food and bark at the containter. Your owner will not let you tell them what to do by barking. You'll have to wait a while to eat now. You'll figure it out eventually.")
			else:
				print("You said you wanted to eat. The question is this:")

x = question_one()

potty_or_eat(x)

