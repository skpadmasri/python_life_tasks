class Bank:

    accounts = {}

    def create_account(self):

        username = input("Enter Username: ")

        if username in Bank.accounts:
            print("Account already exists!")
            return

        password = input("Enter Password: ")

        Bank.accounts[username] = {
            "password": password,
            "balance": 5000,
            "transactions": []
        }

        print("Account Created Successfully!")

    def login(self):

        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if username in Bank.accounts:

            if Bank.accounts[username]["password"] == password:

                print("\nLogin Successful!")
                print("Welcome to Python Bank")

                self.menu(username)

            else:
                print("Invalid Password!")

        else:
            print("Invalid Username!")

    def check_balance(self, username):

        balance = Bank.accounts[username]["balance"]

        print("Available Balance:", balance)

    def deposit(self, username):

        amount = float(input("Enter Deposit Amount: "))

        if amount > 0:

            Bank.accounts[username]["balance"] += amount

            Bank.accounts[username]["transactions"].append(
                f"Deposited: Rs.{amount}"
            )

            print("Amount Deposited Successfully!")

        else:
            print("Enter Valid Amount!")

    def withdraw(self, username):

        amount = float(input("Enter Withdraw Amount: "))

        balance = Bank.accounts[username]["balance"]

        if amount <= 0:
            print("Enter Valid Amount!")

        elif amount <= balance:

            Bank.accounts[username]["balance"] -= amount

            Bank.accounts[username]["transactions"].append(
                f"Withdrawn: Rs.{amount}"
            )

            print("Amount Withdrawn Successfully!")

        else:
            print("Insufficient Balance!")

    def mini_statement(self, username):

        transactions = Bank.accounts[username]["transactions"]

        print("\n----- MINI STATEMENT -----")

        if len(transactions) == 0:

            print("No Transactions Available")

        else:

            for transaction in transactions:
                print(transaction)

        print("Current Balance:",
              Bank.accounts[username]["balance"])

    def menu(self, username):

        while True:

            print("\n===== PYTHON BANK =====")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Mini Statement")
            print("5. Logout")

            choice = input("Enter Your Choice: ")

            if choice == "1":
                self.deposit(username)

            elif choice == "2":
                self.withdraw(username)

            elif choice == "3":
                self.check_balance(username)

            elif choice == "4":
                self.mini_statement(username)

            elif choice == "5":
                print("Thank You for Using Python Bank!")
                break

            else:
                print("Invalid Choice! Try Again")


bank = Bank()

while True:

    print("\n===== WELCOME TO PYTHON BANK =====")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        bank.create_account()

    elif choice == "2":
        bank.login()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
