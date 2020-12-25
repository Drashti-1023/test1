row = int(input("enter a number of rows : "))
column = int(input("enter a number of column : "))

matrix = []
rowwies = int(input("enter a entire matrix :"))
for i in range(row):
 	a = []
 	for j in range(column):
 		a.append((input()))
 	matrix.append(a)

for i in range(row):
 	for j in range(column):
 		print(matrix[i][j],end = " ")
 	print()
flag = True;

if (row != column):
	print("Matrix is invalid")
elif (row != column):
	for i in range(0,row):
		for j in range(0,column):
			if(a[i] == a[j]):
				print("true")
else:
	print("false")

				
