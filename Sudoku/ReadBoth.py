a = input("Row or Column? ")
f = open("Sudoku/pussel.csv", "r")

if a.lower() == "row":
  row = int(input("Skriv in vilken rad du vill läsa: ")) - 1
  lines = f.readlines()
  try:
    if 0 <= row < len(lines):  
      print(lines[row])
    else:
      print("Ogiltig nummer.")
    f.close()
  except ValueError:
    print("Inga bokstäver")
  except IndexError: 
    print("Bara siffror mellan 1-9")
  except:
    print("Okänt fel")
        
elif a.lower() == "column":
  lines = f.readlines()
  try:
      col = int(input("Vilken kolumn vill du se? ")) -1
      for line in lines:
          first_element = line.strip().split(",")[col] 
          print(first_element)  
  except ValueError:
    print("Inga bokstäver")
  except IndexError: 
    print("Bara siffror mellan 1-9")
  except:
    print("Okänt fel")

  f.close()
else:
  raise Exception("Skriv antingen rad eller kolumn.")
f.close()