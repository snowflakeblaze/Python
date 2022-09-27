## A bug collector collects bugs everyday for seven days. 
## Design a program that keeps a running total of the number of bugs collected during seven days. 
## The loop should ask for the number of bugs collected for each day, and 
## when the loop is finished, the program should display the total number of bugs collected.

print ("\nWelcome\n\n")

print ("This program is going to calculate the amount of bugs you collected during the past 7 days\n\n")

bugs_collected = 0

for x in range(7):
    daily_input = int(input("Please enter how many bugs you collected on day " + str(x + 1) + ": \n"))
    bugs_collected = bugs_collected + daily_input

print ("\nTotal bugs colected: " + str(bugs_collected) + "\n\n")
print ("Have a Great Day\n")