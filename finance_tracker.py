import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class FinanceTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        
        # Initialize data
        self.income = 0
        self.expenses = []
        self.savings_goal = 0

        # Setup GUI components
        self.create_widgets()

    def create_widgets(self):
        # Income input
        tk.Label(self.root, text="Monthly Income:").grid(row=0, column=0)
        self.income_entry = tk.Entry(self.root)
        self.income_entry.grid(row=0, column=1)

        # Expense input
        tk.Label(self.root, text="Expense Description:").grid(row=1, column=0)
        self.expense_desc_entry = tk.Entry(self.root)
        self.expense_desc_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Expense Amount:").grid(row=2, column=0)
        self.expense_amount_entry = tk.Entry(self.root)
        self.expense_amount_entry.grid(row=2, column=1)

        # Savings goal input
        tk.Label(self.root, text="Savings Goal:").grid(row=3, column=0)
        self.savings_goal_entry = tk.Entry(self.root)
        self.savings_goal_entry.grid(row=3, column=1)

        # Buttons
        tk.Button(self.root, text="Add Income", command=self.add_income).grid(row=4, column=0)
        tk.Button(self.root, text="Add Expense", command=self.add_expense).grid(row=4, column=1)
        tk.Button(self.root, text="Set Savings Goal", command=self.set_savings_goal).grid(row=5, column=0)
        tk.Button(self.root, text="View Summary", command=self.view_summary).grid(row=5, column=1)
        tk.Button(self.root, text="Plot Expenses", command=self.plot_expenses).grid(row=6, column=0, columnspan=2)

    def add_income(self):
        try:
            self.income = float(self.income_entry.get())
            messagebox.showinfo("Info", "Income added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid income.")

    def add_expense(self):
        try:
            desc = self.expense_desc_entry.get()
            amount = float(self.expense_amount_entry.get())
            self.expenses.append((desc, amount))
            messagebox.showinfo("Info", "Expense added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid expense amount.")

    def set_savings_goal(self):
        try:
            self.savings_goal = float(self.savings_goal_entry.get())
            messagebox.showinfo("Info", "Savings goal set successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid savings goal.")

    def view_summary(self):
        total_expenses = sum(amount for _, amount in self.expenses)
        balance = self.income - total_expenses
        summary = f"Income: ${self.income}\nTotal Expenses: ${total_expenses}\nBalance: ${balance}\nSavings Goal: ${self.savings_goal}"
        messagebox.showinfo("Summary", summary)

    def plot_expenses(self):
        if not self.expenses:
            messagebox.showerror("Error", "No expenses to plot.")
            return
        labels, amounts = zip(*self.expenses)
        plt.bar(labels, amounts)
        plt.title("Expenses")
        plt.xlabel("Description")
        plt.ylabel("Amount")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceTracker(root)
    root.mainloop()
