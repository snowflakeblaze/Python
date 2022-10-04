##Create a program that outputs every odd number from 1 to 100, every even number should say your name.

print ("\nWelcome\n")
print ("\nThis program will display every odd number\nAnd every even number will be displayed with my name\n")

for x in range(100):
    if(int(x + 1) % 2 != 0):
        print (str(x+1))
    elif (int(x + 1) % 2 == 0):
        print ("Pritesh")

print ("\nTHis is the end")
print ("\nHave a Great Day!\n\n")