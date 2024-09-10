try:
  numerator = int(input("ange täljare "))
  denominator = int(input("ange nämnare "))
  print(f'kvoten blir: {numerator/denominator}')
except ZeroDivisionError :
  print("Dela inte med 0 din apa")
except ValueError:
  print("Använd inte bokstäver")
except:
  print("du gjorde fortfarande fel HUR?")

print("hej då")
