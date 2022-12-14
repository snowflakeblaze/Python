## Write a program that will prompt the user to enter an integer number between 1 and 12. 
## Your program should take the input given by the user and display which month the number corresponds to. 
## Additionally, you should also display how many days are typically in that month. 
## For example, if the user inputs ‘2’, your program should display: “The month (2) selected is February, it has 28 days.”. 
## If the user does not enter a number between 1 and 12, your program should display “Please enter a number between 1 and 12”.

print ("\n\nWelcome\n\n")

##Checks the corresponding user input with the list to get the month 
def determine_month(integer_input):    
    if integer_input == 2:
        return "\n\nThe number you chose corresponds to\n \t>>> Febuary <<<"
    elif integer_input == 3:
        return "\n\nThe number you chose corresponds to\n  \t>>> March <<<"
    elif integer_input == 4:
        return "\n\nThe number you chose corresponds to\n  \t>>> April <<<"
    elif integer_input == 5:
        return "\n\nThe number you chose corresponds to\n  \t>>> May <<<"
    elif integer_input == 6:
        return "\n\nThe number you chose corresponds to\n  \t>>> June <<<"
    elif integer_input == 7:
        return "\n\nThe number you chose corresponds to\n  \t>>> July <<<"
    elif integer_input == 8:
        return "\n\nThe number you chose corresponds to\n  \t>>> August <<<"
    elif integer_input == 9:
        return "\n\nThe number you chose corresponds to\n  \t>>> September <<<"
    elif integer_input == 10:
        return "\n\nThe number you chose corresponds to\n  \t>>> October <<<"
    elif integer_input == 11:
        return "\n\nThe number you chose corresponds to\n  \t>>> November <<<"
         

##Checks the corresponding user input with the list to get the amount of days
def determine_days(user_number):
    if (user_number == 3 or 
        user_number == 5 or 
        user_number == 7 or 
        user_number == 8 or 
        user_number == 10):
        return "\nThere are \n\t>>> 31 Days <<<\n in this month\n\n"
        
    elif (user_number == 4 or 
        user_number == 6 or 
        user_number == 9 or 
        user_number == 11):
        return "\nThere are \n\t>>> 30 Days <<<\n in this month\n\n"
        
    elif (user_number == 2):
        return "\nThere are \n\t>>> 28 Days <<<\n in this month\n\n"            

##Ensures the user selects a number in order to provide a output
while True:
    user_input = int(input("please enter a number between 1 and 12\n"))
    if user_input != 1:
        if user_input != 12:
            print (determine_month(user_input))
            print (determine_days(user_input))
            print ("\nHave a Great Day!\n")
            break
        else:
            print("\nYou have made an invalid selection, you must choose a number between 1 and 12.\n") 
    else:
        print("\nYou have made an invalid selection, you must choose a number between 1 and 12.\n") 
