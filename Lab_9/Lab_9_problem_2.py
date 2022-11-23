##Create a program that will accept an input string from a user. 
##Once the string has been provided by the user, 
##your program should traverse the entire string. 
##If any digits are encountered in the provided string, 
##your program should calculate and display both the average and 
##the summation of all digits in the string.

user_input = input(print("\n\nPlease enter a input string"))

new_digit_text = ""
average = 0
total_count_added = 0
new_text = ""
digits = 0
chars = 0
symbols = 0

for letter in user_input:
    if letter.isdigit():
        digits += 1
        total_count_added = total_count_added + int(letter)     
        new_digit_text = new_digit_text + "" + letter
    elif letter.isalpha():
        chars += 1
        new_text = new_text + "" + letter
    else:
        symbols += 1
        

print("-----------Output-----------")
print("# of digits: ", digits)
print("# of chars: ", chars)
print("# of symbols: ", symbols)
print("The average of the digits in the string is: " + str((total_count_added / digits)))
print("The total sum of digits are: " + str(total_count_added))
print("The input without digits is: " + new_text)

