print("===== PERSONAL EXPENSE TRACKER =====")

expense_name = input("Enter Expense Name: ")
expense_amount = float(input("Enter Expense Amount: "))
expense_category = input("Enter Expense Category: ")

print("\n===== EXPENSE DETAILS =====")
print("Expense:", expense_name)
print("Amount:", expense_amount)
print("Category:", expense_category)

print("\n===== EXPENSE SUMMARY =====")
print("Your expense amount:", expense_amount)
print("Amount after adding 100:", expense_amount + 100)