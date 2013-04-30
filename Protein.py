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
    HBonds = 0

    def __init__(self,proteinstr):
        self.protein = proteinstr
        
    def setFolding(self,fold):
        self.folding = fold
        self.folding.append(0)
        return
        
    def printEverything(self):
        print "Protein",self.protein
        print "Folding",self.folding
        print "Grid size and offset",self.gridsize,self.gridoffset,"\n"
        for line in self.proteingrid:
            for element in line:
                print element,
            print ""
        #for loc in self.location:
        #    print loc
        print "\nH Bonds:",self.HBonds
        return

    def findOptimalFolding(self):
        # 1. wave hands in the air
        # 2. magic
        # 3. protein is folded optimally
        return 0
    
    def updateLocation(self,location,direction,nextfold):
        # helper function for foldingDimensions
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
        xmin,xmax,ymin,ymax = 0,0,0,0
        location = [0,0]
        direction = [0,1]
        grid.append(location[:])
        for fold in self.folding:
            location,direction = self.updateLocation(location, direction, fold)
            #print "New location is",location,"new direction",direction,fold
            if location not in grid:
                grid.append(location[:])
                xmin = min([xmin,location[0]])
                xmax = max([xmax,location[0]])
                ymin = min([ymin,location[1]])
                ymax = max([ymax,location[1]])
            else:
                print "Illegal folding",location,grid
                self.gridsize = [0,0]
                return 0
        self.gridsize[0] = xmax - xmin + 1
        self.gridsize[1] = ymax - ymin + 1
        self.gridoffset[0] = -1 * xmin
        self.gridoffset[1] = -1 * ymin
        self.location = grid[:]
        return 0     
    
    def buildGrid(self):
        # uses self.gridsize, self.gridoffset, self.location (maps each element to a grid location) and 
        # self.protrein to populate a grid with the protein chain elements
        self.proteingrid = [None]*self.gridsize[1]
        for row in range(self.gridsize[1]):
            self.proteingrid[row] = ['X']*self.gridsize[0]
        for i in range(len(self.location)):
            self.proteingrid[self.location[i][1]+self.gridoffset[1]][self.location[i][0]+self.gridoffset[0]] = self.protein[i]
        return
    
    def countHBonds(self):
        # calculate the number of H bonds in self.proteingrid
        hcount = 0
        # check horizontal edges
        for i in range(self.gridsize[1]):
            for j in range(self.gridsize[0]-1):
                if (self.proteingrid[i][j]=='1' and self.proteingrid[i][j+1]=='1'):
                    hcount += 1
        # check vertical edges
        for i in range(self.gridsize[1]-1):
            for j in range(self.gridsize[0]):
                if (self.proteingrid[i][j]=='1' and self.proteingrid[i+1][j]=='1'):
                    hcount += 1
        print "Current folding has",hcount,"H bonds"
        self.HBonds = hcount
        return hcount
        
        