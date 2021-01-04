# Waratchaya Luangphairin
# 11/26/2018
# This program shows what creating Attributes and Methods can do

class Superhero:
  def __init__(self, name = "", sidekick = "", villain = "", strengthPts = 0):
    self.name = name
    self.sidekick = sidekick
    self.villain = villain
    self.strengthPts = strengthPts
	
  def superherostrengthPts(self):
      if(self.strengthPts >1000):
          print("")
          print("Let me tell you about my Superhero.")
          print("His name is Captain Crunch and his power is to annihilate hunger by providing cereal to his people")
          print("When facing his villain," + self.villain + ", he shouts out his motto")
          print("Crunch away!! Along with his sidekick, " + self.sidekick + ", Captain Crunch defeated " + self.villain + "." )
          print("Sinister starve gets crushed with giant balls of cereal.")
          print(self.name + " now has " + str(self.strengthPts) + " points. That's over 1000 points!")
      else:
          print(self.name + " has " + str(self.strengthPts) + " points. Unlike Captain Crunch, he has less than 1000 points.")

def main():
	newSuperhero = Superhero("Captain Crunch", "lactose boy", "Sinister Starve", 1230)
	print("Name: " + newSuperhero.name)
	print("Sidekick: " + newSuperhero.sidekick)
	newSuperhero.superherostrengthPts()
	newSuperhero = Superhero("Mister Marshmallow", "kid cracker", "Cruel Cracker", 540)
	print(" ") # blank line
	#another bird using the same Superhero class
	print("Name: " + newSuperhero.name)
	print("Sidekick: " + newSuperhero.sidekick)
	newSuperhero.superherostrengthPts()
main()
