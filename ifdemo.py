# Starting balance
balance = 1000

# Welcome message
print("Welcome to the Simple ATM Simulator!")
print("You have ₱1000 in your account.\n")

# Menu loop
while True:
    # Display options
    print("Please choose an option:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    # Get user input
    choice = input("Enter choice (1-4): ")

    # Check Balance
    if choice == "1":
        print(f"Your current balance is: ₱{balance}\n")

    # Deposit
    elif choice == "2":
        deposit_amount = input("Enter amount to deposit: ")
        if deposit_amount.isdigit():
            deposit_amount = int(deposit_amount)
            if deposit_amount > 0:
                balance += deposit_amount
                print(f"Successfully deposited ₱{deposit_amount}. Newbalance: ₱{balance}\n")
            else:
                print("Please enter a positive amount.\n")
        else:
            print("Invalid input. Please enter a number.\n")

    # Withdraw
    elif choice == "3":
        withdraw_amount = input("Enter amount to withdraw: ")
        if withdraw_amount.isdigit():
            withdraw_amount = int(withdraw_amount)
            if withdraw_amount > 0:
                if withdraw_amount <= balance:
                    balance -= withdraw_amount
                    print(f"Successfully withdrew ₱{withdraw_amount}.Remaining balance: ₱{balance}\n")
                else:
                    print("Insufficient funds.\n")
            else:
                print("Please enter a positive amount.\n")
        else:
            print("Invalid input. Please enter a number.\n")

    # Exit
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    # Invalid Option
    else:
        print("Invalid choice. Please enter a number from 1 to 4.\n")