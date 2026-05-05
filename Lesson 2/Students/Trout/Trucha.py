import math
import time
#value = input("Please type a value: ")

def area_of_circle():
    radius = input("please input the radius: ")
    radius = float(radius)
    area = math.pi*pow(radius, 2)
    print (f" The area of this beautiful circle is {area:.2f}")

    cylinder_request = input("would you fuckin uhhh uhhh, idk like, turn this thing into a cylinder? Yes or No: ")
    if cylinder_request.lower() == "yes":

        height = input("please input the height of the cylinder: ")
        height = float(height)
        Cylinder_Area = (2 * (math.pi * radius * height)) + (2 * math.pi * pow(radius, 2))
        print (f"the height of this AWFUL cylinder is {Cylinder_Area:.2f}")
    else :
        print("fuck you")

area_of_circle() #OMG I DID IT LESFKING GO, by.... extensively ripping off zamboni's if and else code, but i am very proud of it cursing you off if you say no