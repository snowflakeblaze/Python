##Use a loop to traverse an array and display the length of a declared array of at least 10 integer elements. 
##Afterwards, use a built-in function that will return the length of your array. Are they the same length? 
##Print out both lengths and compare.

print ("\nWelcome!\n")
print ("This program will traverse an array & display the length\n")

numbers = [1,2,3,4,5,6,7,8,9,10]

for x in numbers:
    print (numbers[x-1])

print ("\n\nThe length of the array is: " + str(len(numbers)) + "\n\n")