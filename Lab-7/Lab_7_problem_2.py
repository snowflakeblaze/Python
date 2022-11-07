##Design a program that displays a menu allowing the user to select air,water, or steel.
##After the user has made a selection, he or she should be asked to enter the number of seconds the sound will travel in the selected medium. 
##The program should then display that distance the sound will travel.

def menu():
    print("\nMenu")
    print("1. Air")
    print("2. Water")
    print("3. Steel")
    print("6. Exit")

def air(seconds):
    return 1100 * seconds

def water(seconds):
    return 4900 * seconds

def steel(seconds):
    return 16400 * seconds

def main():
    while(True):
        menu()
        choice = input("Please enter a choice (1 - 4): \n")
        
        if choice == "1":
            seconds = int(input("\nPlease enter the ammount of seconds the sound will travel: \n"))
            print("\nAnswer: ", air(seconds))
        
        elif choice == "2":
            seconds = int(input("\nPlease enter the ammount of seconds the sound will travel: \n"))
            print("\nAnswer: ", water(seconds))
            
        elif choice == "3":
            seconds = int(input("\nPlease enter the ammount of seconds the sound will travel: \n"))
            print("\nAnswer: ", steel(seconds))
            
            
        elif choice == "4":
            print("Exiting...")
            break
            
        else:
            print("Please enter a valid selection")

main()