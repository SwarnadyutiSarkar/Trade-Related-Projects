class User:
    def __init__(self, username, user_type):
        self.username = username
        self.user_type = user_type  # 'lender' or 'borrower'
        self.balance = 0
        self.loan_requests = []

class LoanRequest:
    def __init__(self, borrower, amount, purpose):
        self.borrower = borrower
        self.amount = amount
        self.purpose = purpose
        self.is_funded = False

class MicrofinancePlatform:
    def __init__(self):
        self.users = {}
        self.loan_requests = []

    def register_user(self, username, user_type):
        if username in self.users:
            print("Username already exists.")
        else:
            self.users[username] = User(username, user_type)
            print(f"{user_type.capitalize()} {username} registered successfully.")

    def request_loan(self, username, amount, purpose):
        if username not in self.users or self.users[username].user_type != 'borrower':
            print("User must be a borrower to request a loan.")
            return
        
        loan_request = LoanRequest(username, amount, purpose)
        self.loan_requests.append(loan_request)
        self.users[username].loan_requests.append(loan_request)
        print(f"Loan request for ${amount} created by {username} for {purpose}.")

    def fund_loan(self, lender_username, loan_request_index):
        if lender_username not in self.users or self.users[lender_username].user_type != 'lender':
            print("User must be a lender to fund a loan.")
            return
        
        try:
            loan_request = self.loan_requests[loan_request_index]
            if loan_request.is_funded:
                print("This loan request has already been funded.")
                return
            
            # Simple funding logic
            if self.users[lender_username].balance >= loan_request.amount:
                self.users[lender_username].balance -= loan_request.amount
                loan_request.is_funded = True
                print(f"{lender_username} funded the loan of ${loan_request.amount} for {loan_request.borrower}.")
            else:
                print("Insufficient balance to fund this loan.")

        except IndexError:
            print("Invalid loan request index.")

    def add_funds(self, username, amount):
        if username not in self.users:
            print("User not found.")
            return
        
        self.users[username].balance += amount
        print(f"${amount} added to {username}'s balance.")

    def display_loan_requests(self):
        if not self.loan_requests:
            print("No loan requests available.")
            return
        
        print("\nAvailable Loan Requests:")
        for index, request in enumerate(self.loan_requests):
            if not request.is_funded:
                print(f"{index}: ${request.amount} for {request.purpose} by {request.borrower}")

    def run(self):
        while True:
            print("\nMicrofinance Platform")
            print("1. Register User")
            print("2. Request Loan")
            print("3. Fund Loan")
            print("4. Add Funds")
            print("5. Display Loan Requests")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                username = input("Enter username: ")
                user_type = input("Enter user type (lender/borrower): ").lower()
                self.register_user(username, user_type)
            elif choice == '2':
                username = input("Enter your username: ")
                amount = float(input("Enter loan amount: $"))
                purpose = input("Enter purpose of loan: ")
                self.request_loan(username, amount, purpose)
            elif choice == '3':
                lender_username = input("Enter your username: ")
                self.display_loan_requests()
                loan_index = int(input("Enter loan request index to fund: "))
                self.fund_loan(lender_username, loan_index)
            elif choice == '4':
                username = input("Enter your username: ")
                amount = float(input("Enter amount to add: $"))
                self.add_funds(username, amount)
            elif choice == '5':
                self.display_loan_requests()
            elif choice == '6':
                print("Exiting platform.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    platform = MicrofinancePlatform()
    platform.run()
