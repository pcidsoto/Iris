#fuente https://stackoverrun.com/es/q/5154677

import csv
import urllib.request
import codecs

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
ftpstream = urllib.request.urlopen(url)

'''
Usar códecs según lo propuesto por Steven Rumbalski, por lo que no es necesario
leer todo el archivo para decodificar. Reducción del consumo de memoria y
aumento de la velocidad.
'''

csvfile = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))

data = list(csvfile)

print(data)  