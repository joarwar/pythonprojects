f = open("Sudoku/pussel.csv", "r")
row = int(input("Skriv in vilken rad du vill läsa: ")) - 1  
lines = f.readlines()

if 0 <= row < len(lines):  
     print(lines[row])
else:
    print("Ogiltig nummer.")
f.close()  




    