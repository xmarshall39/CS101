
import math
import time

radius = input("please input the radius: ")
radius = float(radius) 

def area_of_circle():
    area = math.pi*pow(radius, 2) 
    print (f"the area is: {area:.2f}") 
    
def area_of_cylinder():
    hight = input ("let me know the hight: ")
    hight = float(hight)
    cArea = (2*math.pi*pow(radius, 2))+(2*math.pi*radius*hight)
    print (f"area of cylinder is: {cArea:.2f}")

area_of_circle()
time.sleep(1)
responce = input ("would you like to know the AREA of the cylinder? type yes \n")
if responce.lower() == "yes":
    area_of_cylinder()
else:
    print ("alright see you never")

#i was so confused why the second part wasnt running until i realized i just forgot to save 
#god this program