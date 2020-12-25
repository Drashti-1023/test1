""" enter a password and check validations 
"""
import re
password = input ("enter your password :")
password.split(",")
def main():
	reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
	a = re.compile(reg)
	match = re.search(a,password)
	if match:
		print("password is valid")
	else:
		print("password is invalid")
if __name__ =='__main__':
	main()
