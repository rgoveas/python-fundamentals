'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''

radius = float (3.14)

height = float (5)

Pi  = 3.14

#Volume of the cylinder and rounded to 2 decimal places

volume = Pi * radius**2 * height
volume = round(volume, 2)


# Area of the cylinder = 2πrh + 2πr**2 and rounded to 2 decimal places

surface_area = (2 * Pi * radius * height) + (2*Pi*radius**2)
surface_area = round(surface_area,2)


print("Volume of the cylinder : " , volume)

print("Surface area of the cylinder : ", surface_area)
