## .csv file
## Un fichero csv es parecido a una hoja de cálculo

import csv

csv_file = open("intermedio/mi_fichero.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"]) #Con writerow vamos escribiendo las líneas del csv
csv_writer.writerow(["Brais", "Moure", 35, "Python", "https://moure.dev"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()
with open("intermedio/mi_fichero.csv") as mi_otro_csv:
    for line in mi_otro_csv.readlines():
        print(line)