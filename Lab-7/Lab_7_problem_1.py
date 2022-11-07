##Create a menu-driven program that starts by displaying a menu of a restaurant to a user. 
##The user should have at least 5 distinct food items to choose from on the menu, along with their prices. 
##The user should be prompted for their input (what food they want to order) until the user decides to finish their order. 
##Display to the user what they ordered and what it costs.
##BONUS: Display to the user the sub-total and tax.

print ("\n\nWelcome\n")

order = []
ammount = []

def menu():
    print("\t\n\n> > >> > > Menu < < << < <")
    print("\n\t 1. Burger\t $ 7,50")
    print("\t 2. Sandwich\t $ 8,50")
    print("\t 3. Wrap\t $ 9,50")
    print("\t 4. Hotdog\t $ 10,50")
    print("\t 5. Taco\t $ 5,50")
    print("\t 6. Fries\t $ 7\n")    
    print("\t\t 7. Exit\n")


def storeItem(item):
    return order.append(item)


def storePrice(price):
    return ammount.append(price)

def main():
    while(True):
        menu()
        choice = input("Please enter a choice (1 - 7): ")
        
        if choice == "1":
            item = ("Burger")
            price = (7.50)
            storeItem(item)
            storePrice(price)
        
        elif choice == "2":
            item = ("Sandwich")
            price = (8.50)
            storeItem(item)
            storePrice(price)
            
        elif choice == "3":
            item = ("Wrap")
            price = (9.50)
            storeItem(item)
            storePrice(price)
            
        elif choice == "4":
            item = ("Hotdog")
            price = (10.50)
            storeItem(item)
            storePrice(price)
            
        elif choice == "5":
            item = ("Taco")
            price = (5.50)
            storeItem(item)
            storePrice(price)

        elif choice == "6":
            item = ("Fries")
            price = (7.00)
            storeItem(item)
            storePrice(price)

        elif choice == "7":
            print ("Your Order is: \n\n")

            for x in range(0, len(order)):
                if(order[x] == "Sandwich"):
                    print("\t" + order[x] + "\t$ " + str(ammount[x]))
                elif(order[x] != "Sandwich"):
                    print("\t" + order[x] + "\t\t$ " + str(ammount[x]))
            
            taxTotal = 0
            orderTotal = 0
            for x in range(0, len(ammount)):                
                orderTotal = orderTotal + float(ammount[x])               
                taxTotal = taxTotal + (0.07 * float(ammount[x]))
                subtotalamount = orderTotal + taxTotal
            print("----------------------------------")
            print ("\n\tTotal:\t\t$ " + '{0:.2f}'.format(float(orderTotal)))
            print ("\n\tTax:\t\t$ " + '{0:.2f}'.format(float(taxTotal)))
            print ("\n\tSub-Total:\t$ " + '{0:.2f}'.format(float(subtotalamount)))


            print ("\n\n")

            
            print("Exiting...\n\n")
            break
            
        else:
            print("Please enter a valid selection")

main()