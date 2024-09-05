# f = open("pussel.csv", "r")
# row = int(input("Skriv in vilken rad du vill läsa: ")) - 1  
# lines = f.readlines()

# if 0 <= row < len(lines):  
#     print(lines[row])
# else:
#     print("Ogiltig radnummer.")
# f.close()  

file = open('pussel.csv',mode='r', encoding='UTF-8')
row = int(input("What row do you want?"))
row_number = file.readlines()
print(row_number[row])


