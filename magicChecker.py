import math

class magicChecker:
    
    def __init__(self, square, order):
        self.square = square
        self.n = order
        self.mag_num = int(self.findMagicNumber())
        self.square_multi = {}
        
    def findMagicNumber(self):
        summ = (self.n/2.) * (math.pow(self.n,2) + 1)
        return summ
    
    def checkIfMultiMagic(self, power):
        ''' Construct New Square '''
        for x in self.square.keys():
            self.square_multi[x] = int(math.pow(self.square[x], power))
        
        
    def checkIfMagic(self):
        for i in range(1, self.n + 1):
            if self.checkRow(i):
                pass
            else:
                return False
        for j in range(1, self.n + 1):
            if self.checkCol(j):
                pass
            else:
                return False
        if self.checkDiag():
            pass
        else:
            return False
        return True
            
    def checkCol(self, k):
        sum_col = 0
        for i in range(1, self.n + 1):
            sum_col += self.square[i,k]
        if sum_col == self.mag_num:
            return True
        else:
            return False
    
    def checkRow(self, k):
        sum_row = 0
        for j in range(1, self.n + 1):
            sum_row += self.square[k,j]
        if sum_row == self.mag_num:
            return True
        else:
            return False
        
    def checkDiag(self):
        sum_diag_1 = 0
        sum_diag_2 = 0
        for k in range(1, self.n + 1):
            sum_diag_1 += self.square[k,k]
        for k in range(1, self.n + 1):
            sum_diag_2 += self.square[k, self.n+1-k]
        if sum_diag_1 == self.mag_num and sum_diag_2 == self.mag_num:
            return True               
        else:
            return False
        
class magicCheckerMulti(magicChecker):
    
    def __init__(self, square, order, power):
        self.n = order
        self.mag_num = int(self.findMagicNumber())        
        self.square = {}  
        for x in square.keys():
            self.square[x] = int(math.pow(square[x], power))
        
    