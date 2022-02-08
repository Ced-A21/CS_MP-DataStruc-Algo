from HotelData import *


def GetReceipt(currCustomer):
    petList = currCustomer.petList
    hourPay = 0
    servicePackagePay = 0
    print("\n\n================ Receipt ================")
    print("\nCustomer Id: ",currCustomer.id)
    print("Customer Name: ",currCustomer.name)
    print("\n------------------------------------------")
    print("               Pet Info")
    print("------------------------------------------")

    for pet in petList:
        hourCheckIn = (abs(pet.startDateTime - pet.endDateTime)).days*24
        dayCheckIn = hourCheckIn/24
        print(pet)
        print(f"Room: {pet.roomNo} Stay: {hourCheckIn:.2f} hours  Package: {pet.service}")
        if(dayCheckIn<1):
           dayCheckIn = 1
        hourPay += (hourCheckIn*rateHour)
        servicePackagePay += packageServices[pet.service] * dayCheckIn
        print("------------------------------------------")

    totalPay = servicePackagePay +  hourPay

    print("\n                Bills")
    print("-------------------------------------------\n")
    print(f"Total Hour Pay: P{hourPay}")
    print(f"Total Service Package: P{servicePackagePay}\n")
    print("-------------------------------------------")
    print(f"\nTotal Bill: P{totalPay}" )
    print("\n============================================\n")

    

#whatsup