import unittest
import sys

sys.path.append('..')

from utils.account import Account
from unittest import mock

accountObj = Account("aaabbb", 111111)

class TestAccount(unittest.TestCase):

    def test_balance(self):
        self.assertEqual(accountObj.getBalance(), "0")

    def test_deposit(self):
        with mock.patch('builtins.input', side_effect=[-10, -5, 0, 15]):
            assert accountObj.depositMoney() == None
        self.assertEqual(accountObj.getBalance(), "15")

    def test_withdraw(self):
        with mock.patch('builtins.input', side_effect=[-10, -5, 0, 20, 5]):
            assert accountObj.withdrawMoney() == None
        self.assertEqual(accountObj.getBalance(), "10")

if __name__ == '__main__':
	  unittest.main(verbosity=2)
