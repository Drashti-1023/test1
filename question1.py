#pattern printting


def pattern(n,m):
	num = 1



	for i in range(1,n+1):
		
		for j in range(1,m+1):
			if (  i == 1 or i==n or j ==1  or j==m):
				print(num,"*",end = " ")
				num = num + 1
			else:
				print(" ",end = " ")
		print(" ")
			
			
		
pattern(6,10)