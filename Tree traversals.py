class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)

def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)
def preorder(root):
    if root!=None:
        print(root.val,end=" ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root!=None:
        postorder(root.left)
        postorder(root.right)
        print(root.val,end=" ")
def size(root):
   if root!=None:
        return 1+size(root.left)+size(root.right)
   else:
       return 0

def height(root):
   if root!=None:
       return max(height(root.left),height(root.right))+1
   else:
       return 0



inorder(root)
print()
preorder(root)
print()
postorder(root)
print()
print(size(root))
print(height(root))
