from magicChecker import magicChecker
from magicChecker import magicCheckerMulti
from gridSquare import GridSquares
import wx
import sys 
import math

class MagicSquareLUX:
    
    def __init__(self, order):
        if order%4 != 0 and order%2 == 0:
            self.k = order/4
        else:
            print 'Order of the square must be of type 4k+2'
            sys.exit(0) 
        self.n = order
        self.lux_square = {}
        self.lux_matrix = {}
        self.mag_num = int(self.findMagicNumber())
        
    def findMagicNumber(self):
        summ = (self.n/2.) * (math.pow(self.n,2) + 1)
        return summ
    
    def createLUXMatrix(self):
        LUX_len = 2*self.k + 1
        L_row = self.k + 1
        U_row = L_row + 1
        for j in range(1, LUX_len + 1):
            for i in range(1, L_row + 1):
                self.lux_matrix[(i,j)] = 'L'
        for j in range(1, LUX_len + 1):
            self.lux_matrix[(L_row + 1, j)] = 'U'
        for j in range(1, LUX_len+1):
            for i in range(L_row + 2, LUX_len + 1):
                self.lux_matrix[(i,j)] = 'X'
        self.lux_matrix[(L_row, LUX_len/2 + 1)] = 'U'
        self.lux_matrix[(U_row, LUX_len/2 + 1)] = 'L'
    
    def createLUXSquare(self):
        LUX_len = 2*self.k + 1
        counter = 1
        k = 1
        pos_LUX = (1, LUX_len/2 + 1)
        pos_square = self.pos_square(pos_LUX)
        self.blockLUXSquare(pos_square, self.typeOfBlock(pos_LUX), k)       
        while counter < LUX_len*LUX_len:
            counter += 1
            k += 4
            pos_LUX_new = self.moveDiag(pos_LUX)
            pos_square = self.pos_square(pos_LUX_new)
            if self.checkIsFree(pos_square, self.lux_square):
                self.blockLUXSquare(pos_square, self.typeOfBlock(pos_LUX_new), k)
                pos_LUX = pos_LUX_new
            else:
                pos_LUX_new = self.move(pos_LUX, SOUTH)
                pos_square = self.pos_square(pos_LUX_new)
                self.blockLUXSquare(pos_square, self.typeOfBlock(pos_LUX_new), k)
                pos_LUX = pos_LUX_new
        return self.lux_square         
            
    def pos_square(self, pos_LUX):
        return (pos_LUX[0] + pos_LUX[0] - 1, pos_LUX[1] + pos_LUX[1] - 1)
    
    def typeOfBlock(self, lux_matrix_pos):
        if self.lux_matrix[lux_matrix_pos] == 'L': return BLOCK_L
        if self.lux_matrix[lux_matrix_pos] == 'U': return BLOCK_U
        if self.lux_matrix[lux_matrix_pos] == 'X': return BLOCK_X
    
    def blockLUXSquare(self, start_pos, block, k):
        self.lux_square[self.move(self.move(start_pos, block[0][0]), block[0][1])] = k
        self.lux_square[self.move(self.move(start_pos, block[1][0]), block[1][1])] = k + 1
        self.lux_square[self.move(self.move(start_pos, block[2][0]), block[2][1])] = k + 2
        self.lux_square[self.move(self.move(start_pos, block[3][0]), block[3][1])] = k + 3
    
    def moveDiag(self, start_pos):
        LUX_len = 2*self.k + 1
        if start_pos == (1, LUX_len):
            return (2, LUX_len)
        pos_new = self.move(start_pos, EAST)
        if pos_new[1] == LUX_len+1:
            pos_new = (pos_new[0], 1)
        pos_new = self.move(pos_new, NORTH)
        if pos_new[0] == 0:
            pos_new = (LUX_len, pos_new[1])
        return pos_new
        
    def move(self, start_pos, direction):
        return (start_pos[0]+direction[0], start_pos[1]+direction[1])
    
    def checkIsFree(self, pos, square):
        return pos not in square.keys()
    
    def printGridSquare(self, sq):
        app = wx.App(0)
        frame = wx.Frame(None, -1, 'LUX Conway Method')
        GridSquares(frame, sq, self.n)
        app.MainLoop()
                            
    def printSquare(self, sq, n):
        for i in range(1, n+1):
            for j in range(1, n+1): 
                print sq[i,j],
            print '\n'

NORTH = (-1,0)
SOUTH = (1,0)
WEST  = (0,-1)
EAST  = (0,1)
STOP  = (0,0)

BLOCK_L = [(EAST,STOP), (SOUTH,STOP), (SOUTH,EAST), (STOP,STOP)]
BLOCK_U = [(STOP,STOP), (SOUTH,STOP), (SOUTH,EAST), (EAST,STOP)]
BLOCK_X = [(STOP,STOP), (SOUTH,EAST), (SOUTH,STOP), (EAST,STOP)]


if __name__ == '__main__':
    n = 14
    sq = MagicSquareLUX(n)
    sq.createLUXMatrix()
    sq.printSquare(sq.lux_matrix, n/2)
    square = sq.createLUXSquare()
    print 'Magic Number of a %dx%d Square is %d' % (n, n, sq.findMagicNumber())
    if magicChecker(sq.lux_square, n).checkIfMagic(): 
        print 'Great, your square is Magic!!!'
    print magicCheckerMulti(sq.lux_square, n, 3).checkIfMagic()
    sq.printGridSquare(square)
    
    