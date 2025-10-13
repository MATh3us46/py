numpar = 0
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

if a % 2 == 0:
    numpar += 1
  
if b % 2 == 0:
    numpar += 1
    
if c % 2 == 0:
    numpar += 1
   
if d % 2 == 0:
    numpar += 1

if e % 2 == 0:
    numpar += 1

print(f'{numpar} valores pares')