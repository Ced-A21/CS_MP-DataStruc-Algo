import datetime
from datetime import datetime

class Pet:
    def __init__(self, name, breed, id,startDateTime, endDateTime, roomNo , service, ownerID):
        self.name = name
        self.breed = breed
        self.id = id
        self.startDateTime = startDateTime
        self.endDateTime = endDateTime
        self.roomNo = roomNo
        self.service = service
        self.ownerID = ownerID
    
    def getData(self):
        return f"{self.name};{self.breed};{self.id};{self.startDateTime};{self.endDateTime};{self.roomNo};{self.service};{self.ownerID}\n"

    def getDateTime(self):
        return (self.startDateTime, self.endDateTime)

    #functions for avl trees
    def __eq__(self,other):
        return self.id ==  other.id
        
    def __lt__(self, other):
        return (self.startDateTime,self.endDateTime,) < (other.startDateTime,other.endDateTime)

    def __gt__(self,other):
        return (self.startDateTime,self.endDateTime,) > (other.startDateTime,other.endDateTime)


    def __contains__(self, other):
        return (self.startDateTime<other.startDateTime and other.startDateTime<self.endDateTime) or (self.startDateTime<other.endDateTime and other.endDateTime<self.endDateTime)

    def __str__(self):
        return f"{self.id} - {self.name}"



