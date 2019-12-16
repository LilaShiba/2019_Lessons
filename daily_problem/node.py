class Node():
    
    def __init__(self,data):
        self.r = None
        self.l = None
        self.v = data
        self.explored = False
        self.parent = None