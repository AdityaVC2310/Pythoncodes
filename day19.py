# Class definition
class Student:
    # Special member function __init__ is used to define data members
    def __init__(self):
        # Declare the data members
        self.roll = 0
        self.name = ""
        self.marks1 = 0.0
        self.marks2 = 0.0
        self.percent = 0.0

# Main section
# Object declaration (s1 is an object of Student class)
s1 = Student()

# User input
s1.roll = int(input("Enter roll no.: "))
s1.name = input("Enter Name: ")
s1.marks1 = float(input("Enter marks1: "))
s1.marks2 = float(input("Enter marks2: "))

# Calculate percentage
s1.percent = (s1.marks1 + s1.marks2) / 200 * 100

# Display all the properties
print("Roll no: ", s1.roll)
print("Name: ", s1.name)
print("Marks 1: ", s1.marks1)
print("Marks 2: ", s1.marks2)
print("Percent: ", s1.percent)
