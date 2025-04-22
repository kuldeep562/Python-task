
# Q-55. Python Program to Find the Area of a Triangle
def triangle_area(base, height):
    area = 0.5 * base * height
    return area

base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))
area = triangle_area(base, height)

print("The area of the triangle is ",area)


