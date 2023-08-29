def factorial():
    print(f'El factorial de {value} es: ', fact)
def error():
    print("Por favor ingrese un valor positivo")
def valor():
   print("Valor: ", value) 
while True:

    value = int(input("Ingrese el número al cúal se le hallará el factorial: "))
    valor()
    a = isinstance(value, int)
    if a == True and value > 0:
        fact = 1
        for i in range (1, value + 1):
            fact = fact*i            
        factorial()
    else:
        error()
