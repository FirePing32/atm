# ATM

A class based ATM app to perform CRUD operations on a user account.

## Requirements

```bash
pip install -r requirements.txt
```

## Classes

- `utils.auth`
  - `Card()` - Authenticate the user
  - `Atm()` - Handle user input for performing relevant operations using the `Account()` class
- `utils.account.Account()` - Handle account related operations of a user
- `utils.user.User()` - Create new user account

## Unit Testing

Uses `unittest` to run tests.

```bash
cd tests && python -m unittest discover .
```
