
# Q-21 Python Program to Convert Centimeters to Feet and Inches.

def cm_to_feet_and_inches(centi):
    feet = centi/30.48
    left_cm = centi % 30.48
    inch = left_cm/2.54
    return feet, inch
# def cm_to_inch(cm):
#     return inch
a = float(input("Enter Centimeter here: "))
feet, inch = cm_to_feet_and_inches(a)
# inch = cm_to_inch(a)
print("The Centimeter of", a, "is", feet, "Feet and", inch,"Inches.." )
# print("The Centimeter of", a, "is", inch, "Inch..")

