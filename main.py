import random

def shuffle (string):
	tempList = list(string)
	random.shuffle(tempList)
	return ''.join(tempList)

# 9 Characters
u1=chr (random.randint(65,90))
u2=chr(random.randint(65,90))
n1=chr(random.randint(48,57))
l1=chr(random.randint(97,122))
u3=chr(random.randint(65,90))
n2=chr(random.randint(48,57))
n3=chr(random.randint(48,57))
l2=chr(random.randint(97,122))
n4=chr(random.randint(48,57))
password1 = u1+u2+n1+l1+u3+n2+n3+l2+n4
#/\/Additional Properties (For more options)/\/

#3 extra Characters(For 12 char)
l1=chr(random.randint(97,122))
u3=chr(random.randint(65,90))
n2=chr(random.randint(48,57))
n3=chr(random.randint(48,57))
password2 = l1+u3+n2+n3

#6 extra Characters(For 18 char)
l2=chr(random.randint(97,122))
n4=chr(random.randint(48,57))
n1=chr(random.randint(48,57))
u1=chr(random.randint(65,90))
u1=chr(random.randint(65,90))
u2=chr(random.randint(65,90))
n1=chr(random.randint(48,57))
password3 = l2+n4+n1+u1+u1+u2+n1

#Translation of password entries to options
option1 = password1
option2 = password1+password2
option3 = password1+password2+password3
option4 = password1+password3
option5 = password2+password3

#Shuffle process of password options
option1 = shuffle(password1)
option2 = shuffle(password1+password2)
option3 = shuffle(password1+password2+password3)
option4 = shuffle(password1+password3)
option5 = shuffle(password1+password2+password3+password3)

# def new_func():
#     return True
# ans=new_func()

#Interaction menu for users
menu1 = True
while menu1:
	print("LUCIUM Password Generator V1.0")
	print("""
	Option 1. A password generated with a set of 9 characters including uppercase and lowercase letters and numbers.
	Option 2. A password generated with a set of 12 characters including uppercase and lowercase letters and numbers.
	Option 3. A password generated with a set of 18 characters including uppercase and lowercase letters and numbers.
	Option 4. A password generated with a set of 15 characters including uppercase and lowercase letters and numbers.
	Option 5. A password generated with a set of 21 characters including uppercase and lowercase letters and numbers.
	----------------
	Option 6. Exit
	""")
	ans = str(input("Please choose your desired option to generate a random password."))
	
	if ans == "1":
		print("\n Your random password is:")
		print(option1)
		print("")
		print("")
		print("")
	elif ans == "2":
		print("\n Your random password is:")
		print(option2)
		print("")
		print("")
		print("")
	elif ans == "3":
		print("\n Your random password is:")
		print(option3)
		print("")
		print("")
		print("")
	elif ans == "4" or ans == "option 4":
		print("\n Your random password is:")
		print(option4)
		print("")
		print("")
		print("")
	elif ans == "5":
		print("\n Your random password is:")
		print(option5)
		print("\n")
		print("")
		print("")
	#elif ans == "6":
	# print("\n")
	#	print(menu2)
	#	print("\n")
	#	print("")
	elif ans == "6": 
		print("\n Exiting...GoodBye!")
		menu = False
	else:
		print("\n Choice invalid! Please try again")
		print("\n")


print("\n")
print("")
print("")
print("")
