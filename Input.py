from Validation import *
from datetime import datetime
from Pet import *
from Customer import *
from PetTree import *
from HotelData import *
from TextFile import *

#creates pet ID
def petID(room, start, end):
    rep = ":'- "
    for i in rep:
        start = str(start).replace(i, '')
        end = str(end).replace(i, '')
    return f'{room}_{start}_{end}'


#creates customer ID
def custoID(first, last, middle):
    num = ''.join([str(ord(i)) for i in f"{first}{middle[0]}" ])
    return f'{last}{num}'


#gets the Start and End DateTime of pet
def GetDateTime(msg,startDate=None):
    while True:
        try:
            print(f'\nEnter {msg} Date')
            year = getDateTime("year","%Y")
            month = getDateTime('month',"%m")
            day = getDateTime('day',"%d")
            print(f'\nEnter {msg} Time')
            hour = getDateTime('hour',"%H")
            min = getDateTime('min',"%M")

            format1= f'{day.day}/{month.month}/{year.year} {hour.hour}:{min.minute}:{00}'
            format2 = f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
            DateTime = datetime.strptime(format1, "%d/%m/%Y %H:%M:%S")
            currTime = datetime.strptime(format2, "%d/%m/%Y %H:%M:%S")

            if DateTime < currTime:
                print()
                print("DateTime is less than the current time")
                print()
                raise Exception    
            elif startDate is not None and DateTime<=startDate:
                print()
                print("End DateTime is less than or equal to the start Date")
                print()
                raise Exception
            print("%s Date Time %s added"%(msg,DateTime))
            return DateTime
        
        except:
            print('\n  ----Invalid Date Input----')
            print()

maxRoom = 100
def GetRoom():
    roomNo = None
    while True:
        roomNo = getInt('room','R')
        if 1<=roomNo and roomNo <= maxRoom:
            break
        else:
            print()
            print('  ----Invalid  Input----')
            print()
    return "R%02d"%roomNo


#gets the package choice of customer
def getPackage():
    package = None
    while True:
        print()
        print(" ========================== Paws Patrol Services ===============================")
        print()
        print("""Package                      SERVICES                       PRICES

Package A                   Meal                            Php. 199  per day
Package B                   Meal+bath                       Php. 299  per day
Package C                   Meal+bath+clothes               Php. 499  per day""")

        print()
        package = getString("package")
        if(package in packageServices):
            return package
        else:
            print()
            print("Invalid package.")
            print()


#displays taken timeslot of chosen room
def displayTimeSlot(roomNo,roomTable):
    print()
    print("=======================")
    print()
    print("Time Slot on room %s"%roomNo)
    print()
    print("-----------------------")
    print()
    if(roomNo not in roomTable):
        print("Room %s has no current reservation/check in."%roomNo)
        print()
    else:
        root = roomTable[roomNo].root
        roomTable[roomNo].displayTimeTable(root)
    print("------------------------\n")

#gets the available DateTime in chosen room
def GetAvailDateTime(roomTable, roomNo):
    pet_startDateTime = None
    pet_endDateTime = None
    while True:
        displayTimeSlot(roomNo,roomTable)
        try:
            print()
            print("Paws Patrol Services")
            print()
            print("  CheckIn Hour rate is P%s"%77)
            pet_startDateTime = GetDateTime('Start')
            pet_endDateTime = GetDateTime('End',pet_startDateTime)
            if roomNo not in roomTable:
                return (pet_startDateTime,pet_endDateTime)
            elif roomTable[roomNo].isAvailTime((pet_startDateTime,pet_endDateTime)):
                return (pet_startDateTime,pet_endDateTime)
            else:
                print()
                print("Conflict Time within the Room.\n")
                displayTimeSlot(roomNo,roomTable)
        except Exception as e:
            print()
            print("----Error-----")
            print()
            print(e)

#add pet data
def AddPet(roomTable,numPet, custo_id):
    print('\nPet %d Information'%numPet)
    print()
    pet_name = getString('pet name')
    pet_breed = getString('pet breed')
    pet_room = GetRoom()
    pet_startDateTime, pet_endDateTime = GetAvailDateTime(roomTable,pet_room)
    pet_id = petID(pet_room, pet_startDateTime, pet_endDateTime)
    pet_services = getPackage()

    pet =  Pet(pet_name, pet_breed, pet_id, pet_startDateTime, pet_endDateTime, pet_room,pet_services, custo_id)
    savePetData(pet)
    return pet

#add customer data 
def AddCustomer(roomTable):
    print('\nCustomer Information')
    print()
    first = getString('first name')
    last =  getString('last name')
    middle =  getString('middle name')
    custo_name = f'{first} {middle} {last}'
    custo_contact = getStringContact('contact number')
    custo_email = getEmail('email')

    custo_id = custoID(first, last, middle)
    petList = []
    petQty = 0
    while True: 
        currPet = AddPet(roomTable,petQty+1, custo_id)
        if(currPet.roomNo not in roomTable):
            roomTable[currPet.roomNo] = PetTree()
        roomTable[currPet.roomNo].add(currPet)
        petList.append(currPet)
        petQty+=1
        print()
        print("Pet %s Added Successfully"%currPet.name)
        print()
        choice = None
        while True:
            choice = input('Add again? [Y/N]: ').upper()
            if(choice =="Y" or choice=="N"):
                break
            else:
                print()
                print('Invalid Input')
                print()
        if choice == "N":
            break   
        elif choice == "Y":
            continue

    return Customer(custo_name, custo_id, custo_contact, custo_email, petList)


