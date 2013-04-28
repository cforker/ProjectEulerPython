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
    gridoffset = [0,0]
    proteingrid = []
    location = []

    def __init__(self,proteinstr):
        self.protein = proteinstr
        
    def setFolding(self,fold):
        self.folding = fold
        
    def printEverything(self):
        print "Protein",self.protein
        print "Folding",self.folding
        print "Grid size and offset",self.gridsize,self.gridoffset
        for line in self.proteingrid:
            print line
        for loc in self.location:
            print loc
        return

    def findOptimalFolding(self):
        # 1. wave hands in the air
        # 2. magic
        # 3. protein is folded optimally
        return 0
    
    def updateLocation(self,location,direction,nextfold):
        location[0] += direction[0]
        location[1] += direction[1]
        newdirection = direction[:]
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
        direction = [0,1]
        grid.append(location[:])
        xlist.append(location[0])
        ylist.append(location[1])
        for fold in self.folding:
            location,direction = self.updateLocation(location, direction, fold)
            #print "New location is",location,"new direction",direction,fold
            if location not in grid:
                grid.append(location[:])
                xlist.append(location[0])
                ylist.append(location[1])
            else:
                print "Illegal folding",location,grid
                self.gridsize = [0,0]
                return 0
        location,direction = self.updateLocation(location, direction, 0)
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
        self.gridoffset[0] = -1 * min(xlist)
        self.gridoffset[1] = -1 * min(ylist)
        self.location = grid[:]
        return 0     
    
    def buildGrid(self):
        self.proteingrid = [None]*self.gridsize[1]
        for row in range(self.gridsize[1]):
            self.proteingrid[row] = [-1]*self.gridsize[0]
        for i in range(len(self.location)):
            self.proteingrid[self.location[i][1]+self.gridoffset[1]][self.location[i][0]+self.gridoffset[0]] = int(self.protein[i])
        return
        