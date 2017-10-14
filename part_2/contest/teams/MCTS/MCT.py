class MCT:
    # monte carlo tree
    def __init__(self, parent, gameState, depth):
        self.visits = 0
        self.T = 0
        self.parent = parent
        self.child = []
        self.state = gameState.deepCopy()
        self.depth = depth
    
    def getGameState(self):
        return self.state
    
    def getChild(self):
        return self.child
    
    def getParent(self):
        return self.parent
    
    def getVisits(self):
        return self.visits
    
    def getTotalValue(self):
        return self.T
    
    def getDepth(self):
        return self.depth
    
    def visit(self):
        self.visits += 1
    
    def addChild(self, child):
        self.child = child

    def updateValue(self, value):
        self.T += value