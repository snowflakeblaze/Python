##Create a program that does the following:  Ask the user to enter a positive integer number.  
##If the number is less than zero display “Negative Number”.  
##Otherwise, display a name based on the following: numbers from 50 – 99 display your name, 
##numbers 100 or greater display “John Doe”, any other numbers display “No Name”.

print ("\nWelcome")
print ("\nThis program will display a number based on your input value\n\n")

def determine_output_value(input_number):
    if(input_number >= 0 and input_number <=49):
        print ("\nNo Name")
    elif(input_number >= 50 and input_number <= 99):
        print ("\nPritesh")
    elif(input_number >= 100):
        print ("\nJohn Doe")

user_input = int(input("Please enter an positive integer number\n"))
if user_input < 0:
    print ("\nNegative Number")
elif user_input >= 0:
    determine_output_value(user_input)

print ("\n\nHave a Great Day\n")
