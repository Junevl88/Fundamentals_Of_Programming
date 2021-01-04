import random
def main():
	
	# 0 = Rock
	# 1 = paper
	# 2 = scissor

	AI = random.randint(0,2)
	
	input("Let's play Rock, Paper, Scissors! (Press any key to continue)")
	print("Let's play Rock, Paper, Scissors!")
	
	print("")
	print("R is Rock")
	print("P is Paper")
	print("S is Scissors")
	print("")

	userInput = input("R is for Rock, P is for Paper, and S is for Scissors: What do you choose? (R/P/S)")
	
	print("You picked: " + userInput)
	
	#Tells what AI picked
	if(AI == 0):
		print("Your opponent picked: R")
	elif(AI == 1):
		print("Your opponent picked: P")
	elif(AI == 2):
		print("Your opponent picked: S")
	
	#rock
	if(AI == 0 and userInput == "R"):
		print("Tie")
	elif(AI == 0 and userInput == "P"):
		print("You Win!")
	elif(AI == 0 and userInput == "S"):
		print("You Lose!")

	#paper
	elif(AI == 1 and userInput == "R"):
		print("You Lose!")
	elif(AI == 1 and userInput == "P"):
		print("Tie")
	elif(AI == 1 and userInput == "S"):
		print("You Win!")
		
	#scissor
	elif(AI == 2 and userInput == "R"):
		print("You Win!")
	elif(AI == 2 and userInput == "P"):
		print("You Lose!")
	elif(AI == 2 and userInput == "S"):
		print("Tie")
	else:
		print("Invalid Input: Please input either R/S/P :)")
	
	print(AI)

main()