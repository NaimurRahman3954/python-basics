# Area function of different shape
print("Enter the shape: ")
shape = input()
if shape == "triangle":
    print("Enter the base and height: ")
    base = int(input())
    height = int(input())
    area = (base*height)/2
    print("Area of triangle is: ", area)
elif shape == "rectangle":
    print("Enter the length and breadth: ")
    length = int(input())
    breadth = int(input())
    area = length*breadth
    print("Area of rectangle is: ", area)
elif shape == "circle":
    print("Enter the radius: ")
    radius = int(input())
    area = 3.14*radius*radius
    print("Area of circle is: ", area)
elif shape == "square":
    print("Enter the side: ")
    side = int(input())
    area = side*side
    print("Area of square is: ", area)
elif shape == "trapezium":
    print("Enter the base1 and base2 and height: ")
    base1 = int(input())
    base2 = int(input())
    height = int(input())
    area = ((base1+base2)/2)*height
    print("Area of trapezium is: ", area)
else:
    print("Invalid shape")
