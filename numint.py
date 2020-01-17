# coding=UTF-8
from math import sqrt, e, sin, pi

# Definerar funtionen f
def f(x):
    return 2*sin(x)*x+x+1

# Beräkna arean mellan funktionen och x-axeln, mellan -2 och 2. 
a = 0.0
# Delar in intervallet i 4 bitar.
for x1 in [-2.0, -1.0, 0.0, 1.0]:
    x2 = x1 + 1
    b = (x2-x1)
    h = f((x1+x2)/2)
    a = a + b*h

print(f'Arean är cirka {a}')

# Skriv om programmet för att lösa följande uppgifter.
# Implementationen ovan ger ett inte så särkillt noggrant svar. 
# Uppgift 1: Uppdatera programmet så du får en area som har 4 decimalers noggranhet.
# Uppgift 2: Funktionen g(x)=(1-x^2)^0.5 är en halvcirkel. 
#            Använd numerisk integration för att bestämma pi med några decimaler.
# Uppgift 3: Ibland vill man ha en viss noggranhet, ex 2 eller 8 decimaler. 
#            Uppdatera programet så kan bestämma arean, eller pi, med ett givet antal värdesiffror.
#            Tips: Försök skriva ett program som gör smalare och smalare staplar tills dess att du är säker på antal värdesiffror som stämmer.