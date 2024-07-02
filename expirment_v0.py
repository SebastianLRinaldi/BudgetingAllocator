import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
from PyQt5.QtCore import Qt  # Import Qt here


"""
Yearly Limit
Monthly Limit
Weekly Limit
Daily Limit
"""
accounts = {
    "Savings": {
        "Alias":"1111",
        "Limit": 1000,
        "Used": 105,
    },
    "Checking": {
        "Alias":"2222",
        "Limit": 100,
        "Used": 85,
    }, 
    "Food": {
        "Alias":"3333",
        "Limit": 150,
        "Used": 10,
    }, 
    "Gas": {
        "Alias":"4444",
        "Limit": 200,
        "Used": 50,
    },     
}



def access_account_info(account_key):
        details = accounts[account_key]
        print(f"Account Type: {account_key}")
        print(f"Alias: {details['Alias']}")
        print(f"Limit: {details['Limit']}")
        print(f"Used: {details['Used']}\n")

    



def check_account_alias_match(user_input):
    # check if it's an alias within any account
    account_name_assocaited_with_alias = None
    found_account_match = False

    # this keeps iteration even after a match but that is for later fix
    for account_name, details in accounts.items():
        # print(f"ALISAS: {user_input} | {account_name} | {details}")
        if user_input == details["Alias"]:
            account_name_assocaited_with_alias = account_name
            found_account_match = True
            
            return (found_account_match, account_name_assocaited_with_alias)
        
    return (found_account_match, account_name_assocaited_with_alias)
    

def check_account_match(user_input):

        found_account_match = False
        account_key = None

        if user_input in accounts:
            found_account_match = True
            account_key = user_input
        else:
            account_match, account_name = check_account_alias_match(user_input)

            account_key = account_name
            found_account_match = account_match

        return (found_account_match, account_key)









class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set up the window
        self.setWindowTitle("PyQt5 Numeric Input Example")
        self.setGeometry(100, 100, 400, 250)  # Adjusted size to accommodate QLineEdit
        
        # Create buttons
        self.button1 = QPushButton('Submit Number', self)
        self.button2 = QPushButton('Clear Number', self)
        self.button3 = QPushButton('Button 3', self)
        
        # Create QLineEdit for numeric input
        self.inputField = QLineEdit(self)
        self.inputField.setPlaceholderText("Enter a number...")
        
        # Position widgets
        self.button1.move(50, 30)
        self.button2.move(50, 80)
        self.button3.move(50, 130)
        self.inputField.move(150, 30)  # Below the buttons
        
        # Connect buttons to functions
        self.button1.clicked.connect(self.button1_clicked)
        self.button2.clicked.connect(self.button2_clicked)
        self.button3.clicked.connect(self.button3_clicked)

    def button1_clicked(self):
        try:
            number = self.inputField.text() 
            print(f"Entered Number: {number}")
            
            found_account_match, account_key = check_account_match(number)

            if found_account_match:
                access_account_info(account_key)
            
            else:
                 print("account not found")

            self.inputField.clear()  # Clear the input field

        except ValueError:
            print("Please enter a valid number.")
    
    def button2_clicked(self):
        print("Number cleared")
        self.inputField.clear()
    
    def button3_clicked(self):
        print("Button 3 clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
    
