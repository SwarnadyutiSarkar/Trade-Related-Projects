class TaxPreparationAssistant:
    def __init__(self):
        self.income = 0
        self.deductions = []
        self.total_deductions = 0

    def welcome(self):
        print("Welcome to the Tax Preparation Assistant!")
        print("Let's get started with your tax preparation.")

    def get_income(self):
        self.income = float(input("Please enter your total income for the year: $"))

    def identify_deductions(self):
        print("\nLet's identify your potential deductions.")
        self.deductions.append(self.get_deduction("Mortgage Interest", 0))
        self.deductions.append(self.get_deduction("Charitable Contributions", 0))
        self.deductions.append(self.get_deduction("Medical Expenses", 0))
        self.deductions.append(self.get_deduction("State Taxes Paid", 0))
        self.deductions.append(self.get_deduction("Retirement Contributions", 0))
        self.calculate_total_deductions()

    def get_deduction(self, deduction_name, default):
        value = float(input(f"Enter the amount for {deduction_name} (or 0 if none): $")) or default
        return value

    def calculate_total_deductions(self):
        self.total_deductions = sum(self.deductions)
        print(f"\nYour total deductions amount to: ${self.total_deductions:.2f}")

    def calculate_taxable_income(self):
        taxable_income = self.income - self.total_deductions
        print(f"\nYour taxable income is: ${taxable_income:.2f}")
        return taxable_income

    def filing_guidance(self, taxable_income):
        print("\nFiling Guidance:")
        if taxable_income < 0:
            print("You have no taxable income, you may not need to file.")
        else:
            print("Consider filing your tax return to report your income and deductions.")

    def run(self):
        self.welcome()
        self.get_income()
        self.identify_deductions()
        taxable_income = self.calculate_taxable_income()
        self.filing_guidance(taxable_income)


if __name__ == "__main__":
    assistant = TaxPreparationAssistant()
    assistant.run()
