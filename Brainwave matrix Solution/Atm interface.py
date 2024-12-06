def generate_random_pin():
    pin = ""
    for i in range(4):
        digit = (37 * (91 + i) + 5) % 10  # Varying method to get a digit
        pin += str(digit)
    return pin

def insert_card():
    print("Please insert your card (press Enter to continue).")
    input()

def select_language():
    print("Please select your language:")
    print("1. English")
    print("2. Hindi")
    print("3. Kannada")
    print("4. Telugu")
    language = int(input("Enter your choice: "))
    if language in [1, 2, 3, 4]:
        print("Language selected.")
    else:
        print("Invalid language selection. Defaulting to English.")
    print()

def enter_pin():
    attempts = 3

    while attempts > 0:
        pin = input("Please enter your 4-digit PIN: ")
        if len(pin) != 4 or not pin.isdigit():
            print("Invalid PIN. The PIN must be exactly 4 digits long and numeric.")
        else:
            print("PIN accepted.")
            return True
        attempts -= 1
        print(f"Invalid PIN. You have {attempts} attempts left.")
    
    print("Your card has been blocked due to multiple incorrect PIN entries.")
    return False

def check_balance(balance):
    print("Your current balance is: ₹" + str(balance))

def deposit(balance, amount):
    if amount > 0:
        balance += amount
        print("₹" + str(amount) + " has been deposited to your account.")
        generate_receipt("Deposit", amount, balance)
    else:
        print("Invalid deposit amount. Please enter a positive value.")
    return balance

def withdraw(balance, amount):
    if 0 < amount <= balance:
        balance -= amount
        print("₹" + str(amount) + " has been withdrawn from your account.")
        generate_receipt("Withdrawal", amount, balance)
    else:
        print("Invalid withdrawal amount. Either the amount is greater than the available balance or it's a non-positive value.")
    return balance

def generate_receipt(transaction_type, amount, balance):
    print("\n--- Receipt ---")
    print("Transaction Type: " + transaction_type)
    print("Amount: ₹" + str(amount))
    print("Remaining Balance: ₹" + str(balance))
    print("----------------")

# Simulate ATM interface
insert_card()
select_language()

if enter_pin():
    balance = 1000  # Initial balance can be set as required

    while True:
        print("\nWelcome to the ATM")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Please choose an option: "))

        if choice == 1:
            check_balance(balance)
        elif choice == 2:
            amount = float(input("Enter the amount to deposit: ₹"))
            balance = deposit(balance, amount)
        elif choice == 3:
            amount = float(input("Enter the amount to withdraw: ₹"))
            balance = withdraw(balance, amount)
        elif choice == 4:
            print("Thank you for using our ATM service. Have a great day!")
            break
        else:
            print("Invalid option. Please try again.")

