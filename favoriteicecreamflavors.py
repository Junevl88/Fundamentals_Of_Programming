#Waratchaya (June)
#Oct 1 2018
#This program ask users for their favorite ice cream flavor and reacts according to the flavor in which user choose

def printFavorites():

	print("Here are  my top 6 Favorite Ice-cream flavors:")
	print("-----------------------------------------")
	print("1. Cookie dough")
	print("2. Rocky Road")
	print("3. Mint")
	print("4. Butter Pecan")
	print("5. Cookies and Cream")
	print("6. Chocolate")
	print("-----------------------------------------")


def main():

	x = input("What is your favorite ice cream flavor?")
	
	icecreamFlavors = ["Cookie Dough", "Rocky Road", "Mint", "Butter Pecan", "Cookies and Cream", "Chocolate"]
	
	if(x == "Cookie Dough"):
		print("Cookie dough is also my favorite flavor!")
		
	elif(x == "Rocky Road"):
		print("I like Rocky Road too!")
		
	elif(x == "Mint"):
		print("I like Mint too!")
		
	elif(x == "Butter Pecan"):
		print("I love Butter Pecan!")
		
	elif(x == "Cookies and Cream"):
		print("I like Cookies and Cream too!")
		
	elif(x == "Chocolate"):
		print("Chocolate sounds good right now!")
		
	else:
		print("Cool!")
	
	print(" ")
	
	printFavorites()

main()
