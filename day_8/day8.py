import json
import os

accounts = []

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdrawal(self, amount):
        if amount > self.balance:
            return "Insufficient balance!"
        self.balance -= amount
        return f"Withdrew {amount}. New balance: {self.balance}"

    def __str__(self):
        return f"Owner: {self.name} - Balance: {self.balance}"

    def to_dict(self):
        return {"name": self.name, "balance": self.balance}


class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0.05):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest added: {interest:.2f}. New balance: {self.balance:.2f}"

    def __str__(self):
        return f"Savings Account | Owner: {self.name} - Balance: {self.balance} - Rate: {self.interest_rate}"


def save_to_json():
    data = [acc.to_dict() for acc in accounts]
    with open("accounts.json", "w") as f:
        json.dump(data, f, indent=4)
    return "Accounts saved to accounts.json"

def load_from_json():
    if not os.path.exists("accounts.json"):
        return "No saved data found."
    with open("accounts.json", "r") as f:
        data = json.load(f)
    for item in data:
        accounts.append(BankAccount(item['name'], item['balance']))
    return f"Loaded {len(data)} accounts."

def find_account(name):
    for acc in accounts:
        if acc.name == name:
            return acc
    return None

def main():
    print(load_from_json())
    while True:
        output = "1. Create Account\n2. Deposit\n3. Withdraw\n4. View Account\n5. View All\n6. Save & Exit"
        print(output)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            acc_type = input("Account type (basic/savings): ")
            if acc_type == "savings":
                accounts.append(SavingsAccount(name, balance))
            else:
                accounts.append(BankAccount(name, balance))
            print(f"Account created for {name}")
        elif choice == 2:
            name = input("Enter account holder name: ")
            acc = find_account(name)
            if acc:
                amount = float(input("Enter deposit amount: "))
                print(acc.deposit(amount))
            else:
                print(f"{name} not found.")
        elif choice == 3:
            name = input("Enter account holder name: ")
            acc = find_account(name)
            if acc:
                amount = float(input("Enter withdrawal amount: "))
                print(acc.withdrawal(amount))
            else:
                print(f"{name} not found.")
        elif choice == 4:
            name = input("Enter account holder name: ")
            acc = find_account(name)
            if acc:
                print(acc)
            else:
                print(f"{name} not found.")
        elif choice == 5:
            if accounts:
                for acc in accounts:
                    print(acc)
            else:
                print("No accounts found.")
        elif choice == 6:
            print(save_to_json())
            break
        else:
            print("Invalid choice. Please try again.")

main()