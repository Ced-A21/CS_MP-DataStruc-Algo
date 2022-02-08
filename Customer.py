import random


class Customer():

    
    def __init__(self, cust_name, cust_id, cust_cotact , cust_email, petlist = None):
    
        self.name = cust_name
        self.id = cust_id
        self.contact = cust_cotact
        self.email = cust_email
        self.petList = petlist
    
    def getData(self):
        return f"{self.name};{self.id};{self.contact};{self.email}"

    def printData(self):
        print(self.name, self.id, self.petList)
    
    def __eq__(self,other):
        return self.name == other.name and self.name == other.name
        
    def __lt__(self, other):
        return (self.name) < (other.name)

    def __gt__(self,other):
        return (self.name) < (other.name)


    def __contains__(self, other):
        return (self.name<=other.name and other.name<self.name) or (self.name<other.name and other.name<self.name)

    def __str__(self):
        return f"{self.id} - {self.name}"





# def genID(first,last,middle):
    
#     num = ''.join([str(ord(i)) for i in f"{x[0]}{x[2]}" ])
#     ID =f'{x[1]}{num}'
#     return ID

# n1  = ["NIKKA", "HABER", "A"]
# n2  = ["SIMON", "ASINO", "G"]
# n3  = ["CED", "ALON", "B"]
# n4 = ["JAMES", "PAZ", "E"]
# n5 = ["DANN", "DIWA", "E"]

# p1 = Customer(n1[0], genID(n1),"chowchow, kia,pia")
# p2 = Customer(n2[0], genID(n2),"lia, pia, kula")
# p3 = Customer(n3[0], genID(n3),"bulldog, chuaahahha, hi")
# p4 = Customer(n4[0], genID(n4),"jwhjwf, hi, hello")
# p5 = Customer(n5[0], genID(n5),"pia, ju, ki")

# p1.printData()
# p2.printData()
# p3.printData()
# p4.printData()
# p5.printData()
#Hi guys
# customers = [p1, p2, p3, p4, p5]

# customers.sort(key=lambda s: s.name) 

# print(end=' ')

# for persons in customers:
# 	print(persons.name, end=" ")
# customers.sort(key=lambda s: s.name, reverse=True) 



