import math
print("This program returns area and circumference of a circle from supplied radius")
radius = float(input("Enter Radius: "))
area = math.pi * (radius**2)
circumference = 2 * math.pi * radius


    
print("The area is:",(round(area)))
print("The circumference is:",(round(circumference)))

