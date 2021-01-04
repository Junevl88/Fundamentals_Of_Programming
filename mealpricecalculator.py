#Waratchaya (June)
#8/31/2018
#This program calculates the total cost of a meal that includes an appetizer, entrée, drink, and dessert, with 6.5% tax and a 20% tip.
 
def main():
 
  print("Welcome to Chili's")
  print("")
 
  appetizer = input("what was your appetizer: ")
  appetizerC = float(input("What was the price of your appetizer: "))
 
  entree = input("what was your entree: ")
  entreeC = float(input("What was the price of your entree: "))
 
  drink = input("what was your drink: ")
  drinkC = float(input("What was the price of your drink: "))
 
  dessert = input("what was your dessert: ")
  dessertC = float(input("What was the price of your dessert: "))
 
  subtotal = appetizerC + entreeC + drinkC + dessertC
  
  tax = (subtotal * 0.065)
  tip = (subtotal * 0.2)
  orderTotal = subtotal + tax + tip
 
  print("your order: ")
  print("")
  print("Item                      Cost")
  print(str(appetizer)+"          	       " + str(appetizerC))
  print(str(entree)+"   	               " + str(entreeC))
  print(str(drink)+"                      " + str(drinkC))
  print(str(dessert)+"                      " + str(dessertC))
 
  print("------------------------------------")
 
  print("subtotal: " + "             $" + str(subtotal))
  print("tax: " + "                  $" + str(tax))
  print("Tip:" + "                   $" + str(tip))
  print("Order Total" + "            $" + str(orderTotal))
 
main()