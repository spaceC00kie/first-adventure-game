#defining switch
def first_choice (dogs_wish):
	switcher = {
		'A' : 'Go potty in the yard'
		'B' : 'Eat breakfast'
		'C' : 'Go on a walk'
	}
	return switcher.get(dogs_wish, "Please make a choice")

#game happens in this loop

is_game_over = False
while is_game_over ==False:
	#print original branching question with switch statement

	#first question
	is_first_wish_made = False
	while is_first_wish_made == False:
		poodle = input("Wish 1 - Pick A, B, or C")

		print(first_choice(poodle))

		#if the returned statement is "Please make a choice", reloop
		if x != "Please make a choice":
			is_first_wish_made = True

	#second question
	is_second_wish_made = False
	while is_second_wish_made == False
		schnauzer = input("Wish 1 - Pick A or B")
		if schnauzer == "y"