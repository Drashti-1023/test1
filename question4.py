a  = ( input ("enter any sentence :"))
d=l=0
for s in a:
	if s.isdigit():
		d=d+1
	elif s.isalpha():
		l=l+1
	else:
		pass
print("number of letter",l)
print("number of digit",d)