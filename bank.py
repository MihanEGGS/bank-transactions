# 
# Darbības ar masīviem - https://www.w3schools.com/python/python_arrays.asp
# 

transactions = []
amount = 0
balance = 0
def deposit(transactions, amount, balance):
    balance  += amount
    transactions.append(amount)
    return balance
def withdraw(transactions, amount, balance):
    if balance < amount:
        print("Du bist inavlid")
        return balance
    balance -= amount 
    transactions.append(-amount)
    return balance
def check_balance(balance):
    print (balance)

def list(transactions):
    for i in transactions:
        print (i)

while True:
    print("\nBanking Options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. List transactions")
    print("5. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        a = float(input("Whats the amount?"))
        balance = deposit(transactions, a, balance)
    elif choice == '2':
        w = float(input("Whats the withdraw?"))
        balance = withdraw(transactions, w, balance)
    elif choice == '3':
        check_balance(balance)
    elif choice == '4':
        list(transactions)
    elif choice == '5':
        print("Exiting the banking system. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

