weight = eval(input("Enter the weight in kilograms: "))
while (weight < 0):
    print("You have entered an invalid weight, please try again")
    weight = eval(input("Enter the weight in kilograms: "))
converted = weight * 2.2
print(weight,'kilograms equals',converted,'pounds')   