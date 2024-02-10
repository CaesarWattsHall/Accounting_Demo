import pandas as pd

# Initialize empty dictionaries to store transactions
transactions = {
    "bills": [],
    "expenses": [],
    "savings": [],
    "notes": [],
}

# Function to add a transaction
def add_transaction(category, amount, note=""):
  if category in transactions:
    transactions[category].append({"amount": amount, "note": note})
  else:
    print("Invalid category. Please enter 'bills', 'expenses', or 'savings'.")

# Function to display transaction summary for a category
def display_summary(category):
  if transactions[category]:
    df = pd.DataFrame(transactions[category])
    print(f"{category.capitalize()}:")
    print(df)
    print(f"Total {category}: ${df['amount'].sum():.2f}")
  else:
    print(f"No {category} recorded yet.")

# Function to display all notes
def display_notes():
  if transactions["notes"]:
    df = pd.DataFrame(transactions["notes"])
    print("Notes:")
    print(df)
  else:
    print("No notes added yet.")

# Main loop
while True:
  print("\nMenu:")
  print("1. Add transaction")
  print("2. View bills summary")
  print("3. View expenses summary")
  print("4. View savings summary")
  print("5. View notes")
  print("6. Exit")

  choice = input("Enter your choice: ")

  if choice == "1":
    category = input("Enter category (bills, expenses, savings): ").lower()
    amount = float(input("Enter amount: "))
    note = input("Enter note (optional): ")
    add_transaction(category, amount, note)
  elif choice == "2":
    display_summary("bills")
  elif choice == "3":
    display_summary("expenses")
  elif choice == "4":
    display_summary("savings")
  elif choice == "5":
    display_notes()
  elif choice == "6":
    break
  else:
    print("Invalid choice. Please try again.")

print("Exiting program. Thank you!")
