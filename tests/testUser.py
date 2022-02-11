from utils.user import User
import unittest
import sys
import csv
import pathlib as pl

sys.path.append('..')

class TestUser(unittest.TestCase):

    def test_file_creation(self):

        data = ["aaabbb",111111,0]
        User.createUser(data)
        path = pl.Path("data.csv")
        self.assertEquals((str(path), path.is_file()), (str(path), True))

    def test_user_exists(self):

        data = ["aabbbb",111111,0]
        User.createUser(data)
        with open("data.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            users = []
            for row in reader:
                users.append(row)
            self.assertEqual(users[3][0], "aabbbb")
            self.assertEqual(users[3][1], "111111")
            self.assertEqual(users[3][2], "0")


if __name__ == '__main__':
	  unittest.main(verbosity=2)
