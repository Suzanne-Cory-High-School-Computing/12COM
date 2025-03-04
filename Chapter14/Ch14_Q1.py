class Investment: # create a class Investment which has 2 variables, 1 method value_after and a special __str__ method
    def __init__(self,principal,interest):
        self.principal = principal
        self.interest = interest/100 # interest rate

    def __str__(self):
        return 'Principal - ${}, Interest rate - {}%'.format(self.principal,self.interest*100)

    def value_after(self,n):
        return 'Value of {} after {} years is {}'.format(self.principal,n,round(self.principal*(1+self.interest)**n,2))
    
principal = eval(input('Enter the investment amount: '))
interest = eval(input('Enter the interest rate: '))
my_investment = Investment(principal,interest) # create a new object
print(my_investment)
n = eval(input('Enter the number of years: '))
output = my_investment.value_after(n)
print(output)