from datetime import datetime
from HashTable import *
from TextFile import *

def getCustomer(custoTable):
    while True:
        custo_ID = input('Enter customer ID: ')

        if custo_ID in custoTable:
            return custoTable[custo_ID]
        else:
            print()
            print('Customer {custo_id} not found')
            print()

def FindPet(petList):
    #show pet list
    petTable = HashTable()
    print("--Pet ID--")
    for pet in petList:
        petTable[pet.id] = pet
        print(pet.id,"-",pet.name)
    petID = None
    # pet 
    while True:
        petID = input('Enter pet ID: ')

        if petID in petTable:
            return petTable[petID]
        else:
            print()
            print('Pet {petID} not found')
            print()



def manualCheckOut(roomTable,customerTable):
    print()
    print("Check Out Pet")
    print()
    customer = getCustomer(customerTable)
    pet_list = customer.petList
    pet = FindPet(pet_list)
    roomTable[pet.roomNo].remove(pet)
    customer.petList.remove(pet)

    if(not customer.petList):
        customerTable.delete(customer.id)
        saveData(custo_path,customerTable)
    saveAllPetData(pet_path,customerTable)

def selfCheckOut(roomTable,customerTable,isDelete=True,msg="Self-check out"):
    keyVal = roomTable.items()
    petTimeOut = []
    print(msg)
    print("--------------------")
    print()
    for key,val in keyVal:
        minPet = val.findMinimumTime()
        if(minPet is not None and minPet.endDateTime<=datetime.now()):
            print("%s (%s to %s)"%(minPet,minPet.startDateTime,minPet.endDateTime))
            if(not isDelete):
                continue
            roomTable[minPet.roomNo].remove(minPet)
            ownerID = minPet.ownerID
            customerTable[ownerID].petList.remove(minPet)
            if(len(customerTable[ownerID].petList)==0):
                customerTable.delete(ownerID)
    print("--------------------")
    saveData(custo_path,customerTable)
    saveAllPetData(pet_path,customerTable)


def ShowCheckout(roomTable, customerTable):
    while True:
        print('\n----------------------------------')
        print()
        option = input("""Checkout MENU\n
[1] Show Overtimed pets
[2] Self Check-Out (Overtimed pets)
[3] Manual Check-Out
[4] Exit\n
Enter choice: """)
        if option == "1":
            selfCheckOut(roomTable,customerTable,False,"Show OverTimed Pets")

        elif option == "2":
            selfCheckOut(roomTable,customerTable,True,"Check out OverTimed Pets")
        elif option == "3":
            manualCheckOut(roomTable,customerTable)
        elif option == "4":
            break

        else:
            print()
            print('Invalid Input')
            print()


