import csv
import pandas as pd
import json
from tabulate import tabulate

def promedio_columna(datos,num_columna): 
    suma = 0
    for i in range(1,len(datos)-1):
        suma += float(datos[i][num_columna])
    print("promedio {}: {}".format( datos[0][num_columna] , round((suma/150),2))) # 150 datos
    
def filas_especie(datos, especie):
    acumulador = 0
    for esp in range(0,len(datos)-1):
        if datos[esp][4] == especie:
            acumulador += 1
    print("Nº filas {}: {}".format(especie, acumulador))


archivo = "data/iris.data"
datos = []
datos.append(["largo_sepalo", "ancho_sepalo", "largo_petalo", "ancho_petalo", "especie"])
with open(archivo,"r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        datos.append(row)

#print(datos)

print(tabulate(datos))

print("Número de filas: ",len(datos))

promedio_columna(datos,0)
promedio_columna(datos,1)
promedio_columna(datos,2)
promedio_columna(datos,3)

filas_especie(datos,"Iris-setosa")
filas_especie(datos,"Iris-versicolor")
filas_especie(datos, "Iris-virginica")

for i in range(0,len(datos)-1):
    for j in range(0,4):
        if i == 1 or i==10 or i == 30 or i==100:
            datos[i][j] = 0
            datos[i][4] = "N/A"

print(tabulate(datos))

print("Número de filas: ",len(datos))


nombre_archivo ="Nuevo-Iris"

with open("data/{}.csv".format(nombre_archivo),"a", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter="\n")
        writer.writerow(datos)
