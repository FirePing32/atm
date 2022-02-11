import unittest
import sys, csv

sys.path.append('..')

from utils.auth import Card, Atm
from unittest import mock

cardObj = Card()
atmObj = Atm()

class TestAuth(unittest.TestCase):

    def test_auth_menu_exit(self):

        with self.assertRaises(SystemExit) as testauth:
            with mock.patch('builtins.input', side_effect=[3]):
                assert cardObj.auth() == None
        assert testauth.exception.code == 0


    def test_setup_user(self):

        with open("data.csv", "w"):
            pass

        with self.assertRaises(SystemExit) as testauth:
            with mock.patch('builtins.input', side_effect=[2, "abcdcd", 111111, 4]):
                assert cardObj.auth() == None
        assert testauth.exception.code == 0

        with self.assertRaises(SystemExit):
            with mock.patch('builtins.input', side_effect=[2, "abcdcf", 11111, "abcdcf", 111111, 4]):
                assert cardObj.auth() == None
        assert testauth.exception.code == 0

        invalidCreds = {
            "abcdc": 11111,
            "abcdcs": "1111ba",
            "abcdcs": "1111112",
            "abcdc": 111111
        }

        for key, value in invalidCreds.items():
            with self.assertRaises(StopIteration):
                with mock.patch('builtins.input', side_effect=[2, key, value, "abcdcf", 111111, 4]):
                    assert cardObj.auth() == None


    def test_login_user(self):

        with open("data.csv", "w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["abcdcd",111111,0])

        with self.assertRaises(SystemExit) as testauth:
            with mock.patch('builtins.input', side_effect=[1, "abcdcd", 111111, 4]):
                assert cardObj.auth() == None
        assert testauth.exception.code == 0

        invalidCreds = {
            "abcdcd": 111112,
            "abcdcd": "1111ab",
            "aaabbbs": 111111
        }

        for key, value in invalidCreds.items():
            with self.assertRaises(SystemExit) as testauth:
                with mock.patch('builtins.input', side_effect=[1, key, value, "abcdcd", 111111, 4]):
                    assert cardObj.auth() == None
            assert testauth.exception.code == 0


if __name__ == '__main__':
	unittest.main(verbosity=2)
