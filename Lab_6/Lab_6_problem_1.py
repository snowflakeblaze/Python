print ("\n\nHello")

print ("\nThis program will read and write to a text file \n\n")

f = open("myfile.txt", "w")
f.write("Hello from ITS140 in Hammond, Indiana.\n")
f.close()
f = open("myfile.txt", "r")
print(f.read())
f.close()
print ("\n\nThis will now print out all content from the textfile after a new line has been added.\n\n")
f = open("myfile.txt", "a")
f.write("This is a new appended line\n")
f.close()

f = open("myfile.txt", "r")
print(f.read())
f.close()