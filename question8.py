import math
x,y = 0 , 0
up = int(input(" enter value of up : "))
down = int(input("enter  value of down : "))
left = int(input("enter value of  left : "))
right = int(input("enter value of right : "))
yy = y + up - down 
xx = x + right - left
a = xx-x
b = yy-y
d = math.sqrt(pow(a,a) + pow(b,b))
d = round(d)
print(d)