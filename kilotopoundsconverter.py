# Waratchaya Luangphairin
# 12/3/2018
# This program converts the values of pounds into kilograms

def convertToKilograms(pounds):
    # Pounds to Kilograms formula
    # kg = (lb / 2.205)

    kilograms = pounds / 2.205
    return kilograms

def main():

    lb = float(input("Enter a weight in pounds: "))
    lb2 = float(input("Enter a weight in pounds: "))
    lb3 = float(input("Enter a weight in pounds: "))
	
    kg = convertToKilograms(lb)
    kg2 = convertToKilograms(lb2)
    kg3 = convertToKilograms(lb3)
	
    print("Pounds		Kilograms")
    print(str(lb) + "         " + str(kg))
    print(str(lb2) + "         " + str(kg2))
    print(str(lb3) + "         " + str(kg3))


main()