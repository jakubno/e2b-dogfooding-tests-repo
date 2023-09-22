from bank import BankAccount


def test_bank_account():
    account = BankAccount(1000)

    account.deposit(500)
    assert account.get_balance() == 1500, f"Expected balance of 1500, but got {account.get_balance()}"

    account.withdraw(200)
    assert account.get_balance() == 1300, f"Expected balance of 1300, but got {account.get_balance()}"

    account.withdraw(2000)
    assert account.get_balance() >= 0, "Balance should not be negative"
