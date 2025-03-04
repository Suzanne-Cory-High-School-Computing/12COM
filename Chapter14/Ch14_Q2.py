class Product: # create a class product with 5 variables and 2 methods
    def __init__(self,name,amount,price):
        # abstraction - we just need name of item
        # amount of this item in inventory
        # regular price without discount
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self,number):
        if number < 10:
            discount_price = 1 * self.price # no discount
        elif number < 99:
            discount_price = 0.9* self.price # 10 percent discount
        else:
            discount_price = 0.8 * self.price # 20 percent discount
        return discount_price
    
    def make_purchase(self,number):
        new_price = self.get_price(number) # get the discounted price
        self.amount -= number # decrease inventory
        return new_price

# taking in user inputs
item = input('What is the item you would like to add in the inventory? ')
inventory_amount = eval(input('How many are in stock? '))
regular_price = eval(input('What is the regular price of this item? '))

bought = Product(item,inventory_amount,regular_price) # declare bought object of type Product
number = eval(input('How many would you like to buy? '))
item_price = bought.make_purchase(number) # call the method of class Product

print('The cost of',bought.name,'after discount is',round(item_price))
print('The regular price of',bought.name,'is',bought.price)
print('We have',bought.amount,'of this item left in the inventory.')