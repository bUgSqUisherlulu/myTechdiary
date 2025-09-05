from datetime import datetime


print("Budget Tracker made by Lulu")
print("Welcome User! \n Manage money in a simple way")

name=input("Enter your name:")
print("Select an option:")
print ("1. Add Income")
print ("2. Add Expense")
print ("3. View Balance")
print ("4. Reset Balance")
print ("5. History")
print ("6. Exit")
print ("__________________________")
balance = 0
history=[]
def add_income(amount):
    global balance
    balance += amount
    print(f"Income of ${amount} added.")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append(f"[{time}]Income: +${amount}") 
    print(f"Your new balance {name} is: ${balance}")
def add_expense(amount):
    global balance
    if amount > balance:
        print("Insufficient funds for this expense.")
    else:
        balance -= amount
        print(f"Expense of ${amount} added.")
        time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        history.append(f"[{time}]Expense: -${amount}")
        print(f"your new balance {name} is : ${balance}")
def view_balance():
    print(f"Current balance: ${balance}")
def reset_balance():
    global balance
    balance = 0
    print("Balance reset to $0.")
def view_history():
   if not history:
        print("No transactions .")
   else:
      
        print("\n--- Transaction History ---")
        for record in history:
            print(record)
        print("---------------------------")
while True:
    option=int(input("Enter option number: "))
    if option == 1:
        amount=float(input("Enter amount :  "))
        add_income(amount)
    elif option == 2:
        amount=float(input("Enter amount :  "))
        add_expense(amount)
    elif option == 3:
        view_balance()
    elif option == 4:
        reset_balance()
    elif option == 5:
        view_history()
    elif option == 6:
        print("Exiting Budget Tracker. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
