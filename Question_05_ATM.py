
balance = float(input("Enter initial balance: "))

n = int(input("Enter number of transactions: "))

total_deposits = 0
total_withdrawals = 0
rejected = 0

for i in range(n):

    print("\nTransaction", i + 1)

    transaction = input("Enter deposit or withdraw: ").lower()
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount! Transaction rejected.")
        rejected += 1

    elif transaction == "deposit":
        balance = balance + amount
        total_deposits = total_deposits + amount
        print("Deposit successful.")

    elif transaction == "withdraw":
        if amount > 10000:
            print("Withdrawal limit exceeded!")
            rejected += 1

        elif amount > balance:
            print("Insufficient balance!")
            rejected += 1

        else:
            balance = balance - amount
            total_withdrawals = total_withdrawals + amount
            print("Withdrawal successful.")

    else:
        print("Invalid transaction type!")
        rejected += 1

print("\n----- ATM TRANSACTION SUMMARY -----")
print("Final Balance: Rs.", balance)
print("Total Deposits: Rs.", total_deposits)
print("Total Withdrawals: Rs.", total_withdrawals)
print("Rejected Transactions:", rejected)
print("-----------------------------------")
