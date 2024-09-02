class student:
    #data members
    def __init__(self):
        self.rollno = None	
        self.name = None
        self.marks1 = None
        self.marks2 = None
        self.marks3 = None
        self.marks4 = None
        self.marks5 = None
        self.total = None
        self.per = None
    #setters
    def setRollno(self,r):
        self.rollno = r
    def setName(self,nm):
        self.name = nm
    def setmarks1(self,m1):
        self.marks1 =	m1
    def setmarks2(self,m2):
        self.marks2 =	m2
    def setmarks3(self,m3):
        self.marks3 =	m3
    def setmarks4(self,m4):
        self.marks4 =	m4
    def setmarks5(self,m5):
        self.marks5 =	m5
    #calculate function
    def calculate(self):
        self.total =  self.marks1 + self.marks2 + self.marks3 + self.marks4 + self.marks5
        self.per =  (self.marks1 + self.marks2 + self.marks3 + self.marks4 + self.marks5 )/500 *100
    #getters 
    def getRollno(self):
        return self.rollno
    def getName(self):
        return self.rollno
    def getmarks1(self):
        return self.marks1
    def getmarks2(self):
        return self.marks2
    def getmarks3(self):
        return self.marks3
    def getmarks4(self):
        return self.marks4
    def getmarks5(self):
        return self.marks5
    def gettotal(self):
        return self.total
e1= student()
r = int(input(" Enter Roll No : "))
nm = input(" Enter Name: ")
m1 = float(input(" Enter Marks 1 : "))
mark2 = float(input(" Enter Marks 2 : "))
mark3 = float(input(" Enter Marks 3 : "))
mark4 = float(input(" Enter Marks 4 : "))
mark5 = float(input(" Enter Marks 5 : "))
e1.setRollno(r)
e1.setName(nm)
e1.setmarks1(m1)
e1.setmarks2(mark2)
e1.setmarks3(mark3)
e1.setmarks4(mark4)
e1.setmarks5(mark5)
print("Rollno : ",e1.getRollno())
print("Name : ",e1.getName())
print("Marks 1 : ",e1.getmarks1())
print("Marks 2 : ",e1.getmarks2())
print("Marks 3 : ",e1.getmarks3())
print("Marks 4 : ",e1.getmarks4())
print("Marks 5 : ",e1.getmarks5())

e1.calculate()
print("Total marks : ", e1.gettotal())
print("Percentage : ",e1.per)
        
        
    
