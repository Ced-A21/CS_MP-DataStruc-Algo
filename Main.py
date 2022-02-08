from Input import *
from HashTable import *
from PetTree import *
from Receipt import *
from CheckOut import *
from Edit import *
from ShowList import *
from TextFile import *


#main method
def main():

    #main data structure
    custoTable = HashTable()
    roomTable = HashTable()

    #retrieval of data
    retrieveCustomerData(custoTable)
    retrievePetData(roomTable, custoTable)

    print("=========== Pet Paw Hotel System =============")
    while True:
        choice = input("""\n\nMENU\n
[1] Check In/Reserve
[2] Show List of Customers and Pets
[3] Edit Existing Pet / Add Pet
[4] Check Out
[5] Exit\n
Enter choice: """)

        if choice == "1":
            currCustomer = AddCustomer(roomTable)
            custoTable[currCustomer.id] = currCustomer
            GetReceipt(currCustomer)
            saveCustomerData(currCustomer)

        elif choice == "2":
            showListChoice(custoTable)

        elif choice == "3":
            ShowEdit(custoTable,roomTable)
            pass

        elif choice == "4":
            ShowCheckout(roomTable, custoTable)

        elif choice == "5":
            break

        else:
            print()
            print("Invalid Input")
            print()
    print("Thank you for using...")
main()


