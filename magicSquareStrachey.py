from magicSquareSiamese import MagicSquareSiamese
from magicChecker import magicChecker
from gridSquare import GridSquares
import wx
import sys
import math

class magicSquareStrachey:
    
    def __init__(self, order):
        if order%4 != 0 and order%2 == 0:
            self.k = order/4
        else:
            print 'Order of the square must be of type 4k+2'
            sys.exit(0) 
        self.k = order
        self.n = self.k/4

    def findMagicNumber(self):
        summ = (self.k/2.) * (math.pow(self.k,2) + 1)
        return summ    
    
    def createSquareStrachey(self):
        square = self.createABCD()
        for j in range(1, self.n + 1):
            square = self.changeSubColumn(square, j)
        for j in range(self.k - (self.n - 1) + 1, self.k + 1):
            square = self.changeSubColumn(square, j)
        square = self.changeSiglePosition(square, ((2*self.n+1)/2+1, 1), 
                                          ((2*self.n+1)/2+1 + 2*self.n+1,1))
        square = self.changeSiglePosition(square, ((2*self.n+1)/2+1, (2*self.n+1)/2+1), 
                                          ((2*self.n+1)/2+1 + 2*self.n+1, (2*self.n+1)/2+1))
        return square
    
    def changeSiglePosition(self, square, pos_1, pos_2):
        value_1 = square[pos_1]
        value_2 = square[pos_2]
        square[pos_1] = value_2
        square[pos_2] = value_1
        return square
          
    def changeSubColumn(self, square, n_col):
        k = int(math.sqrt(len(square.values())))
        n = k/4
        vector = {}
        for i in range(1, k+1):
            vector[i] = square[(i,n_col)]
        for i in range(1, 2*n+2):
            square[(i,n_col)] = vector[i + 2*n+1]
        for i in range(2*n+2, k+1):
            square[(i,n_col)] = vector[i - (2*n+1)]       
        return square
                 
    def createABCD(self):
        sq = {}
        A = MagicSquareSiamese(2*self.n + 1).buildSquare()          
        B = A.copy()
        B = self.createCapitalSquare(B)
        C = B.copy()
        C = self.createCapitalSquare(C)
        D = C.copy()
        D = self.createCapitalSquare(D)
        for j in range(1, 2*self.n + 2):
            for i in range(1, 2*self.n + 2):
                sq[(i,j)] = A[(i,j)]
        for j in range(2*self.n + 2, self.k + 1):
            for i in range(1, 2*self.n + 2):
                sq[(i,j)] = C[(i,j-(2*self.n+1))]
        for j in range(1, 2*self.n + 2):
            for i in range(2*self.n + 2, self.k + 1):
                sq[(i,j)] = D[(i-(2*self.n+1),j)]
        for j in range(2*self.n + 2, self.k + 1):
            for i in range(2*self.n + 2, self.k + 1):
                sq[(i,j)] = B[(i-(2*self.n+1),j-(2*self.n+1))]
        return sq
    
    def createCapitalSquare(self, square):
        for x in square.keys(): square[x] += pow(2*self.n + 1, 2)
        return square
    
    def printGridSquare(self, sq):
        app = wx.App(0)
        frame = wx.Frame(None, -1, 'Strachey Method')
        GridSquares(frame, sq, self.k)
        app.MainLoop()
        
    def printSquare(self, sq, n):
        for i in range(1, n+1):
            for j in range(1, n+1): 
                print sq[i,j],
            print '\n'

if __name__ == '__main__':
    order = 18
    sq = magicSquareStrachey(order)
    square = sq.createSquareStrachey()
    #sq.printSquare(square, order)
    print 'Magic Number of a %dx%d Square is %d' % (order, order, sq.findMagicNumber())
    if magicChecker(square, order).checkIfMagic(): 
        print 'Great, your square is Magic!!!'
    else:
        print 'Sorry Try Again!!'  
    sq.printGridSquare(square)    
        
    