numpar = 0
numimpar = 0
numpo = 0
numne = 0
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
#----------------------------------------

if a % 2 != 0:
    numimpar += 1
  
if b % 2 != 0:
    numimpar += 1
    
if c % 2 != 0:
    numimpar += 1
   
if d % 2 != 0:
    numimpar += 1

if e % 2 != 0:
    numimpar += 1
# -----------------------------------------
if a > 0:
    numpo += 1
  
if b > 0:
    numpo += 1
    
if c > 0:
    numpo += 1
   
if d  > 0:
    numpo += 1

if e  > 0:
    numpo += 1
# -----------------------

if a < 0:
    numne += 1
  
if b < 0:
    numne += 1
    
if c < 0:
    numne += 1
   
if d  < 0:
    numne += 1

if e  < 0:
    numne += 1
print(f'{numpar} valor(es) par(es)')
print(f'{numimpar} valor(es) impar(es)')
print(f'{numpo} valor(es) positivo(s)')
print(f'{numne} valor(es) negativo(s)')