#Capacity for internal array
import random
from LinkedList import *


class HashTable:
    #Initialization of Has table
    def __init__(self,Initial_Capacity = 20):
        self.capacity = Initial_Capacity
        self.size = 0
        self.slots = [LinkedList() for i in range(self.capacity)]

    #Generate Hash for a given key
    #Input: key - string
    #Output: Index from 0 to self.capacity which is 20
    def hash(self, key):
        hashtotal = 0
        #For loop, each character in the key
        #R213
        if(len(key)>=5):
            key = key[:5]

        for i, c in enumerate(key):
            #insert (index + length of key) ^ (current char code)
            hashtotal += (i + len(key)) ** ord(c)
            # Perform modulus to keep hashtotal in range[0, self.capacity - 1]
            hashtotal = hashtotal % self.capacity
        return hashtotal 

    #Insert function
    #Insertion of key, value pair to the hashtable
    def __setitem__(self, key, value):
        if(self.size+1>self.capacity):
            self.resize()

        key = str(key)

        #2. Compute index of the key
        index = self.hash(key)
        #Go to the node corresponding to the hash
        node = self.slots[index]
        # 3. If Slot is empty:
        if not node:
            #This creates the node if the Node is empty
            node.addAtHead(HashNode(key, value))
            self.size += 1
            return
        #chain collision
        currList  = self.slots[index]
        currNode = currList.search(key) 
        if(currNode is None):
            currList.addAtHead(HashNode(key, value))
            self.size += 1
        else:
            currNode.val = value

    def getLength(self):
        return self.size

    def setNewItem(self, newSlots,hashNode):
        #2. Compute index of the key
        index = self.hash(hashNode.key)
        #Go to the node corresponding to the hash
        linkedList = newSlots[index]
        # 3. If Slot is empty:
        if not linkedList:
            #This creates the node if the Node is empty
            linkedList.addAtHead(hashNode)
            return
        #chain collision
        currList  =  newSlots[index]
        currList.addAtHead(hashNode)


    def resize(self):
        self.capacity = self.capacity * 2
        newSlots = [LinkedList() for i in range(self.capacity)]
        for ind, hashNodeList in enumerate(self.slots):
            items = hashNodeList.getItems()
            for key,value in items:
                self.setNewItem(newSlots,HashNode(key,value))
        self.slots = newSlots


    def __contains__(self, key):
        index = self.hash(key)
        #Go to the node corresponding to the hash
        linkedList = self.slots[index]
        # 3. If Slot is empty:
        if linkedList.isEmpty():
            return False
        #chain collision
        currList  = self.slots[index]
        currNode = currList.search(key) 
        if(currNode is None):
            return False
        else:
            return True
        return False
       

    #Delete node stored at key
    def delete(self, key):
        #Get Hash
        index = self.hash(key)
        linkedList = self.slots[index]
        linkedList.delete(key)
        self.size -= 1
       

    def __getitem__(self, key):
        index = self.hash(key)
        if self.slots[index] is None:
            return None
        else:           
            return self.slots[index].search(key).val

    def display(self):
        for slot in self.slots:
            slot.traverse()

    def items(self):
        items = []
        for linkedList in self.slots:
            if linkedList.isEmpty():
                continue
            items.extend(linkedList.getItems())
        return items
