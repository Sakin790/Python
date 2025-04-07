
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
         
         
class Solution(object):
    def insertIntoBST(self, root, val):
        return self.rinsert(root, val)
    
    def rinsert(self, root, val):
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.rinsert(root.left, val)
        elif val > root.val:
            root.right = self.rinsert(root.right, val)
        return root
    
    def search(root,target):
        current =root
        while current:
            if target==current.val:
                return True
            elif target< current.val:
                current=current.left
            else:
               current=current.right
        return False
    
    def inorder(self): # left root right
        result=[]
        self.rinoder(self.root,result)
        return result
    
        
            
        
        