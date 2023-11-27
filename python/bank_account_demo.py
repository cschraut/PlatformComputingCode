from bank_account import BankAccount

account = BankAccount("002345", 1000)
print(account)
account.deposit(1000)
account.withdraw(500)
account.get_balance()
print(account)