""" write a program that accept number between 0 to 999 and give output in string represantaion of that inter in english 
"""
number = int (input("enter any number :"))
if number >= 0 or number <= 999:
	print (number)
else:
	print("invalid input")