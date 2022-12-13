##Create a program with at least 3 functions. 
##One of these functions should accept one argument, and 
##then return that argument with text appended to it. 
##A second function should accept two arguments, and return 
##the remainder of the division of those two arguments. Finally, 
##your third function should not have any arguments, 
##it should only print out a message when called. (20 points)

print ("\nWelcome")

def menu():
    print("\t\nMenu")
    print("\t1. First Function")
    print("\t2. Second Function")
    print("\t3. Third Function")
    print("\t4. Exit\n\n")

def first_function(argument_1):
    return "\n\nThis is the first function with text appended to the argument, 'He is having a " + argument_1 + " day'"

def second_function(num_1, num_2):
    return "\n\nThe remainder of the devision is: " + str(num_1%num_2)

def third_function():
    return "\n\nThank you for a Fantastic semester, \nI have had a great time learning from you\nMerry Christmass, Lance\n "

def main():
    while(True):
        menu()
        choice = input("\nPlease enter a choice (1 - 4): \n")
        
        if choice == "1":
            user_input = input("How is your day?\n")
            print(first_function(user_input))
        
        elif choice == "2":
            choice1 = int(input("\n\nPlease enter a number bigger than 100\n"))
            choice2 = int(input("\n\nPlease enter a number less than 15\n"))
            print(second_function(choice1, choice2))
            
        elif choice == "3":
            print(third_function())
            
            
        elif choice == "4":
            print("Exiting...")
            break
            
        else:
            print("Please enter a valid selection")

main()