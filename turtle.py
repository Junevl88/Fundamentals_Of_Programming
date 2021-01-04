import turtle

def main():

	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("~  Direction to move turtle")
	print("~  F: forward")
	print("~  B: backward")
	print("~  L: left")
	print("~  R: right")
	print("~  Q: Exit")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	
	#CREATE POOL	
	pool = turtle.Turtle()
	pool.color("paleturquoise")
	pool.pensize(2)
	
	pool.begin_fill()
	pool.circle(100)
	pool.end_fill()

	#CREATE TURTLE
	t = turtle.Turtle()
	t.color("darkseagreen")
	t.speed(10)
	t.shape("turtle")
	t.pensize(3)

choice = "-1"

while(choice != "Q"):
        choice = input("Let's move the turtle across the pool! Once you're done, press Q to exit")

        if(choice == "F"):
            t.forward(25)
        elif(choice == "B"):
            t.backward(25)
        elif(choice == "L"):
            t.left(90)
        elif(choice == "R"):
            t.right(90)
        elif(choice == "Q"):
            print("Thank you for drawing today.")
        else:
            print("Oops, an invalid option was picked. Please try again.")

main()