#calculate the area of a cirlce
#radius*radius*pie
def AreaOfCircle():
    pi=3.141592653
#1 get a radius
    radius=input("What is the radius?")
#2 calculate the area
    radius = float(radius)
    area=radius*radius*pi
#3 display the area
    print("The area of the circle is:",area)

AreaOfCircle()
