## Write a program that will prompt the user to input an integer number. 
## The program should then take the input from the user, and 
## display to the user whether the inputted number is an even number or an odd number.

print ("\nWelcome\n\n")
another_round = ""

##function to test whether number is even or odd
def even_odd_tester(number):
    if(number % 2 == 0):
        test_result = "\nThe number you have entered is an \n>>>Even number<<<\n"
    elif(number % 2 != 0):
        test_result = "\nThe number you have entered is an \n>>>Odd number<<<\n"
    return test_result

##while loop used get user inout and repeat until cancelled 
while another_round != "n":
    user_input = int(input("PLease enter a number without any decimals\n"))
    test_result = even_odd_tester(user_input)
    print("" + test_result)
    another_round = input("Would you like to try again?\n")
    if(another_round == "n"):
        print ("\n\nHave a Great Day\n\n")
