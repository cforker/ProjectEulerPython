'''
Created on Apr 26, 2013

@author: cforker
'''

class Protein(object):
    '''
    protein: string of length N that defines the protein, 0=P (polar), 1=H (hydrophobic)
    folding: array that describes one possible protein folding by describing the turn taken
        by the next element: {-1=left,1=right,0=straight}.  Length should be N-2, first move
        always assumed to be straight.
    '''
    
    protein = ''
    folding = []
    gridsize = [1,1]
    proteingrid = []

    def __init__(self,proteinstr):
        self.protein = proteinstr
        
    def setFolding(self,fold):
        self.folding = fold

    def findOptimalFolding(self):
        # 1. wave hands in the air
        # 2. magic
        # 3. protein is folded optimally
        return 0
    
    def updateLocation(self,location,direction,nextfold):
        location[0] += direction[0]
        location[1] += direction[1]
        newdirection = direction
        if (nextfold != 0):
            # rotate clockwise for nextfold=1,counterclockwise for nextfold=-1
            newdirection[0] = direction[1] * nextfold
            newdirection[1] = direction[0] * nextfold * -1
        return location,newdirection
        
    
    def foldingDimensions(self):
        # find the x and y length of a minimal rectangular grid that encloses the current folding
        # also check if the folding is valid 
        grid = []
        xlist = []
        ylist = []
        location = [0,0]
        direction = [1,0]
        grid.append(location)
        xlist.append(location[0])
        ylist.append(location[1])
        for fold in self.folding:
            location,direction = self.updateLocation(location, direction, fold)
            if location not in grid:
                grid.append(location)
                xlist.append(location[0])
                ylist.append(location[1])
            else:
                print "Illegal folding"
                self.gridsize = [0,0]
                return 0
        self.gridsize[0] = max(xlist) - min(xlist) + 1
        self.gridsize[1] = max(ylist) - min(ylist) + 1
        return 0     
    
    def buildGrid(self):
        self.grid = [None]*self.gridsize[1]
        for row in range(self.gridsize[1]):
            self.grid[row] = [-1]*self.gridsize[0]
        return
        