import numpy as np

# Definiera rötterna i sex olika variabler för b
roots1b = [0.99539 + 0.030366j, 0.99539 - 0.030366j]
roots2b = [0.997276 + 0.07376j, 0.997276 - 0.07376j]
roots3b = [0.995757 + 0.092023j, 0.995757 - 0.092023j]
roots4b = [0.992966 + 0.118317j, 0.992966 - 0.118317j]
roots5b = [0.988255 + 0.152813j, 0.988255 - 0.152813j]
roots6b = [0.983916 + 0.17863j, 0.983916 - 0.17863j]

# Definiera rötterna i sex olika variabler för a
roots1a = [0.989544 + 0.03006j, 0.989544 - 0.03006j]
roots2a = [0.987303 + 0.073023j, 0.987303 - 0.073023j]
roots3a = [0.985894 + 0.09007j, 0.985894 - 0.09007j]
roots4a = [0.983946 + 0.117134j, 0.983946 - 0.117134j]
roots5a = [0.978373 + 0.151285j, 0.978373 - 0.151285j]
roots6a = [0.974077 + 0.176844j, 0.974077 - 0.176844j]

# Beräkna polynomkoefficienterna för varje par av rötter för b
coeff1b = np.poly(roots1b)
coeff2b = np.poly(roots2b)
coeff3b = np.poly(roots3b)
coeff4b = np.poly(roots4b)
coeff5b = np.poly(roots5b)
coeff6b = np.poly(roots6b)

# Beräkna polynomkoefficienterna för varje par av rötter för a
coeff1a = np.poly(roots1a)
coeff2a = np.poly(roots2a)
coeff3a = np.poly(roots3a)
coeff4a = np.poly(roots4a)
coeff5a = np.poly(roots5a)
coeff6a = np.poly(roots6a)

# Skriv ut koefficienterna för varje polynom för b
print("Polynomkoefficienterna för roots1b är:", coeff1b)
print("Polynomkoefficienterna för roots2b är:", coeff2b)
print("Polynomkoefficienterna för roots3b är:", coeff3b)
print("Polynomkoefficienterna för roots4b är:", coeff4b)
print("Polynomkoefficienterna för roots5b är:", coeff5b)
print("Polynomkoefficienterna för roots6b är:", coeff6b)
print("--------")
# Skriv ut koefficienterna för varje polynom för a
print("Polynomkoefficienterna för roots1a är:", coeff1a)
print("Polynomkoefficienterna för roots2a är:", coeff2a)
print("Polynomkoefficienterna för roots3a är:", coeff3a)
print("Polynomkoefficienterna för roots4a är:", coeff4a)
print("Polynomkoefficienterna för roots5a är:", coeff5a)
print("Polynomkoefficienterna för roots6a är:", coeff6a)
