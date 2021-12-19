# Sudoku is a solitaire game in which you try to fill a 9x9 grid with numbers from 1 through 9 such that each number appears exactly once in each row, in each column, and in each of the nine 3x3 subgrids. The following would be an example of a winning solution:

# 123 678 945
# 584 239 761
# 967 145 328

# 372 461 589
# 691 583 274
# 458 792 613

# 836 924 157
# 219 857 436
# 745 316 892

# Write a function called DoIWin() which takes the name of a text file as an argument, reads the state of a Sudoku board from that file, and returns True if that board represents a winning solution. (And returns False if it does not.) You may assume that the file contains exactly nine lines and that each line contains exactly nine characters between 1 and 9, inclusive, with no other characters between them (but remember that newline characters are a thing).
def DoIWin(path):
        
    fopen = open(path,'r')
        
    Sudoku = []
    for row in fopen:
        row = row.replace('\n','')
        temp = set(row)
        if(len(temp) != len(row)):
            return False
        Sudoku.append(row)
        
    for i in range(len(Sudoku[0])):
        tempL =[Sudoku[0][i],Sudoku[1][i],Sudoku[2][i],Sudoku[3][i],Sudoku[4][i],Sudoku[5][i],Sudoku[6][i],Sudoku[7][i],Sudoku[8][i]]
        temS = set(tempL)
        if(len(tempL) != len(temS)):
            return False
    
    for i in range(0,9,3):
        for j in range(0,9,3):
            tempL = [Sudoku[i][j],Sudoku[i][j+1],Sudoku[i][j+2],Sudoku[i+1][j],Sudoku[i+1][j+1],Sudoku[i+1][j+2],Sudoku[i+2][j],Sudoku[i+2][j+1],Sudoku[i+2][j+2]]
            tempS = set(tempL)
            if(len(tempL) != len(tempS)):
                return False
                
    fopen.close()
    return True