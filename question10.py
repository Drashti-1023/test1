m=6   
# Outer loop
for i in range(65,70):
    m=m-1
    # Inner loop 1 
    for j in range(m,1,-1):
        print(" ",end=" ")
    # Inner loop 2
    for k in range(65,i+1):
        print(chr(k),end=" ")
    # Inner loop 3
    for n in range(65,i):
        print(chr(n),end=" ")
    print()