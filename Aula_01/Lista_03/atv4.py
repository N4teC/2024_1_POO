import math

print('Digite a base e a altura do retângulo:')
b = int(input())
h = int(input())

a = b*h
p = (b*2)+(h*2)
d = math.sqrt((b*b)+(h*h))

print('Área =',a,'- Perímetro =',p,'- Diagonal =',d)

