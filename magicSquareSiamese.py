# -*- coding: utf-8 -*-
from magicChecker import magicChecker
from magicChecker import magicCheckerMulti
from gridSquare import GridSquares
import wx
import math
import sys

class MagicSquareSiamese:
    
    def __init__(self, order):
        if order%2 == 0:
            print 'Order of the square must be odd!!!'
            sys.exit(0) 
        self.n = order
        self.mag_num = int(self.findMagicNumber())
        
    def findMagicNumber(self):
        summ = (self.n/2.) * (math.pow(self.n,2) + 1)
        return summ
        
    def buildSquare(self):
        square = {}
        k = 1
        pos = (1, self.n/2 + 1)
        square[pos] = k
        while k < self.n*self.n:
            k += 1
            pos_new = self.moveDiag(pos)
            if self.checkIsFree(pos_new, square):
                square[pos_new] = k
                pos = pos_new
            else:
                pos_new = self.move(pos, SOUTH)
                square[pos_new] = k
                pos = pos_new
        return square
        
    def moveDiag(self, start_pos):
        if start_pos == (1, self.n):
            return (2, self.n)
        pos_new = self.move(start_pos, EAST)
        if pos_new[1] == self.n+1:
            pos_new = (pos_new[0], 1)
        pos_new = self.move(pos_new, NORTH)
        if pos_new[0] == 0:
            pos_new = (self.n, pos_new[1])
        return pos_new
        
    def move(self, start_pos, direction):
        return (start_pos[0]+direction[0], start_pos[1]+direction[1])
    
    def checkIsFree(self, pos, square):
        return pos not in square.keys()
    
    def printSquare(self, sq):
        for i in range(1, n+1):
            for j in range(1, n+1): 
                print '%d ' % sq[i,j],
            print '\n'
    
    def printGridSquare(self, sq):
        app = wx.App(0)
        frame = wx.Frame(None, -1, 'Siamese Method')
        GridSquares(frame, sq, self.n)
        app.MainLoop()

NORTH = (-1,0)
SOUTH = (1,0)
WEST  = (0,-1)
EAST  = (0,1)


if __name__ == '__main__':
    n = 5
    sq = MagicSquareSiamese(n)
    square = sq.buildSquare()
    print 'Magic Number of a %dx%d Square is %d' % (n, n, sq.findMagicNumber())
    if magicChecker(square, n).checkIfMagic(): 
        print 'Great, your square is Magic!!!'
    print magicCheckerMulti(square, n, 2).checkIfMagic()
    sq.printGridSquare(square)

    