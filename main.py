class CsvDavinciConverter:
    

    def __init__(self):
        self.lista = []
        self.filename = None
        self.output_file = None

    def convert(self, input, output):
        self.lista = self.csv_to_python_list(input)
        self.python_list_to_formatted_csv(self.lista)
        self.lista_to_new_csv_file(self.lista, output)

    def csv_to_python_list(self, file):
        with open(file, 'r') as i:  # Generar lista con base en el archivo CSV
            archivo = []
            for linea in i:
                archivo.append(linea)
        for linea in archivo:  # Generar una lista 2d con las lineas de la primera lista
            columna = []
            for col in linea.replace('"', '').split(","):
                columna.append(col)
            self.lista.append(columna)
        return self.lista

    def edl_to_python_list(self):
        print("EDL FILE")

    def python_list_to_formatted_csv(self, pythonlist, replace1from=":", replace1to=";", replace2from=" ",
                                     replace2to=""):
        for linea in range(
                len(self.lista)):  # Hacer cambios en las strings de la lista para que sea el formato sea el deseado
            for columna in range(len(self.lista[linea])):
                if columna != 19:  # Col number where the chapter markers is. We don't want to change a : for a ; here
                    for n, s in enumerate(self.lista[linea]):
                        self.lista[linea][columna] = self.lista[linea][columna].replace(replace1from, replace1to).replace(
                            replace2from,
                            replace2to)
        return pythonlist

    def lista_to_new_csv_file(self, pythonlist, file):
        with open(file, 'w') as t:  # Escribir el header del archivo csv
            t.write("Marker Name\tDescription\tIn\tOut\tDuration\tMarker Type\t\n")
        with open(file, 'a') as o:
            for i, linea in enumerate(pythonlist):
                if i == 0:  # ignora el header de la lista original
                    pass
                else:
                    o.write(linea[19])
                    o.write("\t\t")
                    if linea[6][:2] == "01":
                        o.write("00")
                        o.write(linea[6][2:])
                    else:
                        o.write(linea[6])
                    o.write("\t")
                    if linea[7][:2] == "01":
                        o.write("00")
                        o.write(linea[7][2:])
                    else:
                        o.write(linea[6])
                    o.write("\t")
                    o.write("00;00;00;00")
                    o.write("\t")
                    o.write("Chapter")
                    o.write("\t")
                    o.write("\n")


