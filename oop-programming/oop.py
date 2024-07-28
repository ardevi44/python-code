# Person class just for fun

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello my name is {self.name} and I'm {self.age}")

# BackAccount class, to do bank operations


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active and (50 <= amount > 0):
            self.balance += amount
            print(f"{amount} have been deposited to your account. Current balance: {
                  self.balance}")
        else:
            print("Couldn't make deposits.")
            print(f"Balance: {self.get_balance()}")

        if not self.is_active:
            print("Acount deactivated.")

    def withdraw(self, amount):
        if not self.is_active:
            print("This account is inactive you couldn't withdraw")
            return
        if self.balance <= 50:
            print(
                f"This balance ${self.balance} is to low for withdraw, at least you should have $50, please make a deposit first")
            print(f"Balance: {self.get_balance()}")
            return
        if self.balance == 0:
            print("Has no money in your balance: ${self.balance}")
            return
        if amount > self.balance:
            print(f"The withdraw is to much")
            print(f"Balance: {self.get_balance()}")
            return

        if amount > 0:
            self.balance -= amount
            print(f"${amount} have been withdrawn to your account. Current balance: {
                self.balance}")

    def deactivate(self):
        self.is_active = False
        print(f"Account deactivated")

    def get_balance(self):
        return self.balance


person1 = Person("Ana", 30)
person2 = Person("Luis", 25)

# person1.greet()
# person2.greet()

account1 = BankAccount(person1.name, 30_000)
account2 = BankAccount(person2.name, 200_000)

account1.deposit(200)

account1.withdraw(600)
account1.withdraw(30000)  # I should cause an Error ...

account1.withdraw(29550)
account1.withdraw(29)

a = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
print(a)
