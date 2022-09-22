##A nutritionist who works for a fitness club helps members by evaluating their diets.  
## As part of her evaluation, she asks members for the number of fat grams and carbohydrate grams that they consumed in a day.  
## Then, she calculates the number of calories that result from the fat, using the following formula:

##	Calories from Fat = Fat Grams x 9

## Next, she calculates the number of calories that result from the carbohydrates, using the following formula:

##	Calories from Carbs = Carb Grams x 4


import math


print ("\n\nWelcome")
print ("\nI will be calculating your total calories cunsumed in a day ")

carbs = float(input("\n\nPlease enter your total carbs consumed for the day: \n\t"))
fat = float(input("Please enter your total fat consumed for the day: \n\t"))

calories = ((fat * 9) + (carbs * 4 ))

if(calories.is_integer()):
    print("\nYour toal calories consumed for the day is: " + str(math.trunc(calories)))
    print("\nHave a Great Day")
else:
    print("\nYour toal calories consumed for the day is: " + str(calories))
    print("\nHave a Great Day\n\n\n")


