import numpy as np
import math

def polar_to_rectangularb(r, theta_degrees):
    theta_radians = math.radians(theta_degrees)
    x = r * math.cos(theta_radians)
    y = r * math.sin(theta_radians)
    
    return (x, y)

def polar_to_rectangulara(r, theta_degrees):
    theta_radians = math.radians(theta_degrees)
    x = r * math.cos(theta_radians)
    y = r * math.sin(theta_radians)
    
    return (x, y)

reella_b = float(input("reella: "))
imag_b = float(input("imaginära: "))  
rectangular_coordinates = polar_to_rectangularb(reella_b, imag_b)

reella_a = reella_b - 0.01
rectangular_coordinates = polar_to_rectangulara(reella_a, imag_b)


print(f"Rektangulär form: x = {rectangular_coordinates[0]:.4f}, y = {rectangular_coordinates[1]:.4f}")


# Definiera rötterna i sex olika variabler för b
roots1b = [rectangular_coordinates[0] + rectangular_coordinates[1], rectangular_coordinates[0] - rectangular_coordinates[1]]
# Definiera rötterna i sex olika variabler för a
roots1a = [ ]

# Beräkna polynomkoefficienterna för varje par av rötter för b
coeff1b = np.poly(roots1b)

# Beräkna polynomkoefficienterna för varje par av rötter för a
coeff1a = np.poly(roots1a)
# Skriv ut koefficienterna för varje polynom för b
print("Polynomkoefficienterna för roots1b är:", coeff1b)
print("--------")
# Skriv ut koefficienterna för varje polynom för a
print("Polynomkoefficienterna för roots1a är:", coeff1a)


