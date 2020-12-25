""" dictionary formate 
    get an interger number 
    suppose input is 8 and then 
    output must be 
    {1:1 , 2:8,3:9,4:16,5:25,6:36,7:49,8:64}
"""



num = int(input("enter a number : "))
dict = {}
for i in range(0,num):
	i = i + 1
	j = i *i
	print({i,j},end = " ") 