""" write a program that accept number between 0 to 999 and give output in string represantaion of that inter in english 
"""
def number(n):
	dict = {'0':"zero" , '1':"one" , '2':"two" , '3':"three" , '4':"four" , '5':"five" , '6':"six" , '7':"seven" , '8':"eight" , '9':"nine"}
	return " ".join(map(lambda x : dict[x],str(n)))
	if  number(n) <= 9:
		print(number(n))
	else:
		print("invalid input")
n = 10
print(number(n))