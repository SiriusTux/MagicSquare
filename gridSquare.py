import wx.grid

class GridSquares(wx.Frame):

    def __init__(self, parent, square, size):
        self.size = size
        grid = wx.grid.Grid(parent, -1)
        grid.CreateGrid(self.size + 2, self.size + 2)
        
<<<<<<< HEAD
=======
        '''# Set Sizer
        Sizer = wx.BoxSizer(wx.HORIZONTAL)
        Sizer.Add(grid, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        parent.SetSizerAndFit(Sizer)'''

        
>>>>>>> 78bdfeb0675f453f2d39e491d34547a0c3339088
        # Set Labels not visible
        grid.SetRowLabelSize(0)
        grid.SetColLabelSize(0)
        
        # Set Row and Column size
        grid.SetDefaultRowSize(40)
        grid.SetDefaultColSize(40)

        # Print Square Values as string
        for j in range(2, self.size + 2):
            for i in range(2, self.size + 2):
                grid.SetCellAlignment(i-1, j-1, wx.ALIGN_CENTER, wx.ALIGN_CENTER)
                grid.SetCellValue(i-1, j-1, str(square[(i-1,j-1)]))
                grid.SetReadOnly(i-1, j-1)
        
        # Evaluate Rows Sum
        for i in range(1, self.size + 1):
            mg_num = self.evaluateRowSum(square, i)
            grid.SetCellAlignment(i, self.size+1, wx.ALIGN_CENTER, wx.ALIGN_CENTER)
            grid.SetCellBackgroundColour(i, self.size+1, wx.YELLOW)
            grid.SetCellValue(i, self.size+1, str(mg_num))
            grid.SetCellAlignment(i, 0, wx.ALIGN_CENTER, wx.ALIGN_CENTER)
            grid.SetCellBackgroundColour(i, 0, wx.YELLOW)
            grid.SetCellValue(i, 0, str(mg_num))
            grid.SetReadOnly(i, 0)
            
        # Evaluate Columns Sum  
        for j in range(1, self.size + 1):
            mg_num = self.evaluateColSum(square, j)
            grid.SetCellAlignment(self.size+1, j, wx.ALIGN_CENTER, wx.ALIGN_CENTER)
            grid.SetCellBackgroundColour(self.size+1, j, wx.GREEN)
            grid.SetCellValue(self.size+1, j, str(mg_num))
            grid.SetCellAlignment(0, j, wx.ALIGN_CENTER, wx.ALIGN_CENTER) 
            grid.SetCellBackgroundColour(0, j, wx.GREEN)
            grid.SetCellValue(0, j, str(mg_num)) 
            grid.SetReadOnly(0, j)
        
        #Evaluate Diagonal 1
        diag1 = self.evaluateDiag1(square)
        grid.SetCellAlignment(self.size+1, self.size+1, wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        grid.SetCellBackgroundColour(self.size+1, self.size+1, wx.BLUE)
        grid.SetCellTextColour(self.size+1, self.size+1, wx.WHITE)
        grid.SetCellValue(self.size+1, self.size+1, str(diag1))
        grid.SetReadOnly(self.size+1, self.size+1)
        grid.SetCellAlignment(0, 0, wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        grid.SetCellBackgroundColour(0, 0, wx.BLUE)
        grid.SetCellTextColour(0, 0, wx.WHITE)
        grid.SetCellValue(0, 0, str(diag1))
        grid.SetReadOnly(0, 0)
        
        #Evaluate Diagonal 2
        diag2 = self.evaluateDiag2(square)
        grid.SetCellAlignment(0, self.size+1, wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        grid.SetCellBackgroundColour(0, self.size+1, wx.RED)
        grid.SetCellTextColour(0, self.size+1, wx.WHITE)
        grid.SetCellValue(0, self.size+1, str(diag2))
        grid.SetReadOnly(0, self.size+1)
        grid.SetCellAlignment(self.size+1, 0, wx.ALIGN_CENTER, wx.ALIGN_CENTER) 
        grid.SetCellBackgroundColour(self.size+1, 0, wx.RED)
        grid.SetCellTextColour(self.size+1, 0, wx.WHITE)
        grid.SetCellValue(self.size+1, 0, str(diag2))   
        grid.SetReadOnly(self.size+1, 0)     

        parent.Show()
        
    def evaluateRowSum(self, square, row):
        summ = 0
        for j in range(1, self.size + 1):
            summ += square[(row, j)]
        return summ
    
    def evaluateColSum(self, square, col):
        summ = 0
        for i in range(1, self.size + 1):
            summ += square[(i, col)]
        return summ
    
    def evaluateDiag1(self, square):
        diag1 = 0
        for i in range(1, self.size + 1):
            diag1 += square[(i,i)]
        return diag1

    def evaluateDiag2(self, square):
        diag2 = 0
        for i in range(1, self.size + 1):
            diag2 += square[(i,self.size+1-i)]
        return diag2   
            

if __name__ == '__main__':
    app = wx.App(0)
    sq = {(1,1):1,(1,2):2,(2,1):2,(2,2):3}
    frame = wx.Frame(None, -1, 'Test gridSquare output')
    GridSquares(frame, sq, 2)
    app.MainLoop()