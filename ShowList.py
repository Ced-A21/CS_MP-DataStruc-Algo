def menu():
    print(''' Show Menu
    [1] - Show pet list (order by checkin time)
    [2] - Show customer list (order by checkin time)
    [3] - Exit this menu
    ''')
def showListChoice(custoTable):
    while True:
        menu()
        option = input("Enter your choice: ")
        if option in ("1", "2", "3"):
            if option == "1":
                showPetList(custoTable)
            elif option == "2":
                showCustomerList(custoTable)
            elif option == "3":
                break
        else:
            print()
            print("Invalid input, please try again.")
            print()


def showPetList(hashTable):
    keyVal = hashTable.items()
    petAllList = []
    for key,custo in keyVal:
        petAllList.extend(custo.petList)
    mergeSort(petAllList)
    displayList("Pet Lists",petAllList)

def showCustomerList(hashTable):
    keyVal = hashTable.items()
    customerAllList = []
    for key,custo in keyVal:
        if(not custo.petList):
            continue
        customerAllList.append(custo)
    mergeSort(customerAllList)
    displayList("Customer Lists",customerAllList)

def displayList(msg,lst):
    print("====== %s ======"%msg)
    for elem in lst:
        print(elem)
    print("-----------------")

#merge sort
def mergeSort(lst):
    if(len(lst)<=1):
        return
    mid = len(lst)//2
    leftSubList = lst[0:mid]
    rightSubList = lst[mid:]
    mergeSort(leftSubList)
    mergeSort(rightSubList)
    i = 0
    j = 0
    k = 0
    #sort 
    while i < len(leftSubList) and j < len(rightSubList):
        if leftSubList[i] < rightSubList[j]:
            lst[k] = leftSubList[i]
            i += 1
            k += 1
        else:
            lst[k] = rightSubList[j]
            j += 1
            k += 1
    #if there is an element left on the left sublist
    for i in range(i,len(leftSubList)):
        lst[k] = leftSubList[i]
        k += 1
    #if there is an element left on the right sublist
    for j in range(j,len(rightSubList)):
        lst[k] = rightSubList[j]
        k += 1
