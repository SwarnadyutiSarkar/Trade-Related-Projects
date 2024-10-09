import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class InvestmentPortfolioManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Investment Portfolio Manager")
        
        # Initialize data
        self.portfolio = {}
        
        # Setup GUI components
        self.create_widgets()

    def create_widgets(self):
        # Investment input
        tk.Label(self.root, text="Investment Name:").grid(row=0, column=0)
        self.investment_name_entry = tk.Entry(self.root)
        self.investment_name_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Investment Amount:").grid(row=1, column=0)
        self.investment_amount_entry = tk.Entry(self.root)
        self.investment_amount_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Current Value:").grid(row=2, column=0)
        self.current_value_entry = tk.Entry(self.root)
        self.current_value_entry.grid(row=2, column=1)

        # Buttons
        tk.Button(self.root, text="Add Investment", command=self.add_investment).grid(row=3, column=0)
        tk.Button(self.root, text="View Portfolio", command=self.view_portfolio).grid(row=3, column=1)
        tk.Button(self.root, text="Plot Portfolio", command=self.plot_portfolio).grid(row=4, column=0, columnspan=2)

    def add_investment(self):
        try:
            name = self.investment_name_entry.get()
            amount = float(self.investment_amount_entry.get())
            current_value = float(self.current_value_entry.get())
            self.portfolio[name] = {'amount': amount, 'current_value': current_value}
            messagebox.showinfo("Info", "Investment added successfully!")
            self.clear_entries()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for amount and current value.")

    def clear_entries(self):
        self.investment_name_entry.delete(0, tk.END)
        self.investment_amount_entry.delete(0, tk.END)
        self.current_value_entry.delete(0, tk.END)

    def view_portfolio(self):
        if not self.portfolio:
            messagebox.showinfo("Portfolio", "Your portfolio is empty.")
            return
        
        portfolio_summary = "Your Portfolio:\n"
        for name, details in self.portfolio.items():
            profit_loss = details['current_value'] - details['amount']
            portfolio_summary += f"{name}: Initial: ${details['amount']}, Current: ${details['current_value']}, P/L: ${profit_loss}\n"
        messagebox.showinfo("Portfolio Summary", portfolio_summary)

    def plot_portfolio(self):
        if not self.portfolio:
            messagebox.showerror("Error", "Your portfolio is empty.")
            return
        
        labels = list(self.portfolio.keys())
        initial_values = [details['amount'] for details in self.portfolio.values()]
        current_values = [details['current_value'] for details in self.portfolio.values()]
        
        x = range(len(labels))

        plt.bar(x, initial_values, width=0.4, label='Initial Value', color='b', align='center')
        plt.bar([p + 0.4 for p in x], current_values, width=0.4, label='Current Value', color='g', align='center')

        plt.xlabel("Investments")
        plt.ylabel("Value ($)")
        plt.title("Investment Portfolio Performance")
        plt.xticks([p + 0.2 for p in x], labels)
        plt.legend()
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = InvestmentPortfolioManager(root)
    root.mainloop()
