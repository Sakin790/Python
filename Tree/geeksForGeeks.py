class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        
    def insert(self,root,data):
        if root is None:
            return Node(data)
        if root.val==data:
            return root
        if root.val<data:
            root.right=self.insert(root.right,data)
        if root.val>data:
            root.left=self.insert(root.left,data)
        return root
    
b1=Node(10)
print(b1.insert())