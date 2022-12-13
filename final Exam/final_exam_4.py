##Create a program that creates a text file from scratch.
##This text file should have at least 4 lines written to it; 
##with whatever text you want. Once the file has been created 
##and written to, your program should then read from the file 
##and display its contents. Append additional text to your file, 
##and read from it once again. (20 points)

print ("\nWelcome\n")

print ("\nThis program will create a text file and allow you to write to the file\n")

f = open("final_text.txt", "w")
f.write(input("\tPlease type a sentence\n") + "\n")
f.write(input("\tPLease type your favorite beverage\n") + "\n")
f.write(input("\tPlease type your favorite supercar\n") + "\n")
f.write(input("\tPlease type your holiday destination\n") + "\n")
f.close()

print ("\n\nNow the program will print text saved to the text file\n")
f = open("final_text.txt", "r")
print(f.read())
f.close()

print ("\n\nNow the program will add more text to the textfile!\n")

while (True):
    user_input = input("\n\tPlease enter more text to the file\n\tTo stop Type 'break'\n")
    if(user_input == "break"):
        print ("\n\n\tThe Following was added to the text file")
        f = open("final_text.txt", "r")
        print(f.read())
        f.close()
        break
    elif(user_input != "break"):
        f = open("final_text.txt", "a")
        f.write(user_input + "\n")
        f.close()