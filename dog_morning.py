#two layers of if

#ask user first question. store answer
x = input("You wake up. Do you want to potty or eat? Choose A or B\n")

#if x == A potty Go bother human to be let out
if x == "A":
	#Ask user if they want to go on walk. Y or N?
	y = input("Do you want to go for a walk? Y or N?\n")
	#if Y go on a walk and find a smell
	if y == "Y":
		print("You go on a walk and find a smell.")
	#elif N stay home and watch tv
	elif y == "N":
		print("You stay home and watch tv.")
	#else Please pick one

#elif x == B eat Go bother human for food
elif x == "B":
	#Ask if they want to go for walk. Y or N?
	y = input ("Do you want breakfast? Y or N?\n")
	#if Y go on a walk and potty
	if y == "Y":
		print("You bring you food bowl to your human.")
	#elif N stay home and watch tv and wet the floor
	elif y == "N":
		print("You stay home and watch tv hungry until you wet the floor.")
	#else Please pick one
#else #please make a choice


