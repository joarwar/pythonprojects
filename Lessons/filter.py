import numpy as np
import matplotlib.pyplot as plt

# Definiera filterkoefficienterna för ett 3-taps moving average-filter
h = np.array([1/4, 1/2, 1/4])

# Skapa en frekvensvektor från 0 till pi
omega = np.linspace(0, np.pi, 500)

# Beräkna frekvensresponsen H(omega) genom att ta Fouriertransformen
H = np.exp(-1j * omega[:, None] * np.arange(3)) @ h

# Beräkna magnituden av frekvensresponsen |H(omega)|
magnitude = np.abs(H)

# Plotta frekvensresponsens magnitud
plt.plot(omega, magnitude)
plt.title('Magnitud av frekvensresponsen för ett 3-taps moving average-filter')
plt.xlabel(r'$\omega$ (rad/sample)')
plt.ylabel(r'$|H(\omega)|$')
plt.grid(True)
plt.show()