class Employee:
    # Initialization function
    def __init__(self):
        # Data members
        self.empid = 0
        self.empname = ""
        self.bsal = 0.0
        self.itr = 0.0
        self.hra = 0.0
        self.gsal = 0.0

    # Method to input employee details
    def input_details(self):
        self.empid = int(input("Enter Employee ID: "))
        self.empname = input("Enter Employee Name: ")
        self.bsal = float(input("Enter Basic Salary: "))

    # Method to calculate salary components
    def calculate_salary(self):
        self.itr = self.bsal * 0.2  # Income Tax Return (20% of basic salary)
        self.hra = self.bsal * 0.3  # House Rent Allowance (30% of basic salary)
        self.gsal = self.bsal + self.hra - self.itr  # Gross Salary

    # Method to display employee details
    def display_details(self):
        print("\nEmployee ID: ", self.empid)
        print("Employee Name: ", self.empname)
        print("Employee Basic Salary: ", self.bsal)
        print("Employee House Rent Allowance: ", self.hra)
        print("Employee Income Tax Return: ", self.itr)
        print("Employee Gross Salary: ", self.gsal)

# Main section
# Object declaration
e1 = Employee()
# User input
e1.input_details()
# Salary calculations
e1.calculate_salary()
# Display all members
e1.display_details()
