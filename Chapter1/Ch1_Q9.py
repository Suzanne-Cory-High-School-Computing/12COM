mealPrice = eval(input("What is the price of your meal? "));
tip = eval(input("What tip percentage would you like to leave? "));
tipPercent = tip/100 + 1;
print("Your meal amount is", mealPrice);
print("With the tip included, the total bill is", mealPrice*tipPercent);