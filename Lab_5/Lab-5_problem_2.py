##Write a program that will reverse a newly created array of at least 10 elements. 
##After reversing the array, delete whatever element is in the seventh position, 
##and print the array again.

print ("\nWelcome!\n")
print ("This program will reverse a newly created array\n")

answer = ""
names = []

def initial_input():
    for x in range(10):
        names.append(input("\nPlease enter a name\n"))
    return 
    
def adding():    
    names.append(input("\nPlease enter a name\n"))
    return


initial_input()
while answer != "n":
    answer = input("\nWould you like to try again?\n\tyes = y\tno = n\n")
    if(answer == "n"):
        print ("\n\nThank You\n\n")
    elif(answer == "y"):
        adding()

names.reverse()
names.pop(6)
print ("The following array has removed the seventh name\n\n")
print (names)