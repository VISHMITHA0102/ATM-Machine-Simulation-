import time

print("Please insert Your CARD")

# Simulate card processing
time.sleep(5)

password = 1234

# User account balance
balance = 5000

# Transaction history list
transaction_history = []

try:
    # Taking ATM pin from user
    pin = int(input("Enter your ATM pin: "))
except ValueError:
    print("Invalid input! Please enter numeric pin.")
    pin = None

# Checking if the pin is valid
if pin == password:
    while True:
        # Showing info to user
        print("""
        1 == Balance
        2 == Withdraw balance
        3 == Deposit balance
        4 == Change PIN
        5 == Transaction history
        6 == Exit
        """)

        try:
            # Taking an option from user
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue

        # Option 1: Check balance
        if option == 1:
            print(f"Your current balance is: {balance}")
            print("*******************************************")

        # Option 2: Withdraw balance
        elif option == 2:
            try:
                withdraw_amount = int(input("Please enter withdrawal amount: "))
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
                continue

            if withdraw_amount > balance:
                print("Insufficient balance!")
            else:
                balance -= withdraw_amount
                transaction_history.append(f"Withdrew {withdraw_amount}")
                print(f"{withdraw_amount} is debited from your account.")
                print(f"Your updated balance is: {balance}")

            print("*******************************************")

        # Option 3: Deposit balance
        elif option == 3:
            try:
                deposit_amount = int(input("Please enter deposit amount: "))
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
                continue

            balance += deposit_amount
            transaction_history.append(f"Deposited {deposit_amount}")
            print(f"{deposit_amount} is credited to your account.")
            print(f"Your updated balance is: {balance}")

            print("*******************************************")

        # Option 4: Change PIN
        elif option == 4:
            try:
                old_pin = int(input("Please enter your current PIN: "))
                if old_pin == password:
                    new_pin = int(input("Please enter your new PIN: "))
                    confirm_pin = int(input("Please confirm your new PIN: "))
                    if new_pin == confirm_pin:
                        password = new_pin
                        print("PIN successfully changed.")
                    else:
                        print("New PIN and confirmation do not match.")
                else:
                    print("Incorrect current PIN.")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
            print("*******************************************")

        # Option 5: Transaction history
        elif option == 5:
            if not transaction_history:
                print("No transactions yet.")
            else:
                print("Transaction history:")
                for transaction in transaction_history:
                    print(transaction)
            print("*******************************************")

        # Option 6: Exit
        elif option == 6:
            print("Thank you for using our service!")
            break

        else:
            print("Invalid choice! Please select a number between 1 and 6.")

else:
    print("Wrong pin. Please try again.")
