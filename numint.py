# coding=UTF-8
from math import sqrt, e, sin, pi

# Definerar funtionen f
def f(x):
    return 2*sin(x)*x+x+1

# Beräkna arean mellan funktionen och x-axeln, mellan -2 och 2. 
a = 0.0
# Delar in intervallet i 4 bitar.
for x1 in [-2, -1, 0, 1]:
    x2 = x1 + 1
    a = a + (x2-x1)*f(x1)

print(f'Arean är cirka {a}')

# Skriv om programmet för att lösa följande uppgifter.
# Implementationen ovan ger ett inte så särkillt noggrant svar. 
# Uppgift 1: Uppatera programmet så du får en area som har 4 decimalers noggranhet.