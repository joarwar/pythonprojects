f = open("Sudoku/pussel.csv", "r")
lines = f.readlines()
unsolved_sudoku = []

for line in lines:
  row = [int(num) for num in line.strip().split(',')]
  unsolved_sudoku.append(row)

def check_row(unsolved_sudoku, row, number):
    for i in range(9):
        if unsolved_sudoku[row][i] == number:
            return False
    return True

def check_col(unsolved_sudoku, col, number):
    for i in range(9):
        if unsolved_sudoku[i][col] == number:
            return False
    return True

def check_box(unsolved_sudoku, row, col, number):
    #Box (0,0) | Box (0,3) | Box (0,6)
    #--------------------------------
    #Box (3,0) | Box (3,3) | Box (3,6)
    #--------------------------------
    #Box (6,0) | Box (6,3) | Box (6,6)

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if unsolved_sudoku[i + start_row][j + start_col] == number:
                return False
    return True 

def check_numbers(unsolved_sudoku, row, col, number):
    return check_row(unsolved_sudoku, row, number) and check_col(unsolved_sudoku, col, number) and check_box(unsolved_sudoku, row, col, number)

# Fixat checkar måste lägga en check om det finns mer än ett alternativ i en ruta. Om det inte finns det så ska den sätta in det alternativet.
# Om det finns fler än ett alternativ så ska den skriva ut vilka alternativ som finns.

for x in range(9):  
    for y in range(9):  
        if unsolved_sudoku[x][y] == 0:  
            for num in range(1, 10):
                if check_numbers(unsolved_sudoku, x, y, num):
                    print("Row: ", x, "Col: ", y, "Number: ", num)
                else:
                    print("Row: ", x, "Col: ", y, "Number: ", num, "Not possible")

for row in unsolved_sudoku:
    print(row)



f.close()