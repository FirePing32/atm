import unittest
import sys
import csv

sys.path.append('..')

from utils.account import Account

accountObj = Account("aaabbb", 111111)

class TestAccount(unittest.TestCase):

    def test_balance(self):
        self.assertEqual(accountObj.getBalance(), "0")


if __name__ == '__main__':
	  unittest.main(verbosity=2)
