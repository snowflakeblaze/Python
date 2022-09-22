##Design a program that calculates the total amount of a meal purchased at a resturant.
##The program ahould ask the user to enter the charge for the food, and then 
##calculate the amount of a 15 percent tip and 7 percent sales tax.
##Display each of these amounts and the total.

print ("\n\n\t\t\tWelcome")
print ("This program will calculate the total amount, tip, and tax\n\n")

meal_price = float(input("PLease enter the price of the food: \n"))

def calculate_tip(cost):
    tip = (0.15 * cost)
    return tip


def calculate_tax(cost):
    tax = (0.07 * cost)
    return tax

def calculate_total_amount(cost, tax, tip):
    amount_due = (tax + tip + cost)
    return amount_due

tip = round(calculate_tip(meal_price), 2)
tax = round(calculate_tax(meal_price),2)
amount_due = round(calculate_total_amount(tip, tax, meal_price), 2)

print ("\n\nTax amount: $ " + str(tax))
print ("\nTip amount: $ " + str(tip))
print ("\n\nYour total amount due is: $ " + str(amount_due))
print ("\n\nHave a Great Day\n\n")