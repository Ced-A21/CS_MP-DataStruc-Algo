from Customer import *
from Pet import *
from PetTree import *
import traceback

custo_path = "Records/customer_records.txt"
pet_path = "Records/pet_records.txt"
def saveCustomerData(custo):
    file = open(custo_path,"a")
    writeFormat = f"{custo.name};{custo.id};{custo.contact};{custo.email}\n"
    file.write(str(writeFormat))
    file.close()

def retrieveCustomerData(custoTable):

    try:
        file = open(custo_path,"r")
        line = file.readlines()
        for i in line:
            data = i.strip().split(';')
            currCustomer = Customer(data[0],data[1],data[2],data[3])
            currCustomer.petList = []
            custoTable[currCustomer.id] = currCustomer
        file.close()

    except:
        pass

def saveData(path, hashTable):
    dataItems = hashTable.items()
    try:
        file = open(path,"w")
        for key,obj in dataItems:    
            file.write(obj.getData())
        file.close()
    except Exception as e:
        traceback.print_exc()

def saveAllPetData(path, customerTable):

    customerPets = []
    for key,val in customerTable.items():
        customerPets.extend(val.petList)

    try:
        file = open(path,"w")
        for pet in customerPets:    
            file.write(pet.getData())
        file.close()
    except Exception as e:
        traceback.print_exc()


def savePetData(pet):
    file = open(pet_path,"a")
    
    writeFormat = f"{pet.name};{pet.breed};{pet.id};{pet.startDateTime};{pet.endDateTime};{pet.roomNo};{pet.service};{pet.ownerID}\n"
    file.write(str(writeFormat))
    file.close()

def retrievePetData(roomTable, custoTable):
        file = open(pet_path,"r")
        line = file.readlines()
        for i in line:
            data = i.strip().split(';')
            startDateTime = datetime.strptime(data[3], "%Y-%m-%d %H:%M:%S")
            endDateTime = datetime.strptime(data[4], "%Y-%m-%d  %H:%M:%S")
            pet = Pet(data[0],data[1],data[2],startDateTime,endDateTime,data[5],data[6],data[7])
            ownerID = data[7]
            if(ownerID in custoTable):
                custoTable[ownerID].petList.append(pet)
                if(not pet.roomNo in roomTable):
                    roomTable[pet.roomNo] = PetTree()
                roomTable[pet.roomNo].add(pet)
        file.close()
