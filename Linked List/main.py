class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class SSl:
    def __init__(self,start=None):
        self.start=start
    def isEmpty(self):
        return self.start is None
        
