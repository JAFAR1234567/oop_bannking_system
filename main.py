class Person:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class User(Person):
    def __init__(self, name, email, password, account_number):
        super().__init__(name, email, password)
        self.account_number = account_number
        self.balance = 0
        self.loan = 0
        self.transaction_history = []


class Admin(Person):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.bank = Bank()


class Bank:
    def __init__(self):
        self.users = {}
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def create_account(self, name, email, password):
        account_number = len(self.users) + 100
        user = User(name, email, password, account_number)
        self.users[account_number] = user
        return user

    def deposit(self, account_number, amount):
        user = self.users.get(account_number)
        if user:
            user.balance += amount
            self.total_balance += amount
        else:
            print("Invalid account number.")

    def withdraw(self, account_number, amount):
        user = self.users.get(account_number)
        if user:
            if user.balance >= amount:
                if user.balance >= amount and self.total_balance >= amount:
                    user.balance -= amount
                    self.total_balance -= amount
                else:
                    print("Bank is bankrupt! Unable to withdraw.")
            else:
                print(f"{user.name}'s acount has not enough money to withdraw.")    
        else:
            print("Invalid account number.")

    def check_balance(self, account_number):
        user = self.users.get(account_number)
        if user:
            return user.balance
        else:
            print("Invalid account number.")

    def transfer(self, sender_account_number, recipient_account_number, amount):
        sender = self.users.get(sender_account_number)
        recipient = self.users.get(recipient_account_number)
        if sender and recipient:
            if sender.balance >= amount:
                if sender.balance >= amount and self.total_balance >= amount:
                    sender.balance -= amount
                    recipient.balance += amount
                else:
                    print("Bank is bankrupt! Unable to transfer.")
            else: 
                print(f"{sender.name}'s acount has not enough money to send")       
        else:
            print("Invalid account numbers")

    def take_loan(self, account_number):
        user = self.users.get(account_number)
        if user:
            if self.loan_feature_enabled:
                loan_amount = 2 * user.balance
                user.loan += loan_amount
                self.total_loan_amount += loan_amount
                user.balance += loan_amount
                self.total_balance -= loan_amount
                return loan_amount
            else:
                print("Loan feature is disabled by the bank.")
        else:
            print("Invalid account number.")

    def admin_check_total_balance(self, admin):
        if isinstance(admin, Admin):
            return self.total_balance
        else:
            print("This operation is only available for admin.")

    def admin_check_total_loan_amount(self, admin):
        if isinstance(admin, Admin):
            return self.total_loan_amount
        else:
            print("This operation is only available for admin")

    def admin_enable_loan_feature(self, admin):
        if isinstance(admin, Admin):
            self.loan_feature_enabled = True
            print("Loan feature enabled.")
        else:
            print("This operation is only available for admin")

    def admin_disable_loan_feature(self, admin):
        if isinstance(admin, Admin):
            self.loan_feature_enabled = False
            print("Loan feature disabled.")
        else:
            print("Access denied. This operation is only available for admin")


bank = Bank()

# Create users account
user1 = bank.create_account("rahim", "rahim@gmail.com", 12345)
user2 = bank.create_account("karim", "karim@gmail.com", 5432)
user3 = bank.create_account("monir khan", "monir@gmail.com", 51232)

# Create admin
admin = Admin("admin", "admin@gmail.com", "admin123")

# Deposit money
bank.deposit(user1.account_number, 1000)
bank.deposit(user2.account_number, 1000)
bank.deposit(user3.account_number, 1000)

# Check account balance
print(f"{user1.name}'s account balance:", bank.check_balance(user1.account_number))
print(f"{user2.name}'s account balance:", bank.check_balance(user2.account_number))
print(f"{user3.name}'s account balance:", bank.check_balance(user2.account_number))
print()
bank.withdraw(user1.account_number, 500)
bank.withdraw(user2.account_number, 500)

# check blance after withdraw
print("blance after withdraw:")
print(f"{user1.name}'s account balance:", bank.check_balance(user1.account_number))
print(f"{user2.name}'s account balance:", bank.check_balance(user2.account_number))
print()
# Check account balance before taking a loan
# print(f"{user3.name}'s account balance before loan:",
#       bank.check_balance(user3.account_number))

# Take loan
loan_amount_user3 = bank.take_loan(user3.account_number)
print(f"{user3.name} has taken a loan of {loan_amount_user3}.")

# Check account balance after taking a loan
# print(f"{user3.name}'s account balance after loan:",
#       bank.check_balance(user3.account_number))

# Check total loan as admin
# print("Total loan of the bank:", bank.admin_check_total_loan_amount(admin))

# Check the total balance as an admin
print("Total Balance of the bank:", bank.admin_check_total_balance(admin))
print()
# Disable loan feature
# bank.admin_disable_loan_feature(admin)

# # Try taking a loan after disabling the feature
# loan_amount_user3 = bank.take_loan(user3.account_number)
# if loan_amount_user3:
#     print(f"{user3.name} has taken a loan of {loan_amount_user3}.")

# Enable loan feature
# bank.admin_enable_loan_feature(admin)

# Transfer money
# bank.transfer(user1.account_number, user2.account_number, 400)

# Check account balance after transfer
# print(f"{user1.name}'s account balance:",
#       bank.check_balance(user1.account_number))
# print(f"{user2.name}'s account balance:",
#       bank.check_balance(user2.account_number))

print()
print("again try to withdraw money:")
bank.withdraw(user1.account_number, 1000)
bank.withdraw(user2.account_number, 500)

# check blance after withdraw
print("blance after tryin withdraw:")
print(f"{user1.name}'s account balance :", bank.check_balance(user1.account_number))
print(f"{user2.name}'s account balance :", bank.check_balance(user2.account_number))
# ............................


"""
# Accessing all the user objects
for user_account, user_obj in bank.users.items():
    print('ac',user_account)
    print("User:", user_obj.name)
    print("Email:", user_obj.email)
    print("Balance:", user_obj.balance)
    print("Loan:", user_obj.loan)
    print("transenction:", user_obj.transaction_history)
    print("------------------------")
"""
