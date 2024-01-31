weight = float(input("What is your weight?: "))
unit = input("Transfer weight to kg type K or weight in lbs type L: ")
if unit.upper() == "L":
	converted = weight * 0.45
	print(converted)
else:
	converted = weight / 0.45
	print(converted)