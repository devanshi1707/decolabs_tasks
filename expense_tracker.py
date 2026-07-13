

total = 0

print("===== Expense Tracker =====")
print("Enter your expenses one by one.")
print("Type 'quit' to finish.\n")

while True:
    expense = input("Enter expense: ")

    if expense.lower() == "quit":
        break

    try:
        expense = float(expense)
        total += expense
        print(f"Current Total: ₹{total:.2f}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

print("\n===== Expense Summary =====")
print(f"Total Spent: ₹{total:.2f}")
print("Thank you for using Expense Tracker!")
