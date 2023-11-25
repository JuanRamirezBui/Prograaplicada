import random
import csv

nombre_archivo_csv = 'numeros.csv'

while True:
    
    numero_pseudoaleatorio = random.uniform(0, 1)

    with open(nombre_archivo_csv, 'a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow([numero_pseudoaleatorio])

    print(f'Se ha escrito el número {numero_pseudoaleatorio} en el archivo {nombre_archivo_csv}.')
