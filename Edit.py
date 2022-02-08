from Input import *
from HashTable import *


def getCustomer(custoTable):
    while True:
        custo_ID = input('Enter customer ID: ')

        if custo_ID in custoTable:
            return custoTable[custo_ID]
        else:
            print('Customer {custo_id} not found')

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
            print('Pet {petID} not found')


def AddAdditionalPet(custoTable,roomTable):
    customer = getCustomer(custoTable)
    currPet = AddPet(roomTable,len(customer.petList)+1,customer.id)
    customer.petList.append(currPet)

def EditCheckInOutPet(custoTable,roomTable):
    customer = getCustomer(custoTable)
    pet_list = customer.petList
    pet = FindPet(pet_list)
    #delete in avl tree
    roomTable[pet.roomNo].remove(pet)
    #change date time and time
    pet.startDateTime,pet.endDateTime = GetAvailDateTime(roomTable,pet.roomNo)
    pet.id = petID(pet.roomNo, pet.startDateTime, pet.endDateTime)
    #add again in avl tree
    roomTable[pet.roomNo].add(pet)


def ShowEdit(custoTable,roomTable):
    while True:
        print('\n----------------------------------')
        option = input("""MENU\n
[1] Edit Check In/Check Out
[2] Add Pet
[3] Exit\n
Enter choice: """)
        if option == "1":
            EditCheckInOutPet(custoTable,roomTable)

        elif option == "2":
            AddAdditionalPet(custoTable, roomTable)
            
        elif option == "3":
            break

        else:
            print('Invalid Input')