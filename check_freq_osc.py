# -------------------------------------------------------------
# Importera bibliotek
# -------------------------------------------------------------
import pyvisa
import time
import numpy as np
import matplotlib.pyplot as plt


# -------------------------------------------------------------
# Block 1: Initialisera
# -------------------------------------------------------------

def initialisera():
    # Initialiserar anslutningen till oscilloskopet och returnerar instrumentobjektet
    rm = pyvisa.ResourceManager()

    # Hämta alla tillgängliga resurser för att identifiera oscilloskopet anslutet via USB
    resurser = rm.list_resources()
    print("Tillgängliga resurser:", resurser)

    # Kontrollera att resurser finns
    if not resurser:
        raise ValueError("Inga resurser hittades. Kontrollera anslutningen.")

    instrument_adress = resurser[0]
    oscilloskop = rm.open_resource(instrument_adress)

    # Kontrollera att vi är anslutna till rätt instrument genom att fråga om ID
    idn = oscilloskop.query('*IDN?')
    print(f"Ansluten till: {idn}")

    oscilloskop.timeout = 5000
    oscilloskop.write_termination = '\n'
    oscilloskop.read_termination = '\n'

    return oscilloskop


# -------------------------------------------------------------
# Block 2: Mätning
# -------------------------------------------------------------

def mata(oscilloskop, kanal="CHANnel1"):
    try:
        oscilloskop.write(f':MEASure:FREQuency {kanal}')
        frekvens = oscilloskop.query(f':MEASure:FREQuency? {kanal}')
        print(f"Frekvens på {kanal}: {frekvens} Hz")
    except Exception as e:
        print(f"Misslyckades med att mäta frekvens på {kanal}: {e}")
        return None

    return float(frekvens)


# -------------------------------------------------------------
# Block 4: Rita sinusvåg
# -------------------------------------------------------------

def plot_sinus_wave(frequency, duration=0.1, sample_rate=1000):
    # Skapa tidsvektor
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # Generera sinusvåg baserad på den uppmätta frekvensen
    amplitude = 10.0
    y = amplitude * np.sin(2 * np.pi * frequency * t)

    # Rita signalen
    plt.figure(figsize=(10, 4))
    plt.plot(t, y, label=f'Sinusvåg med {frequency:.2f} Hz')
    plt.title(f'Sinusvåg med frekvens {frequency:.2f} Hz')
    plt.xlabel('Tid [s]')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.legend()
    plt.show()


# -------------------------------------------------------------
# Huvudprogram
# -------------------------------------------------------------

def main():
    # Block 1: Initialisera
    try:
        oscilloskop = initialisera()
    except Exception as e:
        print(f"Initialisering misslyckades: {e}")
        return

    # Block 2: Mätning
    try:
        kanal = "CHANnel1"
        for i in range(30):
            time.sleep(1)
            frekvens = mata(oscilloskop, kanal=kanal)
        if frekvens is None:
            return
    except Exception as e:
        print(f"Mätning misslyckades: {e}")
        return

    # Block 4: Rita sinusvåg
    #plot_sinus_wave(frekvens)

    # Stäng anslutningen till oscilloskopet
    oscilloskop.close()

if __name__ == "__main__":
    main()
