import turtle
obj = turtle.Turtle()
obj.speed(0)

def square():
	for i in range(4):
		obj.forward(100)
		obj.right(90)

for i in range (1000):
	square()
	obj.right(11)



