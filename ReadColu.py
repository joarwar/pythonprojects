f = open("pussel.csv", "r")
lines = f.readlines()
try:
    col = int(input("What column would you like to see? ")) -1
    for line in lines:
        first_element = line.strip().split(",")[col] 
        print(first_element)  
except ValueError:
    print("No letters")
except IndexError: 
    print("Only numbers between 1-9")
except:
    print("Something went wrong")

f.close()
