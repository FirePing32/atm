import logging
from .user import User
import csv
from .account import Account
import sys

logging.basicConfig(level=logging.NOTSET, format='%(message)s')


class Card:

    def __init__(self) -> None:
        pass

    def auth(self):
        """Authenticate the user"""
        print('1 - Login\n2 - Create Account\n3 - Exit')

        try:
            optionno = int(input("\nEnter option no: "))
            if optionno == 1:
                    self.login()
            elif optionno == 2:
                self.setupUser()
            elif optionno == 3:
                self.exitAtm()
            else:
                logging.warning("\nInvalid option number !")
                self.auth()

        except ValueError as e:
            logging.error(e)
            self.auth()

    def login(self):
        """Log in the user"""

        username = str(input("\nUsername: "))

        try:
            pin = int(input("PIN: "))
            userIds, keys = [], []
            with open("data.csv", 'r+') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    userIds.append(row[0])
                    keys.append(row[1])
            if username not in userIds:
                logging.error('\nAccount does not exist !')
                self.login()
            else:
                if int(keys[userIds.index(username)]) == pin:
                    atmObj.accountObj = Account(username, pin)
                    atmObj.displayCurrencyMenu()
                else:
                    logging.error('\nIncorrect Password !')
                    self.login()

        except ValueError as e:
            logging.error(e)
            self.login()

    def setupUser(self):
        """Creates a new user account"""

        try:
            username = str(input("\nUsername: "))
            pin = int(input("PIN: "))

            if len(username) < 6:
                logging.warning("\nUsername must be minimum 6 characters !")
                self.setupUser()

            elif len(str(pin)) != 6:
                logging.warning("\nPin must be of 6 integers only !")
                self.setupUser()

            else:
                data = [username, pin, 0]
                with open("data.csv", 'r+') as csvfile:
                    reader = csv.reader(csvfile)
                    userIds = [row[0] for row in reader]

                if username not in userIds:
                    addAcc = User.createUser(data)
                    print(addAcc, '\n')
                    atmObj.accountObj = Account(username, pin)
                    atmObj.displayCurrencyMenu()
                else:
                    logging.warning('\nUsername already exists !')
                    self.setupUser()

        except ValueError as e:
            logging.error(e)
            self.setupUser()

    def exitAtm(self):
        """Exit the ATM"""

        logging.info('\n----Thanks for using Swiss Bank----\n')
        sys.exit(0)


class Atm:

    accountObj = None

    def __init__(self) -> None:
        pass

    def displayCurrencyMenu(self):
        """Display the default menu when the user is logged in"""

        print("\n---Enter the required option number below---")
        print("\n1 - Deposit Money\n2 - Withdraw Money\n3 - View Balance\n4 - Log Out")

        try:
            optionno = int(input("\nEnter option no: "))
            if optionno == 1:
                self.accountObj.depositMoney()
                self.displayCurrencyMenu()
            elif optionno == 2:
                self.accountObj.withdrawMoney()
                self.displayCurrencyMenu()
            elif optionno == 3:
                self.accountObj.getBalance()
                self.displayCurrencyMenu()
            elif optionno == 4:
                self.accountObj.logOut()
            else:
                logging.warning("\nInvalid option number !")
                self.displayCurrencyMenu()
        except ValueError as e:
            logging.error(e)
            self.displayCurrencyMenu()

atmObj = Atm()
cardObj = Card()