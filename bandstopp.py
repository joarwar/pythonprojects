import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# Definiera filterkoefficienterna
b = [1.   ,      0.618034  , 1.00000092]  # Numerator koefficienter (b)
a = []          # Nominator koefficienter (a)

# Definiera samplingsfrekvensen
fs = 48000  # Samplingsfrekvens i Hz

# Beräkna frekvensresponsen
w, h = freqz(b, a)

# Normera frekvensen till [0, 0.5], där 0.5 motsvarar halva samplingsfrekvensen
f_norm = w / np.pi * 0.5  # Normaliserad frekvens (0 till 0.5)

# Plot av frekvensresponsen (magnitud)
plt.figure()
plt.plot(f_norm, np.abs(h))  # Normerad frekvens (0 till 0.5)
plt.title('Normerad frekvensrespons (magnitud)')
plt.xlabel('Normaliserad frekvens (× Nyquist)')
plt.ylabel('Magnitud')
plt.grid()
plt.xlim(0, 0.5)  # Visa bara upp till 0.5 (Nyquist-frekvensen)
plt.show()