a=int(input("ingrese el valor del limite inferior ", ))
b=int(input("ingrese el valor del limite superior ", ))
def primos():
    print(f'{i} es un primo')
import time
inicio = time.time()
for i in range(a,b):
    conta = 0
    for n in range(1, i+1):
        residue = i%n
        if residue == 0:
            conta = conta + 1
              
    if conta == 2:
      primos() 
        
fin = time.time()
print("t = ", (fin - inicio)*1000)
