class HashNode():
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
    def __str__(self):
        return f"<Node: ({self.key}, {self.value}), next: {self.next != None}> "
    def __repr__(self):
        return str(self)

class LinkedList:
    def __init__(self):
        self.head = None
        return


    def addAtHead(self, hashNode):
        node = hashNode
        node.next = self.head
        self.head = node

    def isEmpty(self):
        return self.head is None

    def insert(self, key, value):
        node = HashNode(key, value)
        if self.head == None:
            self.head = node
            return 0
        else:
            temp = self.head
            while temp.next:
                if temp.key == key:
                    temp.value = value
                    return 1
                else:
                    temp = temp.next

            if temp.key == key:
                temp.value = value
                return 1
            temp.next = node
            return 0

    def search(self, key):
        temp = self.head
        while temp:
            if temp.key == key:
                return temp
            else:
                temp = temp.next
        return None

    def delete (self, key):
        if self.head:
            if self.head.key == key:
                val = self.head.val
                self.head = self.head.next
                return val
            else:
                temp= self.head
                while temp.next:
                    if temp.next.key == key:
                        val = temp.next.val
                        temp.next = temp.next.next
                        return val
                    else:
                        temp = temp.next

        raise KeyError (f"this {key} that you are trying to delete does not exist.")

    def traverse(self):
        temp = self.head
        if not temp:
            return
        while temp:
            print(f"{temp.key}\t{temp.val}",end=" -> ")
            temp = temp.next
        print()

    def getItems(self):
        items = []
        temp = self.head
        while temp:
            items.append((temp.key,temp.val))
            temp = temp.next
        return items