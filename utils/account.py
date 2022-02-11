import csv
import logging
import sys

logging.basicConfig(level=logging.NOTSET, format='%(message)s')

class Account:

    def __init__(self, username, pin):
        self.username = username
        self.pin = pin

    def depositMoney(self):
        """Deposit money to account"""

        try:
            amount = int(input("\nEnter amount to deposit: "))
            userIds, pins, balances = list(), list(), list()
            with open("data.csv", 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    userIds.append(row[0])
                    pins.append(int(row[1]))
                    balances.append(int(row[2]))

            if amount <= 0:
                logging.warn("\nAmount should be positive !")
                self.depositMoney()

            else:
                with open("data.csv", "w") as writefile:
                    writer = csv.writer(writefile)
                    csvdata = [[userIds[x], pins[x], balances[x]]
                            for x in range(len(userIds))]
                    currentBal = balances[userIds.index(self.username)] + amount
                    csvdata[userIds.index(self.username)][2] = currentBal
                    writer.writerows(csvdata)
                    logging.info(
                        f"\n----------\nAmount deposited: {amount}\nCurrent balance: {currentBal}\n----------")

        except ValueError as e:
            logging.error(e)
            self.depositMoney()

    def withdrawMoney(self):
        """Withdraw money from account"""

        try:
            amount = int(input("\nEnter amount to withdraw: "))
            userIds, pins, balances = list(), list(), list()
            with open("data.csv", 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    userIds.append(row[0])
                    pins.append(int(row[1]))
                    balances.append(int(row[2]))

            if amount <= 0:
                logging.warn("\nAmount should be positive !")
                self.withdrawMoney()

            elif amount > balances[userIds.index(self.username)]:
                logging.warn("\nInsufficient balance !")
                self.withdrawMoney()
            else:
                with open("data.csv", "w") as writefile:
                    writer = csv.writer(writefile)
                    csvdata = [[userIds[x], pins[x], balances[x]]
                            for x in range(len(userIds))]
                    currentBal = balances[userIds.index(self.username)] - amount
                    csvdata[userIds.index(self.username)][2] = currentBal
                    writer.writerows(csvdata)
                    logging.info(
                        f"\n----------\nAmount withdrawn: {amount}\nCurrent balance: {currentBal}\n----------")

        except ValueError as e:
            logging.error(e)
            self.withdrawMoney()

    def getBalance(self):
        """Returns balance of a particular card linked with an account"""

        with open("data.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == self.username:
                    logging.info(f"\n----------\nCurrent balance: {row[2]}\n----------")
                    return(row[2])

    def logOut(self):
        logging.info("\nLogging out...")
        sys.exit(0)
