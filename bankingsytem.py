print("++++++++++Banking_system++++++++++")
print("Press 1 for check balance")
print("Press 2 for deposit")
print("Press 3 for withdraw")

choice = int(input("Enter your choice: "))
name = input("Enter your name: ")

balance = {'divyansh': 225854, 'rohan': 75858, 'mohan': 556966}

def deposit(amount, balance_amt):
    return amount + balance_amt

def withdraw(name, withdrawamount):
    if name in balance:
        if balance[name] < withdrawamount:
            print("You have not sufficient balance.")
        else:
            balance[name] -= withdrawamount
            print(f"Withdrawal successful. Remaining balance: {balance[name]}")
    else:
        print("User not found!")

def checkbalance(name):
    if name in balance:
        print(f"Your balance is equal to {balance[name]}")
    else:
        print("User not found!")

# Example usage
if choice == 1:
    checkbalance(name)
elif choice == 2:
    amt = int(input("Enter deposit amount: "))
    balance[name] = deposit(amt, balance.get(name, 0))
    print(f"Deposit successful. Current balance: {balance[name]}")
elif choice == 3:
    withdrawamount = int(input("Enter the amount you want to withdraw: "))
    withdraw(name, withdrawamount)
else:
    print("Invalid choice!")
