# coding=UTF-8
from math import sqrt, e

# Definerar funtionen f
def f(x):
    return sqrt(x)

# Medellutning (k), för f vid x med h
def kf(x,h):
    return (f(x+h)-f(x))/h

# Skriver ut några medellutningar
for h in [1.0,0.5,0.1]:
    x=2
    k=kf(x,h)
    print(f'x={x} & h={h} ger k={k}')

# Skriv om programmet för att lösa följande uppgifter.
# Med funktinen f(x) = x^(1/2)
# Uppgift 1: Vad är f'(2) med tre decimaler
# Uppgift 2: Hur litet kan du göra h innan kvärdet blir knasigt.

# Med funktinen g(x) = x^3*ℯ^(-x^2)
# Uppgift 3: Vad är derivatan g'(1)
# [Svårare] Uppgift 4: För är derivatans g'(x) största värde i intervallet 0<x<5  
