# Copyright 2014 Sam Collins
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License

from time import strftime


def transaction(drink, cost, scost):
    global money
    print money
    print cost
    if money >= cost:
        money -= cost
        print 'You now have 1 ', drink
    else:
        print 'To buy a ', drink, ' you need', unichr(163), cost

    transfile = open('G:\PycharmProjects\Pi-Vending\Transactions.txt', 'a')
    transfile.write(strftime('\n[%Y-%m-%d %H:%M:%S] '))
    transfile.write('1 ' + drink + ' at ' + scost)
    transfile.close()
    print 'Anything else'
    # input('Press ENTER')


def addmoney():
    while True:
        global money
        print '1. 5p'
        print '2. 10p'
        print '3. 20p'
        print '4. 50p'
        print '5.', unichr(163), '1'
        print '6.', unichr(163), '2'
        coins = input('How much money ')

        if coins == 1:
            money += 0.05
            break
        elif coins == 2:
            money += 0.1
            break
        elif coins == 3:
            money += 0.2
            break
        elif coins == 4:
            money += 0.5
            break
        elif coins == 5:
            money += 1
            break
        elif coins == 6:
            money += 2
            break
        else:
            print 'Enter 1-6'
    print 'You now have', unichr(163), money


def buy():
    while True:
        if money >= 0.8:
            print 'You have', unichr(163), money
            print ''
            print 'The prices are:'
            print '1. Cola', unichr(163), '0.80'
            print '2. Fanta', unichr(163), '0.80'
            print '3. Lemonade', unichr(163), '0.80'
            print '4. Milkshake', unichr(163), '1.00'
            print '5. Water', unichr(163), '0.50'
            print '6. Quit'

            choice = input('What would you like to buy: ')
            print ''
            if choice == 1:
                transaction('Cola', 0.8, '0.80')
            elif choice == 2:
                transaction('Fanta', 0.8, '0.80')
            elif choice == 3:
                transaction('Lemonade', 0.80, '0.80')
            elif choice == 4:
                transaction('Milkshake', 1, '1.00')
            elif choice == 5:
                transaction('Water', 0.5, '0.50')
            elif choice == 6:
                break
        else:
            print 'You need more money to buy anything'
            break


print 'Welcome to the Py vending machine'
money = 100

while True:
    print ''
    print '1. Add money'
    if money >= 0.5:
        print '2. Buy drinks'
    else:
        print '2. Buy drinks (ADD MORE MONEY)'
    print '3. See balance'
    print '4. Quit'
    print ''

    choice = input('Choose your option ')
    print ''
    if choice == 1:
        addmoney()
    elif choice == 2:
        buy()
    elif choice == 3:
        print 'You have', unichr(163), money
    elif choice == 4:
        break

print 'Thanks for buying from SCollins'
print 'Goodbye'
print 'Sam'