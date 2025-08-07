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

if user_input_lower == "Login":
	username = input("Enter your username: ")
	if username in user_db:
		password = int(input("Enter your password: "))
		if user_db[username]["password"] == password:
			print("Login successful")
			verification = input("Do you want to be verified? : ")
			verification_lower = verification.lower()
			if verification_lower == "Yes":
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

elif user_input_lower == "Register":
	create_username = input("Enter Username: ")
	if create_username in user_db:
		print("Username already exist/taken")
	else:
		create_password = input("Enter your password: ")
		confirm_password = input("Confirm your password: ")
		if confirm_password == create_password:
			length = len(confirm_password)
			length_word = length * 2
			star = length_word * "*"
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
			if verifcation == "Yes":
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

