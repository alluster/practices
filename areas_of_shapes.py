#!/usr/bin/env python3

import math


def main():
	shape = input("Choose a shape (triangle, rectangle, circle):") 
	if not shape:
		quit()
	elif shape != "triangle" and shape !="rectangle" and shape != "circle":
		print("Unknown shape")	
		main()
	elif shape == "triangle":
		base = float(input("Give base of the triangle:"))
		height = float(input("Give height of the triangle:"))
		print(f"The area is {base * height / 2}")
		main()
	elif shape == "rectangle":
		width = float(input("Give width of the rectangle:"))
		height = float(input("Give height of the rectangle:")) 
		print(f"The area is {width * height}")
		main()	
	elif shape == "circle":
		radius = float(input("Give radius of the circle:"))
		print(f"The area is {radius**2 * math.pi}")
		main()
if __name__ == "__main__":
    main()
