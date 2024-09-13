import numpy as np

# Definiera rötterna (kan vara komplexa)
roots = [-0.309017 + 0.951057j, -0.309017 - 0.951057j]  # Exempel på rötter, varav två är komplexa

# Beräkna polynomkoefficienterna
coeff = np.poly(roots)

# Skriv ut koefficienterna
print("Polynomkoefficienterna är:", coeff)