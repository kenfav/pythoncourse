from main import CsvDavinciConverter as dr
from sys import argv

converter = dr()
converter.convert(argv[1], argv[2])
print("FINALIZADO")
