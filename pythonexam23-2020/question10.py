number = int (input(" enter any number : "))
for i in range(0,number ):
	chr = 65
	for j in range(0,number - i):
		print (chr , end = " ")
	print(" ")