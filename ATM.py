# ATM with simple PIN check

correct_pin = "1234"
balance = 1000

print("Welcome to the ATM!")

# Ask for PIN
pin = input("Enter your 4-digit PIN: ")

if pin == correct_pin:
    print("PIN accepted. Access granted.")

    while True:
        print("\n--- Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("Your balance is: $", balance)

        elif choice == '2':
            amount = float(input("Enter amount to deposit: $"))
            balance += amount
            print("Deposited: $", amount)

        elif choice == '3':
            amount = float(input("Enter amount to withdraw: $"))
            if amount <= balance:
                balance -= amount
                print("Withdrawn: $", amount)
            else:
                print("Not enough balance!")

        elif choice == '4':
            print("Thank you for using the ATM. Bye!")
            break

        else:
            print("Invalid choice. Try again.")

else:
    print("Incorrect PIN. Access denied.")
