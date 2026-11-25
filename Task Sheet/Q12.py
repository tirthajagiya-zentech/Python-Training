# Create an ATM machine
#
# - User should be able get money out of it
# - User should be able to deposite money into it
# - You must ask card number and pin before any transaction
# - User can get overall information about his bank account
# - There should be a limit in one time transaction and total transaction in a day (Consider day as from starting of script to exit)
# - Limit on number of transaction
# - Let user choose the bank of ATM
# - Every ATM will have some initial balance
# - Every user has it's own bank
# - If user takes money from an ATM other than his bank take 5% cut in withdrawl amount
#
# Nice to have features:
# - Insert, update and delete users (Generate card number and PIN randomly)
# - Insert, update and delete ATMs
# - Insert, update and delete banks
# - Insert money into ATM (No database is needed for this it can be managed using dicts)
#
# Hint: You can manage all this with data dictionary data type.

import random


class Bank:

    def __init__(self, name, atm_cash, max_transactions, daily_limit, single_limit):
        self.name = name
        self.atm_cash = atm_cash
        self.max_transactions = max_transactions
        self.daily_limit = daily_limit
        self.single_limit = single_limit

    def show_details(self):
        print("----------------------------------")
        print(f"Bank Name             : {self.name}")
        print(f"ATM Balance           : {self.atm_cash}")
        print(f"Max Transactions/Day  : {self.max_transactions}")
        print(f"Daily Withdraw Limit  : {self.daily_limit}")
        print(f"Single Tx Limit       : {self.single_limit}")
        print("----------------------------------")


class Customer:

    def __init__(self, holder_name, bank_name, balance, card_no, pin):
        self.holder_name = holder_name
        self.bank_name = bank_name
        self.balance = balance
        self.card_no = card_no
        self.pin = pin
        self.tx_count = 0
        self.daily_withdrawn = 0

    def show_account(self):
        print("----------------------------------")
        print(f"Holder Name     : {self.holder_name}")
        print(f"Bank Name       : {self.bank_name}")
        print(f"Card Number     : {self.card_no}")
        print(f"PIN             : {self.pin}")
        print(f"Balance         : {self.balance}")
        print(f"Transactions    : {self.tx_count}")
        print(f"Withdrawn Today : {self.daily_withdrawn}")
        print("----------------------------------")

    def withdraw_cash(self, amount, atm_bank):
        print("\n--- Withdraw Cash ---")

        if amount <= 0:
            print("Enter a valid positive amount.")
            return

        if self.tx_count >= atm_bank.max_transactions:
            print("Daily transaction count limit reached.")
            return

        if amount > atm_bank.single_limit:
            print("Amount exceeds single transaction limit.")
            return

        if self.daily_withdrawn + amount > atm_bank.daily_limit:
            print("Amount exceeds daily withdrawal limit.")
            return

        if amount > atm_bank.atm_cash:
            print("Insufficient cash in this ATM.")
            return

        is_other_bank = self.bank_name.upper() != atm_bank.name.upper()
        fee = round(amount * 0.05, 2) if is_other_bank else 0
        total_debit = amount + fee

        if total_debit > self.balance:
            print("Insufficient balance in your account.")
            return

        self.balance -= total_debit
        atm_bank.atm_cash -= amount
        self.tx_count += 1
        self.daily_withdrawn += amount

        print(f"Withdrawn Amount : {amount}")
        if is_other_bank:
            print(f"Other Bank Fee (5%) : {fee}")
        print(f"Total Debited    : {total_debit}")
        print(f"Updated Balance  : {self.balance}")

    def deposit_cash(self, amount, atm_bank):
        print("\n--- Deposit Cash ---")

        if amount <= 0:
            print("Enter a valid positive amount.")
            return

        if self.tx_count >= atm_bank.max_transactions:
            print("Daily transaction count limit reached.")
            return

        if amount > atm_bank.single_limit:
            print("Amount exceeds single transaction limit.")
            return

        self.balance += amount
        atm_bank.atm_cash += amount
        self.tx_count += 1

        print(f"Deposited Amount : {amount}")
        print(f"Updated Balance  : {self.balance}")


banks = {
    "SBI": Bank("SBI", 500000, 5, 50000, 20000),
    "HDFC": Bank("HDFC", 400000, 4, 40000, 15000),
    "AXIS": Bank("AXIS", 300000, 3, 30000, 10000),
}

customers = {
    2001: Customer("Aarav", "SBI", 120000, 2001, 1122),
    2002: Customer("Karan", "HDFC", 45000, 2002, 2233),
    2003: Customer("Neha", "AXIS", 90000, 2003, 3344),
    2004: Customer("Priya", "SBI", 15000, 2004, 4455),
}


def generate_card_and_pin():
    while True:
        card = random.randint(1000, 9999)
        if card not in customers:
            break
    pin = random.randint(1000, 9999)
    return card, pin


def choose_atm_bank():
    print("\nAvailable ATM Banks:")
    for bank_name in banks:
        print(f"- {bank_name}")
    selected = input("Enter ATM Bank Name : ").strip().upper()
    if selected not in banks:
        print("ATM Bank not found.")
        return None
    return banks[selected]


