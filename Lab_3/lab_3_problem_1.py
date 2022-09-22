##Create a program that asks the user to enter the costs for the following expenses incurred from operating his or her automobile:  
## loan payment, insurance, gas, oil, tires, and maintenance.  
## The program should then display the total cost of these expenses.


print ("\n\nWelcome")
print ("\nCalculate your total expense for using your automobile\n\n")

loan_payment = float(input("Please enter your monthly loan payment: \n\t"))
insurance = float(input("\nPlease enter your monthly insurance fees: \n\t"))
gas = float(input("\nPlease enter your monthly gas expenses: \n\t"))
oil = float(input("\nPlease enter your monthly oil expense: \n\t"))
tires=  float(input("\nPlease enter your monthly expense on tires: \n\t"))
maintenance = float(input("\nPlease enter your monthly expense on your automobile maintenance: \n\t"))

monthly_expense = loan_payment + insurance + gas + oil + tires + maintenance
yearly_expense = ((loan_payment + insurance + gas + oil + tires + maintenance) * 12)

print ("\nYour total monthly expense for your automobile is: $ " + str(round(monthly_expense, 2)))

print ("\nYour total expense per year for your automobile is: $ " + str(round(yearly_expense, 2)))

print ("\n\nThank you \nHave a great day")

print("\n\n\n")