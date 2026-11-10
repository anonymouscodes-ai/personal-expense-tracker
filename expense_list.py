from database import add_expense, view_expenses
expenses = []

number = int(input("How many expenses do you want to enter? "))

for i in range(number):

    print("\nEnter expense", i + 1)

    name = input("Expense name: ")
    amount = float(input("Expense amount: "))
    category = input("Expense category: ")

    expense = {
    "name": name,
    "amount": amount,
    "category": category
}

    expenses.append(expense)
    add_expense(name, amount, category)


print("\n===== ALL EXPENSES =====")

for expense in expenses:
    print("Name:", expense["name"])
    print("Amount:", expense["amount"])
    print("Category:", expense["category"])


total = 0

for expense in expenses:
    total = total + expense["amount"]

print("\nTotal expenses:", total)
print("\n===== CATEGORY SUMMARY =====")

category_totals = {}

for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]

    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount

for category, amount in category_totals.items():
    print(category, ":", amount)

print("\n===== SAVED EXPENSES FROM DATABASE =====")

saved_expenses = view_expenses()

for expense in saved_expenses:
    print(expense)