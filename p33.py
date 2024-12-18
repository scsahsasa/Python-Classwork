class SimpleInterestCalculator:
    def __init__(self, principal, rate, time):
        self.principal = principal  
        self.rate = rate  
        self.time = time  

    def calculate_interest(self):
        
        return (self.principal * self.rate * self.time) / 100



principal = float(input("Enter the principal amount (in Rs.): "))
rate = float(input("Enter the rate of interest (per year in %): "))
time = float(input("Enter the time (in years): "))


calculator = SimpleInterestCalculator(principal, rate, time)


simple_interest = calculator.calculate_interest()
print("The Simple Interest is:", simple_interest)
