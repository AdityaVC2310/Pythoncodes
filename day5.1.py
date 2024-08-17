#Sample data (Monthly compounded) and Output:

def calculate_future_value(principal, interest_rate, years):

    for i in range(1, years+1):
        future_value = principal * (1 + (interest_rate / 100 / 12))**(i * 12)
        
        print(i,future_value)
        
    

# Input values
principal = float(input("Input the investment amount: "))
interest_rate = float(input("Input the rate of interest: "))
years = int(input("Input number of years: "))

#call
res= calculate_future_value(principal,interest_rate,years)
 