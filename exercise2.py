class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_number = 1731  # admission number initialization and privatized
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        else:
            print("Invalid deposit amount. Please enter a positive value.")
            return False

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                return True
            else:
                print("Insufficient funds.")
                return False
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")
            return False

    def check_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

# Example usage the bank processes
if __name__ == "__main__":
    # Create a new bank account
    account = BankAccount(1000)  # Initial balance of 1000

    # Display initial balance and account number
    print(f"Account Number: {account.get_account_number()}")
    print(f"Initial Balance: ${account.check_balance()}")

    # Perform some transactions
    account.deposit(500)
    print(f"Balance after deposit: ${account.check_balance()}")

    account.withdraw(200)
    print(f"Balance after withdrawal: ${account.check_balance()}")

    # Try to withdraw more than the balance
    account.withdraw(2000)

    # Try to deposit a negative amount
    account.deposit(-100)

    # Final balance
    print(f"Final Balance: ${account.check_balance()}")
