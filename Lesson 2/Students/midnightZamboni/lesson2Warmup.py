import math
import time

def radius_of_circle():
    circumference = float (input ("Enter Circumference of Cirlce: "))
    radius = circumference/(2*math.pi)
    print (f"The radius of your circle is {radius:.2f}.")
    

    request = input("Would you like to calculate the volume of a cylinder of this radius? Yes or No ")
    if request == "Yes":
        height = float (input ("What is the height of your cylinder? "))
        roundRadius = round(radius,2)
        cylVol = math.pi*roundRadius*roundRadius*height
        #print(roundRadius)
        print(f"The volume of your circle is {cylVol:.2f}.")
        print("...")
        time.sleep(2)
        print("Goodbye.")

    else:
        print("Goodbye.")

radius_of_circle();