while True:
    print("\n================================")
    print("          ATM SYSTEM")
    print("================================")
    print("1. Admin Menu")
    print("2. Customer Login")
    print("3. Exit")
    print("================================")

    try:
        main_choice = int(input("Enter Your Choice : "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if main_choice == 1:
        while True:
            print("\n--- Admin Menu ---")
            print("1. Show All Users")
            print("2. Show All Banks")
            print("3. Add New User")
            print("4. Delete User")
            print("5. Add New Bank")
            print("6. Delete Bank")
            print("7. Add Cash to ATM")
            print("8. Back")

            try:
                admin_choice = int(input("Enter Admin Choice : "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if admin_choice == 1:
                if not customers:
                    print("No users found.")
                for user_obj in customers.values():
                    user_obj.show_account()

            elif admin_choice == 2:
                if not banks:
                    print("No banks found.")
                for bank_obj in banks.values():
                    bank_obj.show_details()

            elif admin_choice == 3:
                name = input("Enter User Name : ").strip()
                bank_name = input("Enter Bank Name : ").strip().upper()
                if bank_name not in banks:
                    print("Bank does not exist. Add bank first.")
                    continue
                try:
                    balance = int(input("Enter Initial Balance : "))
                except ValueError:
                    print("Invalid balance.")
                    continue
                card_no, pin = generate_card_and_pin()
                customers[card_no] = Customer(name, bank_name, balance, card_no, pin)
                print(f"User Added! Card Number: {card_no}, PIN: {pin}")

            elif admin_choice == 4:
                if not customers:
                    print("No users available.")
                    continue
                for card_no, user_obj in customers.items():
                    print(f"Card: {card_no} | Name: {user_obj.holder_name}")
                try:
                    del_card = int(input("Enter Card Number to Delete : "))
                except ValueError:
                    print("Invalid card number.")
                    continue
                if del_card in customers:
                    removed = customers.pop(del_card)
                    print(f"User {removed.holder_name} removed.")
                else:
                    print("Card number not found.")

            elif admin_choice == 5:
                b_name = input("Enter New Bank Name : ").strip().upper()
                if b_name in banks:
                    print("Bank already exists.")
                    continue
                try:
                    atm_cash = int(input("Enter Initial ATM Cash : "))
                    max_tx = int(input("Enter Max Transactions Limit : "))
                    daily_lim = int(input("Enter Daily Withdrawal Limit : "))
                    single_lim = int(input("Enter Per Transaction Limit : "))
                except ValueError:
                    print("Invalid numeric input.")
                    continue
                banks[b_name] = Bank(b_name, atm_cash, max_tx, daily_lim, single_lim)
                print(f"Bank {b_name} added.")

            elif admin_choice == 6:
                if not banks:
                    print("No banks available.")
                    continue
                for b_name in banks:
                    print(f"- {b_name}")
                del_bank = input("Enter Bank Name to Delete : ").strip().upper()
                if del_bank in banks:
                    banks.pop(del_bank)
                    print(f"Bank {del_bank} removed.")
                else:
                    print("Bank not found.")

            elif admin_choice == 7:
                atm_bank = choose_atm_bank()
                if atm_bank is not None:
                    try:
                        cash = int(input("Enter Cash Amount to Insert : "))
                    except ValueError:
                        print("Invalid amount.")
                        continue
                    if cash > 0:
                        atm_bank.atm_cash += cash
                        print(f"Added {cash} to {atm_bank.name} ATM. New ATM Balance: {atm_bank.atm_cash}")
                    else:
                        print("Enter positive amount.")

            elif admin_choice == 8:
                break

            else:
                print("Invalid admin choice.")

    elif main_choice == 2:
        try:
            card_input = int(input("\nEnter Card Number : "))
            pin_input = int(input("Enter PIN : "))
        except ValueError:
            print("Card number and PIN must be numbers.")
            continue

        if card_input not in customers or customers[card_input].pin != pin_input:
            print("Invalid Card Number or PIN.")
            continue

        current_user = customers[card_input]
        print(f"\nWelcome, {current_user.holder_name}!")

        while True:
            print("\n--------------------------------")
            print("1. Withdraw Money")
            print("2. Deposit Money")
            print("3. Account Summary")
            print("4. Logout")
            print("--------------------------------")

            try:
                user_choice = int(input("Enter Your Choice : "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if user_choice == 1:
                atm_bank = choose_atm_bank()
                if atm_bank is None:
                    continue
                try:
                    amount = int(input("Enter Amount to Withdraw : "))
                except ValueError:
                    print("Invalid amount.")
                    continue
                current_user.withdraw_cash(amount, atm_bank)

            elif user_choice == 2:
                atm_bank = choose_atm_bank()
                if atm_bank is None:
                    continue
                try:
                    amount = int(input("Enter Amount to Deposit : "))
                except ValueError:
                    print("Invalid amount.")
                    continue
                current_user.deposit_cash(amount, atm_bank)

            elif user_choice == 3:
                current_user.show_account()

            elif user_choice == 4:
                print("Logged out successfully.")
                break

            else:
                print("Invalid choice.")

    elif main_choice == 3:
        print("\nThank you for using ATM System.")
        break

    else:
        print("Invalid choice.")
