import csv


class User:

    def __init__(self) -> None:
        pass

    def createUser(data):
        """Register a new user"""

        with open('data.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)

        userPin = str(data[1])
        status = f"\nCreated account with username: {data[0]}\npin: {userPin[0]}XXX{userPin[4]}{userPin[5]}"
        return(status)
