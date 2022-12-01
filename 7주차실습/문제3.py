# 2019112018 원규진
print('2019112018 원규진')
print('문제3 레드블랙트리 구현\n')

class Node:
    def __init__(self, key):
        self.key = key
        
        self.left = None
        self.right = None
        self.parent = None
        
        self.color = 'Red'
        
class RedBlackTree:
    def __init__(self):
        self.root = None
        self.nil = None
        
    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        
    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
        
    def insertFixup(self, n):
        while n.parent.color == 'Red':
            if n.parent == n.parent.parent.left:
                y = n.parent.parent.right
                if y.color == 'Red':
                    n.parent.color = 'Black'
                    y.color = 'Black'
                    n.parent.parent.color = 'Red'
                    n = n.parent.parent
                elif n == n.parent.right:
                    n = n.parent
                    self.leftRotate(self, n)
                n.parent.color = 'Black'
                n.parent.parent.color = 'Red'
                self.rightRotate(self,n.parent.parent)
        self.root.color = 'Black'
        
    def insert(self, n):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if n.key < x.key:
                x = x.left
            else:
                x = x.right
        n.parent = y
        if y == self.nil:
            self.root = n
        elif n.key < y.key:
            y.left = n
        else:
            y.right = n
        n.left = self.nil
        n.right = self.nil
        n.color = 'Red'
        self.insertFixup(self, n)
        
def printTree(n):
    if n.left != None:
        printTree(n.left)
    if n.parent != None:
        print("key: %d, parent: %d, color: %s" %(n.key, n.parent.key, n.color))
    else:
        print("key: %d, root: %d, color: %s" %(n.key, n.parent, n.color))
    if n.right != None:
        printTree(n.right)
        
tree = RedBlackTree()
n = [20, 15, 14, 12, 13, 1]

for i in n:
    RedBlackTree.insert(tree, i)
    printTree(tree.root)
    print()
    
printTree(tree.root)