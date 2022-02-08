from AVL_tree import AVL_TREE,NodeTree
class PetTree(AVL_TREE):
    def __init__(self):
        self.count = 0
        AVL_TREE.__init__(self)


    #Override add for insert only for Pet tree
    def add(self,data):
        oldCount = self.count
        def insert(root,data):
            if root is None:
                self.count += 1
                return NodeTree(data)
            elif(data in root.val):
                return root
            elif(data<root.val):
                root.left = insert(root.left,data)
            else:
                root.right = insert(root.right,data)

            # update height of the root
            root.updateHeight()
            #BF =  height(left) - height(right)
            BF = root.getBalanceFactor()
            if(abs(BF)>1):
                #BF are out of range of -1,0,1  which need to perform rotation
                #case 1 left left case
                if(BF>1 and data<root.left.val):
                    return self.rightRotate(root)
                #case 2 right right case
                elif(BF<-1 and data>root.right.val):
                    return self.leftRotate(root)
                #case 3 left right case
                elif(BF>1 and data>root.left.val):
                    root.left = self.leftRotate(root.left)
                    return self.rightRotate(root)
                #case 4 right left case
                elif(BF<-1 and data<root.right.val):
                    root.right = self.rightRotate(root.right)
                    return self.leftRotate(root)

            return root
        self.root = insert(self.root,data)
        
        return self.count>oldCount
    
    def remove(self,data):
        oldCount = self.count
        self.root = self.delete(self.root,data)
        return self.count<oldCount

    def deleteNode(self,root):
        #found the node
        #if there is no children then removed
        if(root.left is None and root.right is None):
            print("Deleted data successfully")
            self.count-=1
            return None
        #current subroot has both children
        elif(root.right is not None and root.left is not None):
            temp = self.find_successor(root.right)
            root.val = temp.val
            root.right = self.delete(root.right,temp.val)
            return root

        # if the current subroot has only one child then subtite
        elif(root.right is not None ):
            print("Deleted data successfully")
            self.count-=1
            return root.right
        elif(root.left is not None):
            print("Deleted data successfully")
            self.count-=1
            return root.left
        return None
    
    def getPet(self, petData):
        def getNode(root,data):
            if(root is None):
                return None
            subtree = None
            if(data == root.val):
                return root.val
            elif(data <root.val):
                subtree = root.left
            else:
                subtree = root.right
            return getNode(subtree, data)
        return getNode(self.root,petData)

    def searchPet(self, data):
        def getNode(root,data):
                if(root is None):
                    return False
                subtree = None
                if(data == root.val):
                    return True
                elif(data <root.val):
                    subtree = root.left
                else:
                    subtree = root.right
                return getNode(subtree, data)
        return getNode(self.root,data)

    def isAvailTime(self, dateTime):
        def checkTime(root,dateTime):
            if(root is None):
                return True
            currStartDateTime = root.val.startDateTime
            currEndDateTime = root.val.endDateTime
            currDateTime = (currStartDateTime, currEndDateTime)
            if(currStartDateTime<=dateTime[0] and dateTime[0]<currEndDateTime ):
                return False
            elif(currStartDateTime<dateTime[1] and dateTime[1]<currEndDateTime):
                return False
            elif(currDateTime==dateTime):
                return False
            elif(currDateTime<dateTime):
                return checkTime(root.left,dateTime)
            else:
                return checkTime(root.right,dateTime)
        return checkTime(self.root,dateTime)

    def isEmpty(self):
        return self.root is None

    #tree traversal
    def displayTimeTable(self,root):
        if root is None:
            return 
        self.displayTimeTable(root.left)
        print("%s (%s to %s)"%(root.val,root.val.startDateTime, root.val.endDateTime))
        self.displayTimeTable(root.right)

    # O(log n)
    def findMinimumTime(self):
        temp = self.root 
        if(temp is None):
            return None
        while(temp.left is not None):
            temp = temp.left
        return temp.val


#


