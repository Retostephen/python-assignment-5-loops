

user_db = {
"reto": {"password": 1234, "balance": 5000, "is_verified": False},
"scholar": {"password": 5678, "balance": 4000, "is_verified": False,}
	}

print("""
Welcome!
Login or Register
""")

verification_amount = 1500

user_input = input("Do you want to Login or Register: ")
user_input_lower = user_input.lower()

if user_input_lower == "login":
	username = input("Enter your username: ")
	if username in user_db:
		password = int(input("Enter your password: "))
		if user_db[username]["password"] == password:
			print("Login successful")
			verification = input("Do you want to be verified? : ")
			verification_lower = verification.lower()
			if verification_lower == "yes":
				if user_db[username]["balance"] >= verification_amount:
					user_db[username]["balance"] -= verification_amount
					print("You are verified")
					user_db[username]["is_verified"] = True
					print(user_db[username])
				else:
					print("Insufficient Funds")
			else:
				print(user_db[username])
		else:
			print("Invalid Password")
	else:
		print("Username is not registered on our data base")

elif user_input_lower == "register":
	create_username = input("Enter Username: ")
	if create_username in user_db:
		print("Username already exist/taken")
	else:
		create_password = input("Enter your password: ")
		confirm_password = input("Confirm your password: ")
		if confirm_password == create_password:
#			length = len(confirm_password)
#			length_word = length * 2
#			star = length_word * "*"
			password = f"{confirm_password[0]}{confirm_password[-1]}"
			balance = float(input("Enter your balance: "))
			is_verified = False

			user_db.update({create_username: {
			"password": password,
			"balance": balance,
			"is_verified": is_verified
			}})

			print(user_db[create_username])

			verification = input("Do you want to be verified? 'Yes/No' : ")
			verification = verification.lower()
			if verification == "Yes":
				if user_db[create_username]["balance"] >= verfication_amount:
					user_db[create_username]["balance"] -= verification_amount
					user_db[create_username]["is_verfied"] = True
					print(user_db[create_username])
				else:
					print("Insufficient funds")
			else:
				print(user_db[create_username])
		else:
			print("Invalid Password")
else:
	print("Error, Invalid Syntax")

'''
users_db = {
"reto": {"password": 1234, "balance": 5000, "is_verified": False},
"scholar": {"password": 5678, "balance": 4000, "is_verified": False,}
	}	
command = input("Enter login or register: ")

# Your implementation here...
if command == 'login':
	user_name = input('Enter user name: ')
	password = input('Enter password: ')
	if user_name == users_db[0]['name'] and password == users_db[0]['password']:
		print(f'SUCCESSFUL LOGIN \n{users_db}')
	elif user_name == users_db[0]['name'] and password != users_db[0]['password']:
		print('WRONG PASSWORD')
	elif password == users_db[0]['password'] and user_name != users_db[0]['name']:
		print('INVALID USER NAME')
	else:
		print('INVALID INFORMATION!')	
elif command == 'register':
	user_name = input('Create a user name: ')
	create_password = input('Create a password: ')
	balance = float(input('Enter balance: '))
	is_verified = False
	if user_name == users_db[0]['name']:
		print('USERNAME ALREADY EXIST!')
	else:
		user2 = {'name': user_name ,'password': create_password , 'balance': balance , 'is_verified': is_verified}
		users_db.append(user2)
		print(user2)
		get_verified = input('Verification option\nverification cost 1500\nEnter yes/no accept/decline verification ')	
		if get_verified == 'yes':
			if balance >= verification_amount:
				user2.update({'is_verified': True })
				balance = balance - verification_amount
				user2.update({'balance': balance})
				print(f'LOGIN SUCCESSFUL\nYour account has been verified and this is your current status:\n{user2}')
			else:
				print(f'INSUFFICIENT FUND!\nLOGIN SUCCESSFUL\n{user2}')
		elif get_verified == 'no':
			print(f'REGISTRATION SUCCESSFUL:\n{user2}')
		else:
			print('INVALID OPTION!')
else:
	print('INVALID COMMAND!')
'''
