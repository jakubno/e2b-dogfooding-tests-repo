"""Unit tests for the bank.py module."""

import unittest
from bank import BankAccount

class TestBankAccount(unittest.TestCase):

    def test_initial_balance(self):
        account = BankAccount(100)
        self.assertEqual(account.get_balance(), 100, 'Initial balance should be equal to the value passed in constructor.')

    def test_deposit(self):
        account = BankAccount(100)
        account.deposit(50)
        self.assertEqual(account.get_balance(), 150, 'Depositing 50 should increase balance to 150.')

    def test_withdraw(self):
        account = BankAccount(100)
        account.withdraw(50)
        self.assertEqual(account.get_balance(), 50, 'Withdrawing 50 should decrease balance to 50.')

if __name__ == '__main__':
    unittest.main()
