# *ATM Machine* 
# def atm(balance): 
# Create inner functions: 
# deposit(amount) 
# withdraw(amount) 
# check_balance()

def atm(balance):
    def deposit(amount):
        nonlocal balance
        balance += amount
        print(f"Deposited: Rs.{amount}")
        print(f"New Balance: Rs.{balance}")

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            print("Insufficient funds.")
        else:
            balance -= amount
            print(f"Withdrawn: Rs.{amount}")
            print(f"New Balance: Rs.{balance}")

    def check_balance():
        print(f"Current Balance: Rs.{balance}")

    return deposit, withdraw, check_balance