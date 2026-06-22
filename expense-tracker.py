print("=" * 40)
print("      EXPENSE TRACKER SYSTEM")
print("=" * 40)

total = 0
expense_count = 0

while True:
    user_input = input(
        "\nEnter expense amount (or type 'quit' to stop): "
    )

    # Sentinel Value (Kill Switch)
    if user_input.lower() == "quit":
        print("\nStopping Expense Tracker...")
        break

    # Defensive Coding
    try:
        expense = float(user_input)

        if expense < 0:
            print("Expense cannot be negative!")
            continue

        # Accumulator Pattern
        total += expense
        expense_count += 1

        print(f"Expense Added: ₹{expense:.2f}")
        print(f"Running Total : ₹{total:.2f}")

    except ValueError:
        print("Invalid Input! Please enter a valid number.")

# Output Phase
print("\n" + "=" * 40)
print("            FINAL REPORT")
print("=" * 40)

print(f"Number of Expenses : {expense_count}")
print(f"Total Expenses     : ₹{total:.2f}")

if expense_count > 0:
    average = total / expense_count
    print(f"Average Expense    : ₹{average:.2f}")
else:
    print("Average Expense    : ₹0.00")

print("=" * 40)
print("Thank You For Using Expense Tracker!")
print("=" * 40)

