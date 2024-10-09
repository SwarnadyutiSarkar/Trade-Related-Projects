import tkinter as tk
from tkinter import messagebox

class ExpenseSharingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Sharing App")

        # Initialize data
        self.expenses = {}
        self.contributors = {}

        # Setup GUI components
        self.create_widgets()

    def create_widgets(self):
        # Contributors input
        tk.Label(self.root, text="Contributor Name:").grid(row=0, column=0)
        self.contributor_entry = tk.Entry(self.root)
        self.contributor_entry.grid(row=0, column=1)

        # Expense input
        tk.Label(self.root, text="Expense Description:").grid(row=1, column=0)
        self.expense_desc_entry = tk.Entry(self.root)
        self.expense_desc_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Total Expense Amount:").grid(row=2, column=0)
        self.total_expense_entry = tk.Entry(self.root)
        self.total_expense_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Split Among (comma-separated names):").grid(row=3, column=0)
        self.split_entry = tk.Entry(self.root)
        self.split_entry.grid(row=3, column=1)

        # Buttons
        tk.Button(self.root, text="Add Contributor", command=self.add_contributor).grid(row=4, column=0)
        tk.Button(self.root, text="Add Expense", command=self.add_expense).grid(row=4, column=1)
        tk.Button(self.root, text="View Balances", command=self.view_balances).grid(row=5, column=0, columnspan=2)

    def add_contributor(self):
        name = self.contributor_entry.get().strip()
        if name and name not in self.contributors:
            self.contributors[name] = 0
            messagebox.showinfo("Info", f"Contributor '{name}' added successfully!")
        elif name in self.contributors:
            messagebox.showerror("Error", f"Contributor '{name}' already exists.")
        else:
            messagebox.showerror("Error", "Please enter a valid name.")
        self.contributor_entry.delete(0, tk.END)

    def add_expense(self):
        try:
            desc = self.expense_desc_entry.get().strip()
            total = float(self.total_expense_entry.get().strip())
            split_names = [name.strip() for name in self.split_entry.get().split(',') if name.strip()]

            if desc and total > 0 and all(name in self.contributors for name in split_names):
                amount_per_person = total / len(split_names)
                for name in split_names:
                    self.contributors[name] -= amount_per_person

                messagebox.showinfo("Info", f"Expense '{desc}' added successfully!")
            else:
                messagebox.showerror("Error", "Invalid input. Check names and amount.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid total expense amount.")
        
        # Clear entries
        self.expense_desc_entry.delete(0, tk.END)
        self.total_expense_entry.delete(0, tk.END)
        self.split_entry.delete(0, tk.END)

    def view_balances(self):
        if not self.contributors:
            messagebox.showinfo("Balances", "No contributors added.")
            return

        balances = "\n".join(f"{name}: ${balance:.2f}" for name, balance in self.contributors.items())
        messagebox.showinfo("Balances", balances)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseSharingApp(root)
    root.mainloop()
