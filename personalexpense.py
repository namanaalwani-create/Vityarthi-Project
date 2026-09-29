expenses = []

def add_expense(): #this function is used to add expenses
    date = input("Enter date: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    expense = {
        "date": date,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added")


def display_expense(): #this function is used to display the expenses
    if len(expenses) == 0:
        print("No expenses found")
        return
    str="-----------LISTS OF EXPENSES------------"
    for i in range(len(expenses)):
        if(i==0):
           print(str)
        print(i + 1, expenses[i]["date"], expenses[i]["category"], 
              "Rs.", expenses[i]["amount"])


def search_expense(): #this function is used to search expenses 
    category = input("Enter category: ")
    found = False

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print(expense["date"], expense["category"],
                  "Rs.", expense["amount"])
            found = True

    if not found:
        print("Expense not found")


def update_expense(): #this function is used to update expenses
    display_expense()

    if len(expenses) == 0:
        return

    n = int(input("Enter expense number: "))

    if n >= 1 and n <= len(expenses):
        expenses[n - 1]["date"] = input("Enter new date: ")
        expenses[n - 1]["category"] = input("Enter new category: ")
        expenses[n - 1]["amount"] = float(input("Enter new amount: "))
        print("Expense updated")
    else:
        print("Invalid number")


def removeExpense(): #this function is used to delete expenses
    display_expense()

    if len(expenses) ==0:
        return

    n = int(input("Enter expenses number: "))

    if n >= 1 and n <= len(expenses):
        expenses.pop(n - 1)
        print("Expense deleted")
    else:
        print("Invalid number")

        
def summary(): #this function is used to summarize the expenses
    if len(expenses) == 0:
        print("No expenses found")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total expense =", total)


def main():
    while True:
        print("Personal Expense Tracker")
        print("1. Add Expense")
        print("2. view")
        print("3. Search Expense")
        print("4. Update")
        print("5. Delete Expense")
        print("6. Total Expense")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            display_expense()
        elif choice == "3":
            search_expense()
        elif choice == "4":
            update_expense()
        elif choice == "5":
           removeExpense()
        elif choice == "6":
            summary()
        elif choice == "7":
            print("Thank you")
            break
        else:
            print("Invalid choice")


main()