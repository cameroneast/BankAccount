class BankAccount:
    bank_title = "first bank"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        self.current_balance += amount

    def withdrawal(self, amount):
        if self.current_balance >= amount and not self.current_balance < self.minimum_balance:
            self.current_balance -= amount

    def print_customer_information(self):
        print("Bank Name: " + BankAccount.bank_title + "\nCustomer Name: " + self.customer_name + "\nCurrent Balance: " +
              str(self.current_balance) + "\nMinimum Balance: " + str(self.minimum_balance))


bank = BankAccount("Customer1", 100.00, 20.00)
print("Before method calls:\n")
bank.print_customer_information()

bank.deposit(100)
bank.withdrawal(20)
print("\nAfter method calls:\n")
bank.print_customer_information()