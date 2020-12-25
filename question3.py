""" comma accepting with sorting alphabetically 
"""

text = input("enter any sentence :").split(",") 
a=text.sort()
print(a)
for words in a:
	print(words)
