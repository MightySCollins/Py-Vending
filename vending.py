# Copyright 2014 Sam Collins
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License

from time import strftime


def transaction(item, cost):
    transfile = open('C:/Users/Sam/PycharmProjects/Pi-Vending/Transactions.txt', 'a')
    transfile.write(strftime('[%Y-%m-%d %H:%M:%S] '))
    transfile.write(item)
    transfile.write(cost)
    transfile.close()


print 'Welcome to the Py vending machine'

money = 0
while True:
    print ''
    print '1. Add money'
    if money >= 0.8:
        print '2. Buy drinks'
    else:
        print '2. Buy drinks (You will not be able to buy anything until you add some money)'
    print '3. See balance'
    print '4. Quit'
    print ''

    choice = input('Choose your option: ')
    print ''
    if choice == 1:
        addedMoney = input('How much money ')
        if addedMoney > 10:
            print 'Sorry you cant have that much money'
        elif addedMoney <= 0:
            print 'You much enter a positive number'
        else:
            money += addedMoney
            print 'Money added'
            print 'You now have', unichr(163), money

    elif choice == 2:
        while True:
            if money >= 0.8:
                choice = 0
                print 'You have', unichr(163), money
                print 'The prices are:'

                print ''
                print '1. Cola', unichr(163), '1.50'
                print '2. Fanta', unichr(163), '1.50'
                print '3. Lemonade', unichr(163), '1.20'
                print '4. Milkshake', unichr(163), '1.60'
                print '5. Water', unichr(163), '0.80'
                print '6. Quit'

                choice = input('What would you like to buy: ')
                print ''
                if choice == 1:
                    if money >= 1.5:
                        money -= 1.5
                        print 'You now have 1 Cola'
                        transaction('Cola', '1.5')
                    else:
                        print 'To buy a Cola you need', unichr(163), '1.50'
                elif choice == 2:
                    if money >= 1.5:
                        money -= 1.5
                        print 'You now have 1 Fanta'
                    else:
                        print 'To buy a Fanta you need', unichr(163), '1.50'
                elif choice == 3:
                    if money >= 1.2:
                        money -= 1.2
                        print 'You now have 1 Lemonade'
                    else:
                        print 'To buy a Lemonade you need', unichr(163), '1.20'
                elif choice == 4:
                    if money >= 1.6:
                        money -= 1.6
                        print 'You now have 1 Milkshake'
                    else:
                        print 'To buy a Milkshake you need', unichr(163), '1.60'
                elif choice == 5:
                    if money >= 0.8:
                        money -= 0.8
                        print 'You now have 1 Water'
                    else:
                        print 'To buy Water you need', unichr(163), '0.80'

                if choice == 6:
                    break
                elif money >= 50.8:
                    print ''
                    print 'Anything else'
                    print ''

            else:
                print 'You need more money to buy anything'
                break

    elif choice == 3:
        print 'You have', unichr(163), money
    elif choice == 4:
        break

print 'Thanks for buying from SCollins'
print 'Goodbye'