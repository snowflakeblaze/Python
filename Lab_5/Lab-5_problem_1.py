##Write a program that declares an array of names that is at least of size 6. 
##After the array has been declared, you should print out the very first element, 
##along with the third and sixth element of the array individually.

print ("\nWelcome!\n")
print ("This program will add 6 names to the array\n")

names = []

for x in range(6):
    names.append(input("\nPlease enter a name\n"))



print ("\n\nThe First Element in the array is: \n" + names[0])

print ("\n\nThe Third Element in the array is: \n" + names[2])

print ("\n\nThe Sixth Element in the array is: \n" + names[5])


print ("\nHave a Great Day!\n\n")