#TIP CALCULATOR

print("Welcome to the tip calculator!")

subTotal = input("What is the total cost of your bill?")

tipInput = input("What percentage tip are you looking to give?")

tipPercentage = int(tipInput) / 100

tipAmount = float(subTotal) * float(tipPercentage) 

totalBill = float(subTotal) + tipAmount

print("You will be tipping $" + "{:,.2f}".format(tipAmount) + ". The total bill including the tip will be $" + "{:,.2f}".format(totalBill))