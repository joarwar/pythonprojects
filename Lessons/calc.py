import numpy as np
pi = np.pi

def calc_dia():
    diameter_input = float(input("What's the diameter? "))  
    return diameter_input * pi  

print(calc_dia() )
