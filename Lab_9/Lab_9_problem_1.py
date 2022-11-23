##Create a program that will accept an input string from a user. 
##The string must be at least 5 characters long. 
##Once the user has provided the correct string, 
##reverse the string the user provided and 
##create a new string with the first, last, and 
##middle character in that order.

def reverse(string):
    string = string[::-1]
    return string


user_input = input(print("\n\nPlease enter a input string\nThe input should more than 5 characters\n"))
if(len(user_input) >= 5):
    reversed_input = reverse(user_input)
    string_len = len(reversed_input)

   

final = reversed_input[0]
middle = int(string_len / 2) 

final = final + reversed_input[middle] 
final = final + reversed_input[string_len - 1] 
print("-----------Output-----------")
print("The original input it: " + user_input)
print("The reversed input it: " + reversed_input)
print("String after manipulation: ", final)
