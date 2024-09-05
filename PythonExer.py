import os

#referenser och kopior
#Skapa en lista som heter my_numbers och innehåller 8 st 1:or (int:ar)
my_numbers = [1,1,1,1,1,1,1,1]
#Skapa ytterligare en lista som heter new_numbers och tilldela den elementen 2 och 3 från listan my_numbers. Kontrollera att innehållet i new_numbers på lämpligt vis.
new_numbers =[my_numbers[2],my_numbers[3]]
print(new_numbers)
#Ändra det första elementet i listan new_numbers till en 5:a. Kontrollera att innehållet i new_numbers på lämpligt vis, kontrollera även innehållet i my_numbers. Är innehållet i my_numbers oförändrat?
new_numbers[0] = 5
print(new_numbers[0])

#Tilldela nu istället new_numbers hela my_numbers (inte bara element 2 och 3 som i tidigare uppgift).
new_numbers[1] = 5
print(new_numbers)

#Skapa en ny sträng my_name som tilldelas en sträng med ditt fullständiga namn (för och efternamn åtskilda med underscore)
full_name = "Joar_Warholm"
#Skriv ut underscore:t genom att indexera my_name korrekt!
print(full_name[4])
#Skriv ut förnamnet genom att indexera my_name med ett intervall!
print(full_name[0:4])
#Skriv ut efternamnet genom att indexera my_name med ett intervall!
print(full_name[5:12])
#Skriv ut varannan bokstav i ditt fulla namn!
even_list = []
odd_list = []
for i in range(len(full_name)):
    if i % 2 == 0:
        even_list.append(full_name[i])
    else:
        odd_list.append(full_name[i])
print(even_list)
print(odd_list)
#Skriv ut ditt fulla namn baklänges!
print(full_name[::-1])
print(full_name[::2])

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())