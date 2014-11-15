from magicChecker import magicChecker
import math
import random

class MagicSquareRandom:
    
    def __init__(self, order):
        self.n = order
        self.mag_num = int(self.findMagicNumber())
        
    def findMagicNumber(self):
        summ = (self.n/2.) * (math.pow(self.n,2) + 1)
        return summ
    
    def randomSquare(self):
        keys = []     
        for i in range(1, self.n + 1):
            for j in range(1, self.n + 1):
                keys.append((i,j))
        values = random.sample(xrange(1, self.n*self.n + 1), self.n*self.n)
        square= dict(zip(keys, values))
        return square
        
    def printSquare(self, sq):
        for i in range(1, n+1):
            for j in range(1, n+1): 
                print '%d ' % sq[i,j],
            print '\n'
        
    
if __name__ == '__main__':
    n = 3
    sq = MagicSquareRandom(n) 
    sq_random = sq.randomSquare()
    ck = magicChecker(sq_random, n)
    k = 1
    while ck.checkIfMagic() == False:        
        sq_random = sq.randomSquare()
        ck = magicChecker(sq_random, n)
        print 'Tentativo numero', k
        k += 1
    print 'Magic Number of a %dx%d Square is %d' % (n, n, sq.findMagicNumber())
    sq.printSquare(sq_random)

        
