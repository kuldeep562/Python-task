
# Q-64. Python Program to Find the Gravitational Force between Two Objects

G = 6.674 * (10**-11)  


m1 = float(input("Enter the mass of the first object (in kg): "))
m2 = float(input("Enter the mass of the second object (in kg): "))
r = float(input("Enter the distance between the objects (in meters): "))


force = (G * m1 * m2) / (r**2)

print("The gravitational force between the two objects is: " ,force,"N")

