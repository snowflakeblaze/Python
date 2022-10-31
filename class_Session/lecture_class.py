##Opens file and reads
file = open("class_Session/names.txt", "r") 
print (file.read())
file.close

##Opens and closes file for you & reads every line in the file
with open("class_Session/names.txt", "r") as file:
    for line in file:
        print(line)
