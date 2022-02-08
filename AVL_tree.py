# since this is a node tree or subtree
# we can perform functions like get and update of the height and balance factor the tree
# a self-updating height of NodeTree
class NodeTree:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 0
        self.updateHeight()

    def updateHeight(self):
        self.height = max(self.getSubtreeHeight(self.left),self.getSubtreeHeight(self.right))+1

    def getBalanceFactor(self):
        return self.getSubtreeHeight(self.left)-self.getSubtreeHeight(self.right)

    def getSubtreeHeight(self,subtree):
        if(subtree is None):
            return 0
        return subtree.height
    

from VisualTree import *
class AVL_TREE:
    def __init__(self):
        self.root = None

    def add(self,data):
        def insert(root,data):
            if root is None:
                return NodeTree(data)

            if(data<root.val):
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

    def remove(self,data):
        self.root = self.delete(self.root,data)

    def delete(self,root,data):
            if root is None:
                print("DataToDel not found.")
                return
            if(data<root.val):
                root.left = self.delete(root.left,data)
            elif(data>root.val):
                root.right = self.delete(root.right,data)
            else:
                return self.deleteNode(root)

            root.updateHeight()
            BF = root.getBalanceFactor()
            if(abs(BF)>1):
                #need to perform rotations
                #based on different category
                if(data>root.val):
                    #R category
                    leftSubtree = root.left
                    leftBF = leftSubtree.getBalanceFactor()
                    if(leftBF==0):
                        #RO Category - Right Rotate
                        return self.rightRotate(root)
                    elif(leftBF==1):
                        #R1 Category - Right Rotate
                        return self.rightRotate(root)
                    elif(leftBF==-1):
                        #R-1 Category - Left Right Rotate
                        root.left = self.leftRotate(leftSubtree)
                        return self.rightRotate(root)
                elif(data<root.val):
                    #L category
                    rightSubtree = root.right
                    rightBF = rightSubtree.getBalanceFactor()
                    if(rightBF==0):
                        #L0 Category Left Rotate
                        return self.leftRotate(root)
                    elif(rightBF==1):
                        #L1 Category Right Left Rotate
                        root.right = self.rightRotate(rightSubtree)
                        return self.leftRotate(root)
                    elif(rightBF==-1):
                        #L-1 Category Left Rotate
                        return self.leftRotate(root)
            return root

    def deleteNode(self,root):
        #found the node
        #if there is no children then removed
        if(root.left is None and root.right is None):
            print("Deleted data successfully")
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
            return root.right
        elif(root.left is not None):
            print("Deleted data successfully")
            return root.left
        return None
    
    def find_successor(self,root):
        while(root.left is not None):
            root = root.left
        return root
        
            
    def preorder(self,root):
        if(root is None):
            return

        print(root.val,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def leftRotate(self,root):
        # rotate
        rightSubtree = root.right
        leftChildof_RightSubtree = rightSubtree.left
        rightSubtree.left = root
        root.right = leftChildof_RightSubtree

        #update height
        root.updateHeight()
        rightSubtree.updateHeight()
        #return new root
        return rightSubtree

    def rightRotate(self,root):
        #rotate
        leftSubtree = root.left
        rightChildof_leftSubtree = leftSubtree.right
        leftSubtree.right = root
        root.left = rightChildof_leftSubtree

        #update height
        root.updateHeight()
        leftSubtree.updateHeight()
        #return new root
        return leftSubtree

    def get(self,data):
        def getNode(root,data):
            if(root is None):
                return None
            subtree = None
            if(data == root.val):
                return root
            elif(data <root.val):
                subtree = root.left
            else:
                subtree = root.right
            return getNode(subtree, data)
        return getNode(self.root,data)

    def search(self,root,data):
        #if it is in the leaf node then there is no element in the tree
        if(root is None):
            return False
        
        subtree = None
        if(data == root.val):
            return True
        elif(data <root.val):
            subtree = root.left
        else:
            subtree = root.right
        return self.search(subtree,data)

    def display(self):
        print_tree(self.root)