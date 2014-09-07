choice = 0
loop = 1
money = 0
loopBuy = 1
addedMoney = 0

print "Welcome to the Py vending machine"

while loop == 1:
	print ""
	print "1. Add money"
	if money >= 0.8:
		print "2. Buy drinks"
	else:
		print "2. Buy drinks (You will not be able to buy anything untill you add some money)"
	print "3. See balance"
	print "4. Quit"
	print ""

	choice = input("Choose your option: ")
	print ""
	if choice == 1:
		addedMoney = input("How much money ")
		if addedMoney > 10:
			print "Sorry you cant have that much money"
		elif addedMoney <= 0:
			print "You much enter a positive number"
		else:
			money += addedMoney
			print "Money added"
			print "You now have", unichr(163),money

	elif choice == 2:
		loopBuy = 1
		while loopBuy == 1:			
			if money >= 0.8:
				choice = 0
				print "You have", unichr(163),money
				print "The prices are:"
				
				print ""
				print "1. Cola", unichr(163), "1.50"
				print "2. Fanta", unichr(163), "1.50"
				print "3. Lemonaid", unichr(163), "1.20"
				print "4. Milkshake", unichr(163), "1.60"
				print "5. Water", unichr(163), "0.80"
				print "6. Quit"
				
				choice = input("What would you like to buy: ")
				print ""
				if choice == 1:
					if money >= 1.5:
						money -= 1.5
						print "You now have 1 Cola"
					else: 
						print "To buy a Cola you need", unichr(163),"1.50"
				elif choice == 2:
					if money >= 1.5:
						money -= 1.5
						print "You now have 1 Fanta"
					else: 
						print "To buy a Fanta you need", unichr(163),"1.50"
				elif choice == 3:
					if money >= 1.2:
						money -= 1.2
						print "You now have 1 Lemonaid"
					else: 
						print "To buy a Lemonaid you need", unichr(163),"1.20"
				elif choice == 4:
					if money >= 1.6:
						money -= 1.6
						print "You now have 1 Milkshake"
					else: 
						print "To buy a Milkshake you need", unichr(163),"1.60"
				elif choice == 5:
					if money >= 0.8:
						money -= 0.8
						print "You now have 1 Water"
					else: 
						print "To buy Water you need", unichr(163),"0.80"
								
				if choice == 6:
					loopBuy = 0	
				elif money >= 50.8 :
					print ""
					print "Anything else"
					print ""

			else:
				print "You need more money to buy anything"
				loopBuy = 0


	elif choice == 3:
		print "You have", unichr(163),money
	elif choice == 4:
		loop = 0

print "Thanks for buying from SCollins"
print "Goodbye"