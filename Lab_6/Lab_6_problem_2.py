print ("\n\nHello")

print ("\nThis program will read and write to a text file \n\n")

with open("file.txt", "a") as f:
   lines = ["Adding lines", "\nwriting into it", "\nwritten successfully" ]
   f.writelines(lines)
   f.close()

count = 0
textfileArray = []

f = open("file.txt", "r")
for line in f:
    count += 1
    textfileArray.append(str(line))
    print("Line{}: {}".format(count, line.strip()))

print ("\n\nThis will print the lines from the array\n")
for x in textfileArray:
    print(x)


print ("\n\n\tHave a Great Day\n\n")