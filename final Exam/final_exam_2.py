##Create a program for the following:  
##Allow a user to input a series of ages and then calculate
##and display the total sum of all ages and the average of all ages. 
##The user should be allowed to enter ages until a 0 is entered. 
##Do not allow entry of negative numbers.  (20 points)

print ("\n\nWelcome\n")
user_input = ""
counter = 0
total_sum = 0
average = 0

while user_input != 0:
    user_input = int(input("\tPlease enter a series of ages\n\tTo stop the program type: '0' \n\n\n"))
    if(user_input < 0):
        print ("\nYou have entered an invalid number\n")
    elif(user_input == 0):
        print ("\n\nThe Total sum of all ages are: " + str(total_sum))
        print ("\n\nThe average is: " + str(average))
        print ("\nHave a Great Day")
        break
    elif(user_input > 0):
        counter = counter + 1
        total_sum = total_sum + user_input
        average = (counter / total_sum) * 100
       