##Create a program that asks the user to enter the current temperature.  
##Display the appropriate message from the following table based on 
##the temperature entered. (25 points)

def tempreture_message(user_input):
    if(user_input < 32):
        return "\nIt's Cold"
    elif (user_input >= 32 and user_input <= 80):
        return "\nIt's Moderate"
    elif (user_input > 80):
        return "\nIt's Hot"

print ("\n\nWelcom20e\n")

tempreture_input = int(input("Please Enter the current tempretuure\n"))

print(tempreture_message(tempreture_input))