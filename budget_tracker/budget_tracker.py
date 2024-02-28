#!/usr/bin/python3
import json

# Add expenses
def add_expense(expenses, description, amount):
    expenses.append({"description": description, "amount": amount}) # Added to a the list as a dictionary with key-value pairs
    print(f"\nAdded expense: {description},\nAmount: {amount}")

# Getting total expenses
def get_total_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense['amount']
    return sum

# Getting the balance
def get_balance(budget, expenses):
    balance = budget - get_total_expenses(expenses)
    return balance

# Show budget details
def show_budget_details(budget, expenses):
    print(f"\nTotal budget: {budget}")
    print("Expenses:")
    for expense in expenses:
        print(f"- {expense['description']}: {expense['amount']}")
    print(f"Total spent: {get_total_expenses(expenses)}")
    print(f"Remaining budget: {get_balance(budget, expenses)}")

# Saving budget data
def save_budget_data(filepath, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

# Retrieving budget data
def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data['initial_budget'], data['expenses']
    except(FileNotFoundError, json.JSONDecodeError):
        return 0, []

# Main program
def main():
    print("Welcome to the Budget Tracker App!")
    filepath = 'budget_data.json'
    initial_budget, expenses = load_budget_data(filepath)
    if initial_budget == 0:
        initial_budget = float(input("\nEnter your initial budget: "))
    budget = initial_budget

    
    while True:
        print("\n1. Add an expense.")
        print("2. Show budget details.")
        print("3. Exit")

        choice = input("Enter choices 1/2/3: ")

        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter amount: "))
            add_expense(expenses, description, amount)
        elif choice == '2':
            show_budget_details(budget, expenses)
        elif choice == '3':
            save_budget_data(filepath, initial_budget, expenses)
            print("Exiting the app! Goodbye!")
            break
        else:
            print("Invalid choice, choose again please!")

if __name__ =='__main__':
    main()
