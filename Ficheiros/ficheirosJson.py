import csv
import json

datos = {"nome": "Jose",
         "edad": 30,
         "xenero": "Home"}

with open ("exemplo.json", "w") as ficheiro:
    json.dump(datos, ficheiro)

with open ("exemplo.json", "r") as ficheiro:
    datoJson = json.load(ficheiro)
    print(datoJson)
    print(type(datoJson))

with open ('exemplo.csv', 'a', newline='') as ficheiro:
    writer = csv.writer(ficheiro)
    writer.writerow(datoJson.values())
