
def return_to_menu():
	ussd_code = eval(input('please type in your bank ussd code:'))
	Mainmenu()
print('Here is UBA Bank ussd code s\nZenith: *919#')
def Mainmenu():
	print('1.Airtme_self\n2.Airtime_self\n3.Transfer_UBA\n4.Transfer_Other Banks\n5.Transfer_UBA Prepaid\n6.Check Balance\n7.Pay Bills\n8.Next')
	option = eval(input("please select an option:"))
	if option == 1:
		print('Magic Banking please select an option below:')
		if option4 ==1:
			account=eval(input('1.enter pin\n2.O.main')
			print('invalid pin')
			print("Enter 00.Back \nEnter 0 to main")
			top = eval(input(':'))
			if top == 0:
				Mainmenu()
			elif top == 00:
				exit()
			else:
			print('Wrong input')
	elif option == 4:
		input = ('pin')
		Transfer = input('Please Enter Bank  Account Number Or Name Of beneficiary')
		amount = eval(input('Enter amont'))
		option = eval(input('receivers name'))
		print('send money',amount,'Naira to',Transfer,'\n1. YES\n2. NO')
		Assure_massage = eval(input(":"))
		if Assure_massage == 1:
			print('\n1. YES\n2.NO')
			exit()
			print("ENTER 0 TO RETURN TO MENU\nENTYER 00 TO GO BACK")
			top = eval(input(':'))
			if top == 0:
				return_to_main_menu()
			elif top == 00:
				back()
			else:
				print('Wrong input')
	elif option == 2:
		transfer = eval(input('1. For self\n2. For other'))
		if transfer == 2:
			print ('pin')
			amount = eval(input('Enter amount'))
			print('Transaction successifull')
		elif transfer == 2:
			amount = eval(input('Enter amount'))
			Phone_number = eval(input('enter destination name or phone number'))
			print(' ',('pin'),'\n1. yes\n2. No')
			Airtime_Assure_massage = eval(input(':'))
			if Airtime_Assure_massage == 1:
				print('rnter amount')
				print('Transaction successifull')
				print("ENTER 0 TO RETURN TO MAIN MENU \nENTYER 00 TO BACK")
				top = eval(input(':'))
				if top == 00:
					Mainmenu()
				elif top == 0:
					exit()
				else:
					print('Wrong input')
	elif option == 2:
		print('An SMS massage will be send to you shortly')
ussd_code = eval(input('please type in your bank ussd code:'))
if ussd_code == 919:
	bank = "UBA"
	Mainmenu()
else:
	Mainmenu()																					